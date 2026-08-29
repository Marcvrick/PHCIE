#!/usr/bin/env node
/*
 * build.js — tamponne les partials partagés dans chaque page HTML, sur place.
 *
 * Pourquoi sur place et non vers dist/ : les 73 pages ont chacune un <head> sur
 * mesure (title, meta, canonical, 191 blocs JSON-LD, 1,58 Mo de <style> inline).
 * Les passer en pages-source + CONFIG demanderait de déplacer tout ça, et de
 * basculer Vercel sur buildCommand/outputDirectory avec 60 URL déjà indexées.
 * Ici on ne touche qu'aux régions dupliquées, celles qui dérivent :
 *
 *   1. <nav class="navbar"> … </nav>        <- _partials/navbar.html
 *   2. le <ul> sous <h4>Navigation</h4>     <- _partials/footer-nav.html
 *   3. <script src="nav.js" defer>          <- injecté avant </body>
 *   4. la bande teal juste avant <footer>   <- injectée (voir TEAL_BAND)
 *   5. la section « Au comptoir » d'index   <- les 5 premières .blog-card
 *      (1 article vedette + 4 secondaires)      de blog.html
 *
 * Le reste de la page n'est jamais lu ni réécrit. Idempotent : deux passes
 * consécutives ne produisent aucun diff.
 *
 * Usage :  node build.js          applique
 *          node build.js --check  n'écrit rien, sort en 1 si une page dérive
 */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const CHECK = process.argv.includes('--check');

// Dossiers hors site : sauvegardes, maquettes, contenu non publié.
const SKIP_DIRS = new Set([
    '.git', 'node_modules', '_partials', 'favicon', 'images', 'fonts', 'videos',
    'Design Test Index', 'index-redesign', 'docs', 'Blog posts IG', 'planning',
    'Pharmacies de garde', 'GMB', 'photos', 'logos',
]);

// Une page sans <nav class="navbar"> n'est pas une page de contenu (stub de
// vérification Google, infographie autonome, redirection) — on la laisse.
const NAVBAR_OPEN = /<nav\b[^>]*\bclass="[^"]*\bnavbar\b[^"]*"[^>]*>/;

const navbarTpl = read('_partials/navbar.html').trimEnd();
const footerNavTpl = read('_partials/footer-nav.html').trimEnd();

/* Quelle entrée de menu marquer `active`, d'après le chemin de la page. */
function navKey(rel) {
    const base = path.basename(rel);
    if (rel.startsWith('blog/') || base === 'blog.html') return 'blog';
    if (rel.startsWith('Nos-marques/')) return 'marques';
    if (rel.startsWith('Quizzes/')) return 'quiz';
    if (base === 'index.html') return 'accueil';
    if (base === 'services.html') return 'services';
    if (base === 'histoire.html') return 'histoire';
    if (base === 'annuaire-sante.html') return 'annuaire';
    if (base === 'contact.html') return 'contact';
    if (base.startsWith('pharmacie-de-garde')) return 'garde';
    if (base.startsWith('recrutement')) return 'recrutement';
    if (base.startsWith('test-angine') || base.startsWith('location-tire-lait')
        || base.startsWith('automesure-tension') || base.startsWith('vaccination-grippe')
        || base.startsWith('bas-de-contention')) return 'services';
    return null;
}

function render(tpl, rel) {
    const depth = rel.split('/').length - 1;
    let out = tpl.replace(/\{\{ROOT\}\}/g, '../'.repeat(depth));
    const key = navKey(rel);
    if (key) {
        out = out.replace(
            new RegExp(`(class="nav-link[^"]*)(" data-nav="${key}")`),
            '$1 active$2'
        );
    }
    return out;
}

/* Fin de la balise ouverte à `start`, en comptant les imbrications. */
function closeAt(html, start, tag) {
    const re = new RegExp(`</?${tag}\\b`, 'g');
    re.lastIndex = start;
    let depth = 0, m;
    while ((m = re.exec(html))) {
        depth += m[0][1] === '/' ? -1 : 1;
        if (depth === 0) return html.indexOf('>', m.index) + 1;
    }
    return -1;
}

function replaceNavbar(html, rel) {
    const m = NAVBAR_OPEN.exec(html);
    if (!m) return null;
    const end = closeAt(html, m.index, 'nav');
    if (end < 0) throw new Error(`${rel}: <nav class="navbar"> non refermée`);
    return html.slice(0, m.index) + render(navbarTpl, rel) + html.slice(end);
}

function replaceFooterNav(html, rel) {
    const h4 = /<h4\b[^>]*>\s*Navigation\s*<\/h4>/i.exec(html);
    if (!h4) return html;
    const ulStart = html.indexOf('<ul', h4.index + h4[0].length);
    if (ulStart < 0) return html;
    // Un <ul> qui ne suit pas immédiatement le titre appartient à autre chose.
    if (html.slice(h4.index + h4[0].length, ulStart).trim() !== '') return html;
    const end = closeAt(html, ulStart, 'ul');
    if (end < 0) throw new Error(`${rel}: <ul> de navigation footer non refermé`);
    // On ne remplace que les <li> : la balise <ul> de la page garde ses classes
    // (footer-links sur 4 pages), donc aucun style n'est perdu.
    const inner = html.indexOf('>', ulStart) + 1;
    const close = html.lastIndexOf('</ul', end);
    const indent = /\n([ \t]*)$/.exec(html.slice(inner, close));
    return html.slice(0, inner) + '\n' + ' '.repeat(24) + render(footerNavTpl, rel)
        + '\n' + (indent ? indent[1] : ' '.repeat(20)) + html.slice(close);
}

/* La bande teal qui sépare le contenu du footer, présente sur l'accueil.
   Couleur en dur plutôt que var(--teal-pro) : les 8 pages Nos-marques
   redéfinissent --teal-pro sur la couleur de la marque (Aragan cyan, Pileje
   navy…), la bande y virait donc au bleu ou au vert. Le footer, lui, est
   charcoal partout.
   Les pages Quizzes ont un <body> en flex column + align-items:center : sans
   `width:100%` la bande se réduit à sa largeur de contenu (zéro), et sans
   `flex-shrink:0` ses 80px se font écraser. Le footer de ces pages porte déjà
   `width:100%` pour la même raison. */
const TEAL_BAND = '<div style="background: #2D5F5D; height: 80px;'
    + ' width: 100%; flex-shrink: 0;"></div>';
const TEAL_BAND_RE =
    /[ \t]*<!-- Teal band above footer -->\n[ \t]*<div style="[^"]*"><\/div>\n+[ \t]*/;

