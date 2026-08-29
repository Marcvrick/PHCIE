#!/usr/bin/env node
/*
 * sync-sitemap.js — recale chaque <lastmod> de sitemap.xml sur la vraie date
 * de dernière modification de la page.
 *
 * Pourquoi : un <lastmod> périmé fait dépriorer le recrawl par Google. En août
 * 2026, services.html annonçait encore 2026-03-30 alors que la page avait été
 * refaite le 27/08 — GSC ne rattachait plus l'URL au sitemap.
 *
 * Source de la date, dans cet ordre :
 *   1. fichier modifié ou non suivi (git)  -> aujourd'hui (il part au prochain commit)
 *   2. sinon                               -> date du dernier commit qui l'a touché
 * Les mtimes du disque ne sont JAMAIS lues : iCloud les réécrit toutes lors
 * d'une resync, elles indiquaient toutes le 19/08.
 *
 * Usage :  node sync-sitemap.js          applique
 *          node sync-sitemap.js --check  n'écrit rien, sort en 1 si ça dérive
 *
 * Lancé automatiquement par .git/hooks/pre-commit (voir README).
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = __dirname;
const CHECK = process.argv.includes('--check');
const SITEMAP = path.join(ROOT, 'sitemap.xml');
const ORIGIN = 'https://www.pharmaciecharnal.com/';

const git = (...args) =>
    execFileSync('git', args, { cwd: ROOT, encoding: 'utf8', maxBuffer: 32 << 20 });

const today = new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/Paris' });

/* Fichiers modifiés, mis en index, ou non suivis : leur date est aujourd'hui. */
const dirty = new Set([
    ...git('diff', '--name-only', '-z', 'HEAD').split('\0'),
    ...git('ls-files', '--others', '--exclude-standard', '-z').split('\0'),
].filter(Boolean));

/* ponytail: un `git log` par page (66 spawns, ~1 s). Si le sitemap dépasse
   quelques centaines d'URL, passer à un seul `git log --name-only` parsé. */
function lastCommitDate(rel) {
    return git('log', '-1', '--format=%cs', '--', rel).trim();
}

function fileFor(loc) {
    const rel = decodeURIComponent(loc.slice(ORIGIN.length));
    return rel === '' ? 'index.html' : rel;
}

const src = fs.readFileSync(SITEMAP, 'utf8');
const missing = [];
const changed = [];

const out = src.replace(
    /(<loc>)(.*?)(<\/loc>\s*<lastmod>)(.*?)(<\/lastmod>)/g,
    (whole, o1, loc, o2, old, o3) => {
        if (!loc.startsWith(ORIGIN)) return whole;
        const rel = fileFor(loc);
        if (!fs.existsSync(path.join(ROOT, rel))) { missing.push(rel); return whole; }
        const date = dirty.has(rel) ? today : lastCommitDate(rel) || old;
        if (date !== old) changed.push(`${rel}: ${old} -> ${date}`);
        return o1 + loc + o2 + date + o3;
    }
);

for (const m of missing) console.error(`404 en puissance — dans le sitemap, absent du disque : ${m}`);
for (const c of changed) console.log(`   ${c}`);
console.log(`${changed.length} lastmod ${CHECK ? 'à recaler' : 'recalés'}, ${missing.length} URL sans fichier`);

if (CHECK) {
    if (changed.length || missing.length) process.exit(1);
} else if (changed.length) {
    fs.writeFileSync(SITEMAP, out);
}
