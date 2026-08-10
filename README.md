# Site Web - Pharmacie Charnal

Site statique — **www.pharmaciecharnal.com**
Repository : `https://github.com/Marcvrick/Pharmacie-Charnal` · Branche unique `main` (déploiement auto)

---

## Documentation

**Wiki opérationnel (point d'entrée) :** [`../wiki/index.md`](../wiki/index.md)
Design system, workflow blog, Instagram, GMB, SEO, déploiement, pages marques — tout est là.

**Instructions Claude :** [`CLAUDE.md`](CLAUDE.md) — checklists techniques, CSS, schema.org, règles contenu.

**Contenu & voix :** [`/Pharma/CLAUDE-Pharma.md`](../../CLAUDE-Pharma.md) — voix de Laure, règles médicales, skills.

---

## Informations Pharmacie

| | |
|--|--|
| Adresse | 32 Place de Toulouse, 56530 Quéven |
| Téléphone | 02 97 05 09 31 |
| Horaires | Lun-Ven 9h-12h30 / 14h-19h15 · Sam 9h-12h30 · Dim fermé |
| Instagram | @pharmaciecharnalqueven |
| Facebook | /pharmaciecharnal |
| Google Analytics | G-2Q64V6B0QE |

---

## Structure du site

```
website-pharmacie-charnal/
├── index.html
├── histoire.html
├── services.html
├── blog.html
├── contact.html
├── annuaire-sante.html
├── pharmacie-de-garde-queven-hennebont-lorient.html
├── recrutement-preparatrice-pharmacie-queven.html
├── mentions-legales.html
├── donnees-personnelles.html
├── style.css                  # Legacy (articles blog, mentions-légales)
├── style-v2.css               # HIMS design system (pages principales)
├── animations.js
├── robots.txt · sitemap.xml · llms.txt · feed.json · vercel.json · CNAME
├── Nos-marques/               # 16 pages marques + nosmarques.html + TEMPLATE-marque.html
├── Quizzes/                   # 3 quiz publiés + guide hub
├── blog/                      # 19 articles publiés + sources .md numérotées
├── planning/                  # Meta-refresh → https://marcvrick.github.io/PLPH/ (ne pas supprimer)
└── images/ · fonts/ · favicon/
```

**Pages migrées style-v2.css :** histoire, services, contact, blog, annuaire-sante, pharmacie-de-garde, recrutement, nosmarques.
**À migrer :** index.html, mentions-legales.html, donnees-personnelles.html, pages marques individuelles.

**App Planning RH :** repo séparé `https://github.com/Marcvrick/PLPH` (local : `/Users/mc/git-repos/PLPH/`). Ne jamais modifier le planning depuis ce repo.

---

## Commandes rapides

```bash
# Test local
python3 -m http.server 8000

# Déployer
git add [fichiers] && git commit -m "Message" && git push origin main
# JAMAIS --force sur main (branch protection active depuis 19 avril 2026)
```

---

## Changelog

### 10 Août 2026

**Homepage — visuel Dermocosmétique agrandi (non commité) :**
- `.card--dermo .product-feature-img { transform: scale(1.8) }` + sa variante `:hover` (`scale(1.94) translateY(-4px)`). La règle hover doit être dupliquée : `transform` écrase le scale de base, sans elle le pot rétrécit au survol.
- Cause : `images/dermocosmetique-product.png` est un carré 750×750 avec beaucoup de vide autour du sujet, alors que les 3 autres visuels sont détourés serré. Le CSS compense — un recrop de l'image rendrait la règle inutile.
- Vérifié en rendu réel (Puppeteer, 1280px et 390px) : poids visuel aligné sur celui des gélules, pas de rognage sur mobile.

### 4 Août 2026

**Homepage — hero et services fusionnés en un seul bloc (commits `7a23fee`, `ea8791e`) :**
- Le hero et la section « On s'occupe de Vous » ne forment plus qu'une seule `<section class="hero">`, sur un aplat `--pastel-sage`. Ordre des services remis sur celui documenté dans [`CLAUDE.md`](CLAUDE.md) (Ordonnances → Livraison), que le deck inversait.
- Six marqueurs de page générée retirés : badge-pilule au-dessus du H1, capsules de stats en verre dépoli, blobs radiaux du fond, cartes icône+titre+texte, CTA `btn-secondary` délavé (→ `btn-primary` teal), deck empilé `skewY(-7deg)`.
- Les 6 services passent en index typographique `.hero-services-index` (nom | description | flèche), 2 colonnes ≥900px.
- Mobile (≤767px) : description et ligne de chiffres masquées, CTA centré.
- **Supprimés :** `.services-v2`, `.dcard`, le JS « tap en deux temps », et l'emplacement de `videos/pharma-entry-4x3.mp4` (le fichier reste sur disque). ⚠️ Les entrées **21 juin** et **20 juin 2026** ci-dessous décrivent ce deck : elles ne s'appliquent plus.
- Pièges consignés dans [`CLAUDE.md`](CLAUDE.md) § Hero Section : `style-v2.css` impose `grid-template-columns: 1fr 1fr` sur `.hero-container` et `justify-content: center` sur `.hero-cta` — les deux doivent être redéclarés dans le bloc inline.

### 1 Juillet 2026

**Wiki créé :** [`../wiki/`](../wiki/) — 9 pages thématiques (site, design, blog, IG, GMB, SEO, déploiement, marques, log). README nettoyé — documentation détaillée déplacée dans le wiki.

### 29 Juin 2026

**`pharmacie-de-garde` — bandeau dernier article + nettoyage (commits `2b1c195`, `1fb9c23`, `b44d2ef`) :**
- Bandeau « dernier article de blog » auto-fetch depuis `blog.html` (1re `.blog-card`) — se met à jour seul à chaque publication. Filet de secours en dur si `fetch` échoue (http(s) uniquement, pas `file://`).
- Carte « Nous contacter » retirée du bloc « Aussi à la Pharmacie Charnal » (reste 3 cartes).
- Carte « 3237 » recentrée : `margin-left/right: auto` ajouté sur `.info-3237`.

**Dashboard SEO 6 mois :** `SEO TO DO/SEO analysis 6M/dashboard-seo-charnal.html` — bilan Search Console (21 fév – 27 juin 2026) : impressions ×40, clics ×20, position 9,3 → 7,1.

### 21 Juin 2026

**Homepage — deck services : tap en deux temps sur mobile (commit `17e595b`) :**
- Tactile (`@media (hover: none)`) : 1er tap relève la vignette, 2e tap ouvre le lien, tap en dehors redescend.
- État = `.dcard.is-raised` (JS). Le `:hover` est enfermé dans `@media (hover: hover)` → desktop inchangé.

**`services.html` — maillage interne (commit `f3b407a`) :**
- Marques cliquables vers leur page dédiée (Avène, La Roche-Posay, Bioderma, Nuxe, Klorane, Mustela, Boiron, Nat&Form, S.I.D Nutrition, PiLeJe, Bion 3).
- CTA de sortie par carte (`.service-links-row`) : quiz + articles blog pertinents.
- Ancre cassée corrigée : `nosmarques.html#cosmetiques` → `nosmarques.html`.

**Homepage — logos marques agrandis écrans medium (commits `48df976` + `76b6ce5`) :**
- Palier `768–1024px` : logos `120×48` → `156×62`. Avène & Nuxe +30% supplémentaire.

### 20 Juin 2026

**Homepage mobile — deck conservé sur mobile + ombres cartes quiz :**
- Deck empilé conservé sur mobile (plus aplati en liste). Alignement haut, pas 50px, `isolation: isolate`.
- Ombres sur `.product-feature-card` : `box-shadow: 0 12px 32px -18px rgba(31,33,33,.55)`.
- Foldables (480–767px) : grille quiz `max-width: 440px; margin: 0 auto`.

### 14 Mai 2026

**Articles #19 et #20 publiés :**
- #19 — Chiens & chats : les essentiels santé (~2200 mots, ANSES/ANMV/ESCCAP/VIDAL/CAPAE-Ouest)
- #20 — Peau de bébé 0-3 ans (~1900 mots, SFP/HAS/ANSM/SFD). Corrections médicales post-fact-check.
- Source .md article #18 shampoings créée — HTML à générer.

**Page Speed audit (toutes pages principales) :**
- `<link rel="preload" as="image">` redondant supprimé sur 19 articles (remplacé par `fetchpriority="high"`)
- Titles ≤60 chars sur 4 pages. Google Fonts async sur 10 pages. `--gray-light` → `#767676` (WCAG AA).

### 7 Mai 2026

**Fix logos hero pages marques (6 pages, commit `6192b3f`) :** placeholders et noms de fichiers erronés corrigés sur avene, pileje, aragan, arkopharma, mustela, boiron.

**Fix CSS padding `.laure-blog-link` (9 pages marques, commit `fe9252a`) :** `var(--space-20)` non défini → `padding: 20px 24px` hardcodé.

**Homepage quiz : 3×2 bento → 4×1 rangée (commit `2d3306d`).** Hero mobile restructuré : H1 → photo → CTA (commit `6d6d7ea`).

**`blog/BRAND-BLOG-MAPPING.md` créé** — référence maillage SEO marque → article.

### 6 Mai 2026

**SEO — Audit GSC + optimisations homepage et page garde :** canonical corrigé, title/meta enrichis, schema Pharmacy avec `areaServed` (8 villes), section blog magazine-style auto-fetch. Réindexation demandée pour 8 pages.

### 11 Avril 2026

**Vercel + Clean URLs :** `vercel.json` ajouté (`cleanUrls: true`, `trailingSlash: false`). Redirects 301 pour sous-dossiers avec espaces (`Moral en berne/`, `Peau Seche/`).

### 20 Février 2026

**Quizzes :** 3e quiz publié, page guide hub créée, "Quizzes santé" ajouté au dropdown navbar (43 pages).

### 6 Février 2026

**style-v2.css :** fix menu mobile dropdown (display flex, invisible bridge, touch-action). Logos marques cliquables sur nosmarques.html.

---

**Dernière mise à jour :** 10 Août 2026
**Statut :** En ligne sur www.pharmaciecharnal.com · Migration style-v2.css en cours