function insertTealBand(html, rel) {
    // On retire la bande existante avant de la réécrire : idempotent, et une
    // bande qui aurait dérivé (autre hauteur, autre couleur) est remise d'aplomb.
    const out = html.replace(TEAL_BAND_RE, (m) => /\n([ \t]*)$/.exec(m)?.[1] ?? '');
    const m = /<footer\b[^>]*>/.exec(out);
    if (!m) return out;
    const indent = /\n([ \t]*)$/.exec(out.slice(0, m.index));
    const ind = indent ? indent[1] : '    ';
    return out.slice(0, m.index)
        + `<!-- Teal band above footer -->\n${ind}${TEAL_BAND}\n\n${ind}`
        + out.slice(m.index);
}

function injectNavScript(html, rel) {
    if (/<script[^>]+src="[^"]*nav\.js"/.test(html)) return html;
    const depth = rel.split('/').length - 1;
    const tag = `    <script src="${'../'.repeat(depth)}nav.js" defer></script>\n`;
    const i = html.lastIndexOf('</body>');
    if (i < 0) throw new Error(`${rel}: pas de </body>`);
    return html.slice(0, i) + tag + html.slice(i);
}

function read(rel) {
    return fs.readFileSync(path.join(ROOT, rel), 'utf8');
}

/* ------------------------------------------------------------------ *
 * Section « Au comptoir » de l'accueil, alignée sur blog.html.
 *
 * index.html embarquait les 5 articles en dur et un fetch('blog.html') les
 * réécrivait au chargement : le visiteur voyait d'abord l'ancien article, image
 * comprise, puis la substitution. On les écrit ici, au build. Le fetch reste en
 * place comme filet (il ne réécrit plus que des valeurs identiques).
 * ------------------------------------------------------------------ */

/* Les 5 premières cartes de blog.html, dans l'ordre de publication. */
function readBlogCards(n) {
    const html = read('blog.html');
    const cards = [];
    const re = /<article class="blog-card\b/g;
    let m;
    while ((m = re.exec(html)) && cards.length < n) {
        const end = closeAt(html, m.index, 'article');
        if (end < 0) throw new Error('blog.html : <article class="blog-card"> non refermée');
        const card = html.slice(m.index, end);
        const pick = (r) => (r.exec(card) || [, null])[1];
        cards.push({
            url: pick(/<a href="([^"]*)"/),
            img: pick(/<div class="blog-image-placeholder"[^>]*>\s*<img src="([^"]*)"/),
            alt: pick(/<div class="blog-image-placeholder"[^>]*>\s*<img [^>]*\balt="([^"]*)"/),
            date: pick(/<span class="blog-date">([\s\S]*?)<\/span>/),
            title: pick(/<h2 class="blog-title">([\s\S]*?)<\/h2>/),
            excerpt: pick(/<p class="blog-excerpt">([\s\S]*?)<\/p>/),
        });
    }
    return cards;
}

/* La balise ouvrante qui porte id="…", sous forme [début, fin[. */
function tagRangeById(html, id, rel) {
    const at = html.indexOf(`id="${id}"`);
    if (at < 0) throw new Error(`${rel} : id="${id}" introuvable`);
    return [html.lastIndexOf('<', at), html.indexOf('>', at) + 1];
}

function setAttr(html, id, attr, value, rel) {
    if (value == null) return html;
    const [start, end] = tagRangeById(html, id, rel);
    const tag = html.slice(start, end);
    const re = new RegExp(`(\\s${attr}=")[^"]*(")`);
    if (!re.test(tag)) throw new Error(`${rel} : ${id} n'a pas d'attribut ${attr}`);
    return html.slice(0, start) + tag.replace(re, `$1${value}$2`) + html.slice(end);
}

/* Le contenu de l'élément porteur de id="…". Ces éléments (span, h2, h3, p)
   n'ont pas d'enfants : le premier `</` rencontré est bien leur fermeture. */
function setInner(html, id, value, rel) {
    if (value == null) return html;
    const [, open] = tagRangeById(html, id, rel);
    const close = html.indexOf('</', open);
    if (close < 0) throw new Error(`${rel} : ${id} non refermé`);
    return html.slice(0, open) + value.trim() + html.slice(close);
}

function syncHomeBlog(html, rel) {
    if (rel !== 'index.html') return html;
    const cards = readBlogCards(5);
    if (!cards.length) return html;

    const [f, ...minis] = cards;
    let out = html;
    out = setAttr(out, 'latest-article-image-link', 'href', f.url, rel);
    out = setAttr(out, 'latest-article-link', 'href', f.url, rel);
    out = setAttr(out, 'latest-article-img', 'src', f.img, rel);
    out = setAttr(out, 'latest-article-img', 'alt', f.alt, rel);
    out = setInner(out, 'latest-article-date', f.date, rel);
    out = setInner(out, 'latest-article-title', f.title, rel);
    out = setInner(out, 'latest-article-excerpt', f.excerpt, rel);

    minis.forEach((c, i) => {
        const n = i + 1;
        out = setAttr(out, `mini-card-${n}`, 'href', c.url, rel);
        out = setAttr(out, `mini-img-${n}`, 'src', c.img, rel);
        out = setAttr(out, `mini-img-${n}`, 'alt', c.alt || '', rel);
        out = setInner(out, `mini-date-${n}`, c.date, rel);
        out = setInner(out, `mini-title-${n}`, c.title, rel);
    });
    return out;
}

function walk(dir, out = []) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
        if (e.isDirectory()) {
            if (!SKIP_DIRS.has(e.name)) walk(path.join(dir, e.name), out);
        } else if (e.name.endsWith('.html')) {
            out.push(path.relative(ROOT, path.join(dir, e.name)));
        }
    }
    return out;
}

let stamped = 0, drifted = [], skipped = 0;

for (const rel of walk(ROOT).sort()) {
    const before = read(rel);
    const withNav = replaceNavbar(before, rel);
    if (withNav === null) { skipped++; continue; }
    const after = syncHomeBlog(
        injectNavScript(insertTealBand(replaceFooterNav(withNav, rel), rel), rel), rel);
    stamped++;
    if (after === before) continue;
    drifted.push(rel);
    if (!CHECK) fs.writeFileSync(path.join(ROOT, rel), after);
}

const verb = CHECK ? 'dérivent' : 'réécrites';
console.log(`${stamped} pages tamponnées, ${skipped} sans navbar (ignorées)`);
console.log(`${drifted.length} ${verb}`);
for (const d of drifted) console.log(`   ${d}`);

if (CHECK && drifted.length) {
    console.error('\n--check : ces pages ne sont plus à jour. Lancer `node build.js`.');
    process.exit(1);
}
