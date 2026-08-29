# CLAUDE.md - Site Web Pharmacie Charnal

> Instructions spécifiques pour le développement et la maintenance du site web.
> Pour les règles de contenu, ton de voix et pédagogie, voir `/Pharma/CLAUDE-Pharma.md`

---

## Configuration GitHub Pages

**Repository:** `https://github.com/Marcvrick/Pharmacie-Charnal`
- **Branche principale:** `main` (déploiement automatique)
- **Branche de travail:** `pharmacie-charnal`
- **GitHub Pages:** Activé sur `main`

**Custom Domain:**
- **URL canonique:** `https://www.pharmaciecharnal.com` (TOUJOURS .com, JAMAIS .fr)
- **Fichier CNAME:** Contient `www.pharmaciecharnal.com`
- **DNS:** CNAME → `marcvrick.github.io`
- **HTTPS:** Activé

**Workflow Git:**
```bash
# Seule branche active: main (deploiement automatique GitHub Pages)
# Avant toute session: git fetch && git pull --rebase
# JAMAIS de git push --force sur main (branch protection activée 19 avril 2026)
git add [fichiers] && git commit -m "Message" && git push origin main
```

## App Planning RH: Repo SÉPARÉ

L'app de planning RH n'est PLUS dans ce repo depuis le 19 avril 2026.

- **Ancien emplacement:** `planning.html` à la racine du site (SUPPRIMÉ)
- **Repo dédié:** `https://github.com/Marcvrick/PLPH` (renommé depuis `pharmacie-charnal-planning` pour ne pas exposer "planning" dans l'URL publique du repo)
- **URL de production:** `https://marcvrick.github.io/PLPH/`
- **Local:** `/Users/mc/git-repos/PLPH/`

**Raison:** un force-push sur le repo site pour modifier planning.html avait écrasé tout l'historique du site public (incident 19 avril). La séparation prévient ce scénario.

Si on te demande de modifier le planning, l'app RH, ou les vacances, **va travailler dans l'autre repo**. Ne touche jamais au site pour ces demandes.

### Redirection `/planning` → PLPH

Pour préserver l'ancienne URL publique `https://www.pharmaciecharnal.com/planning`, le site sert un fichier `planning/index.html` qui contient un meta-refresh + JS redirect vers `https://marcvrick.github.io/PLPH/`.

- **Fichier:** `planning/index.html` (ne PAS supprimer)
- **Comportement:** GitHub Pages sert le dossier sur `/planning` → meta refresh `0s` → `window.location.replace` vers PLPH
- **Note:** `vercel.json` contient aussi une règle `/planning`, mais GitHub Pages l'ignore, elle est conservée au cas où le site migrerait un jour vers Vercel

---

## Charte Graphique

### Palette de Couleurs

```css
:root {
    --sage: #7C9885;           /* Vert naturel principal */
    --sage-light: #9DB3A4;
    --sage-dark: #5F7A68;
    --teal: #2D5F5D;           /* Teal professionnel */
    --teal-dark: #1E4644;
    --blue: #4A7C8E;           /* Bleu confiance */
    --cream: #F5F1E8;          /* Crème chaleureux */
    --white: #FFFFFF;
    --black: #1A1A1A;
    --accent: #b4a6d7;         /* Lavande "Au Comptoir" */
    --accent-hover: #9b8bc4;
}
```

**Dashboard Ventes (palette spécifique):**
- Fond: `#FAF8F5` | Cartes: `#FFFFFF` | Bordures: `#E8E3DA`
- Titres: `#2D5F5D` | Secondaire: `#7C9885` | Complémentaire: `#4A7C8E`
- Positif: `#50A686` | Warning: `#FF9F5A` | Alerte: `#C0392B`

### Typographie

- **Headings:** Georgia, Crimson Pro, serif
- **Body:** -apple-system, San Francisco, DM Sans, sans-serif

---

## Structure des Fichiers

**Pages principales:**
```
index.html, histoire.html, services.html, blog.html, contact.html
mentions-legales.html, donnees-personnelles.html
pharmacie-de-garde-queven-hennebont-lorient.html
recrutement-preparatrice-pharmacie-queven.html
annuaire-sante.html
```

**Blog:** `blog/*.html` (13 articles). Sources .md organisees dans des dossiers numerotes (`01-prevenir-maux-hiver/`, `04-detox-apres-fetes/`, ..., `12-troubles-sommeil/`), numerotation alignee sur les posts GMB. Les .html restent a la racine de `blog/` (URLs live du site).
**Marques:** `Nos-marques/*.html` (16 pages + nosmarques.html index + TEMPLATE-marque.html)
**Quiz:** `Quizzes/*.html` (quiz-automedication, quiz-soin-peau, quiz-produits-naturels, quiz-coming-soon, guide-quizzes-sante)
**Assets:** `images/`, `style.css`, `style-v2.css`, `animations.js`, `nav.js`
**Partials:** `_partials/navbar.html`, `_partials/footer-nav.html` + `build.js`
**Guides:** `Guide Badge produit style HIMS.md`

### Régions générées par build.js: INTERDIT de les éditer dans une page

`build.js` réécrit cinq régions dans les 74 pages, et rien d'autre:

1. `<nav class="navbar">` depuis `_partials/navbar.html`
2. le `<ul>` sous `<h4>Navigation</h4>` du footer depuis `_partials/footer-nav.html`
3. `<script src="nav.js" defer>` avant `</body>`
4. la bande teal de 80px juste avant `<footer>` (couleur en dur `#2D5F5D`, plus
   `width: 100%; flex-shrink: 0` sans quoi elle disparaît sur les pages `Quizzes/`)
5. la section « Au comptoir » d'`index.html`, depuis les 5 premières `.blog-card` de `blog.html`

Les modifier passe **toujours** par la source, puis `node build.js`. Éditer la navbar d'une page
directement, ou copier-coller l'en-tête d'une page existante pour en créer une nouvelle, recrée
le bug du 12 août 2026 : 13 articles avaient dérivé, leur menu mobile ne s'ouvrait plus, et
« Quiz santé » était inatteignable depuis ces pages.

Publier un article demande de l'ajouter à `blog.html` **puis** de lancer `node build.js`, sinon
l'accueil reste sur l'article précédent et son image clignote au chargement.

`node build.js --check` sort en 1 si une page a dérivé. Le hook `pre-commit` le lance et refuse
le commit. Le comportement du hamburger vit dans `nav.js` seul, jamais dans un script de page.

---

## Règles de Contenu Web

### Marques Approuvées

**RÈGLE:** Seules les marques réellement vendues peuvent être mentionnées.

**Cosmétiques:** Bioderma, La Roche-Posay, Avène, Nuxe, La Rosée, Mustela, Klorane
**Compléments:** PiLeJe, S.I.D Nutrition, Boiron, Aragan, Nat&Form, Bion 3, Biogaran

**❌ Ne JAMAIS inventer de marques**

### Vérification Vidal (OBLIGATOIRE)

**Toute information médicamenteuse doit être vérifiée avec le Vidal avant publication** : contre-indications, âges limites, posologies, conditions de délivrance (OTC vs prescription). Ne jamais écrire une recommandation médicale approximative — la précision est non négociable sur un site de pharmacie.

Exemples de pièges courants :
- ❌ "Le lopéramide est contre-indiqué chez l'enfant" → trop vague (CI absolue < 2 ans, prescription 2-8 ans, OTC variable selon forme)
- ❌ "Pas d'anti-vomitif sans avis médical" → inexact (Vogalib OTC dès 6 ans, max 2 jours)
- ✅ Toujours préciser : l'âge, la forme galénique, OTC ou prescription, la durée max sans avis médical

### CTAs (Calls-to-Action)

**✅ Autorisé:** "Passez nous voir", "Venez en pharmacie", "N'hésitez pas à venir"
**❌ Interdit:** "Contactez-nous", "Appelez-nous", "Prenez rendez-vous"

**Maillage interne — choix par contexte, pas par chronologie (OBLIGATOIRE):** Tout lien interne dans un article (CTA mid-article, "À lire aussi" en intro, navigation bas d'article) doit pointer vers l'article qui **complète le mieux le sujet traité**, pas vers le dernier article publié. Exemple: pour un article "Stress des examens des ados", le lien pertinent est l'article sommeil ou l'article fatigue/moral, pas l'article courbatures juste parce qu'il a été publié juste avant. Si aucun article existant n'est pertinent, ne pas forcer le lien. Pas de bandeau "★ 4,9/5 Google" ou autre social proof dans les CTAs.

**Navigation bas d'article:** Renommer le bloc "Article précédent" → "Pour aller plus loin" (ou "À lire aussi") et y placer l'article le plus complémentaire au sujet, choisi par contexte. Le tri chronologique (article précédent / suivant) est interdit — il génère des liens incohérents quand les sujets ne se suivent pas.

**Liens contextuels sur mots-clés dans le corps du texte (OBLIGATOIRE sur chaque nouvel article):** En plus des blocs "À lire aussi" et de la navigation bas d'article, identifier dans le corps du texte 1 à 2 mots-clés qui renvoient naturellement vers un autre article existant. Les insérer sous forme de `<a href="...">mot-clé</a>` directement dans la phrase, sans modifier le texte. Règles:
- Cibler la **première occurrence** du mot-clé dans le body (pas dans les meta, schémas ou nav)
- Le lien doit être naturel: "paracétamol" → article paracétamol/ibuprofène, "compléments alimentaires" → article 13-compléments, "fatigue" → article fatigue hivernale, "troubles du sommeil" → article sommeil, "stress" → article stress examens ou crampes, "douleurs articulaires" → article humidité/arthrose, "tiques" → article tiques Bretagne
- Ne jamais forcer: si aucun mot-clé pertinent n'apparaît naturellement, ne pas ajouter de lien
- Ne pas dupliquer un lien déjà présent dans le même article (vérifier les blocs "À lire aussi" existants)

### Ton de Voix Blog (Voix de Laure — OBLIGATOIRE)

**Chaque article de blog doit être écrit dans la voix de Laure.** Référence: article "Moral en berne".

- **"Je" pour l'expertise personnelle:** "L'alternative que je privilégie", "Je vérifie toujours..."
- **"Nous" pour l'équipe/la pharmacie:** "Passez nous voir", "Chez nous", "Nous prendrons le temps"
- **Conversationnel:** Parle comme au comptoir, pas comme une encyclopédie médicale
- **Franche et empathique:** "Parlons franchement", "vous n'êtes pas seul(e)"
- **Ancrée localement:** Météo bretonne, vie à Quéven, références concrètes
- **Vulgarisatrice:** Images parlantes ("la boule au ventre"), mécanismes expliqués simplement
- **Pas d'autopromotion:** Éviter "je recommande souvent/régulièrement/fréquemment" — "je recommande" suffit. Pas d'adverbes de fréquence qui en font trop.

**Formulations naturelles:**
- ✅ "Chez nous", "Notre pharmacie", "Nous proposons"
- ❌ "À la Pharmacie Charnal", "La Pharmacie Charnal propose..."

### Informations Pharmacie

- **Adresse:** 32 Place de Toulouse, 56530 Quéven
- **Téléphone:** 02 97 05 09 31
- **Horaires:** Lun-Ven 9h-12h30/14h-19h15 | Sam 9h-12h30 | Dim fermé
- **Instagram:** `@pharmaciecharnalqueven`
- **Facebook:** `/pharmaciecharnal`

---

## Optimisation IA (Blog)

### Règles Obligatoires

1. **Questions en H2/H3:** Au moins 50% doivent être des questions explicites
   - ✅ "Comment protéger sa peau du froid breton ?"
   - ❌ "Protection peau hiver"

2. **FAQ Schema:** Chaque article doit inclure un markup FAQ (3-5 Q&A)
   ```html
   <script type="application/ld+json">
   {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [...]}
   </script>
   ```

3. **Hyper-localisation:** Mentionner Quéven, Bretagne, Morbihan, climat océanique

4. **Crédibilité:** Mécanismes biologiques, dosages précis, noms scientifiques

### robots.txt

Autoriser: GPTBot, PerplexityBot, Claude-Web, Google-Extended

---

## Performance Mobile (RÈGLE OBLIGATOIRE — pages marques)

### Google Fonts — chargement non-bloquant

**JAMAIS `<link rel="stylesheet">` synchrone pour Google Fonts** — c'est un render-blocker qui retarde FCP/LCP de 1–2s sur mobile (Lighthouse 69 → cible 85+).

**Pattern obligatoire sur toutes les pages marques :**
```html
<!-- Fonts — non-render-blocking -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap"></noscript>
```

Appliqué sur les 15 pages marques le 2026-05-12.

### Hero photo — `<img>` obligatoire, PAS de CSS background

**JAMAIS `background: url(...)` pour le hero photo** — le browser preload scanner ne trouve pas les CSS backgrounds pendant le parse HTML. Résultat : LCP +1–2s vs un `<img>`.

**Pattern obligatoire (appliqué sur les 15 pages marques le 2026-05-12) :**

```css
/* CSS : pas de background sur .hero */
.hero { position: relative; min-height: calc(100vh - 120px); ... overflow: hidden; }

.hero-img {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    object-fit: cover; object-position: center; z-index: 0;
}
@media (max-width: 1023px) { .hero-img { object-position: 65% center; } }

.hero::before { ...; z-index: 1; /* overlay doit être au-dessus de l'img */ }
.hero-content { position: relative; z-index: 2; }
```

```html
<!-- HTML : premier enfant de <section class="hero"> -->
<img src="logos/{BrandName}-hero.jpg" alt="" class="hero-img"
     fetchpriority="high" loading="eager" decoding="async" aria-hidden="true">
```

- **Pas de `<link rel="preload" as="image">`** — le `fetchpriority="high"` sur l'`<img>` suffit et est plus fiable.
- `object-position` remplace `background-position` pour le recadrage mobile (ajuster % selon position du sujet dans la photo).

### Goulots restants (non résolus — info)

- **TBT ~150ms** : ~1 000 lignes de CSS inline par page + 40 éléments `.reveal` — externaliser le CSS (nécessite build step ou migration Vercel)
- **TTFB / FCP floor ~2.5s** : GitHub Pages CDN sans contrôle des cache headers — Vercel (`vercel.json` déjà présent) résoudrait ça avec edge caching

---

## Spécifications Techniques

### Google Analytics

**ID:** `G-2Q64V6B0QE`

Code à insérer dans `<head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2Q64V6B0QE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-2Q64V6B0QE');
</script>
```

### Carte Leaflet

- **Leaflet:** v1.9.4 (sans integrity hash)
- **PapaParse:** v5.4.1
- **Données:** `professionnels-sante-queven-carte.csv`
- **Markers:** Pharmacie en rouge, autres en bleu

### CSS - Règles Critiques

**Footer Navigation (mobile):**
```css
@media (max-width: 767px) {
    .footer-col:nth-child(2) { display: none; }
}
```

**Copyright visible:** `color: var(--white); opacity: 0.8;`

**Images blog/marque (homepage):**
- `.editorial-image` et `.brand-spotlight-logo` : `max-width: 84%` (bords alignes verticalement)
- Mobile : images et textes centres (`margin: 0 auto`, `text-align: center`)
- La Rosee SVG : dimensions explicites `width="125" height="34"` requises pour le rendu

**Boutons navigation:** `background: linear-gradient(135deg, var(--cream-dark), var(--beige));`

### Fichiers CSS

- `style-v2.css`: Pages principales (index, services, histoire, contact, pharmacie-de-garde, recrutement, annuaire-sante, nosmarques index, blog.html)
- `style.css`: Articles blog individuels (`blog/*.html`), mentions-legales, donnees-personnelles
- **Pages marques (Nos-marques/*-page.html):** CSS inline (pas de stylesheet externe). Chaque page contient ~3400 lignes de `<style>` avec variables CSS propres + couleurs de la marque.
- **IMPORTANT:** La navbar doit etre visuellement identique entre `style.css` et `style-v2.css`. Le bouton "Au comptoir" (`.nav-link-blog`) doit toujours rester lavande `#b4a6d7` — ne PAS ajouter de `.nav-link-blog.active` qui assombrit la couleur.

---

## Typographie Francaise (CRITIQUE)

### Accents
Verifier systematiquement:
- ✅ **Queven** (pas "Queven")
- ✅ **Decouvrez**, **francaise**, **experience**

Emplacements prioritaires: `<meta description>`, header, footer

### Ponctuation

**RÈGLE ABSOLUE:** `!`, `?` et `:` doivent TOUJOURS être collés au dernier mot du mot précédent (pas d'espace avant)

- ✅ `symptomes?` (pas `symptomes ?`)
- ✅ `comment tenir le coup en fin d'hiver?`
- ✅ `Venez nous voir!`
- ✅ `Crampes abdominales: comprendre et soulager`
- ✅ `L'essentiel en 3 points:`
- ❌ `symptomes ?` (INCORRECT)
- ❌ `Venez nous voir !` (INCORRECT)
- ❌ `Crampes abdominales : comprendre` (INCORRECT)

Vérifier systématiquement: titres, h1-h6, meta descriptions, textes visibles

---

## Synchronisation Titres Blog

Quand on modifie un titre d'article, mettre à jour:
1. Dans l'article: `<title>`, meta tags, Schema.org, `<h1>`
2. Dans `blog.html`: carte article
3. Dans autres articles: navigation "Article précédent/suivant"

---

## Homepage - Structure et Design

### Hero Section — bloc unifie (refonte 2026-08-04)

Le hero et l'ancienne section « On s'occupe de Vous » ne font plus qu'une seule
`<section class="hero">`, sur un aplat `--pastel-sage`. L'ancienne `.services-v2`
(deck de cartes empilees en `skewY(-7deg)`) est supprimee : CSS, HTML et le JS
« touch two-step » associe.

Structure interne, dans `.hero-container` :

1. `.hero-top` — `.hero-lede` a gauche (H1 / description / CTA), photo
   `images/hp PC.jpg` a droite dans `.hero-figure`.
2. `.hero-facts` — les trois chiffres (40 ans / 6j-7 / 4,9 Google) en une ligne
   composee sous un filet, pleine largeur. Ce ne sont PLUS des capsules.
3. `.hero-services` — titre `<h2>` « On s'occupe de Vous » puis
   `.hero-services-index` : 6 liens `.svc` en index typographique
   (nom | description | fleche), 2 colonnes ≥900px. Ce ne sont PLUS des cartes.

**Ce qui a ete retire volontairement — ne pas remettre :**

- **Le badge-pilule** au-dessus du H1 (« Depuis plus de 40 ans a Queven »). Un
  eyebrow au-dessus d'un titre est le tell le plus reconnaissable d'une page
  generee. L'info vit maintenant dans `.hero-facts`.
- **Les capsules de stats** en verre depoli (`backdrop-filter`).
- **Les deux blobs radiaux** `.hero::before` / `.hero::after`.
- **Les 6 cartes** icone + titre + texte : la carte est le conteneur par defaut,
  et six cartes identiques comme structure de page ne disent rien.
- **La video** `videos/pharma-entry-4x3.mp4` : elle n'a plus d'emplacement dans le
  bloc. Le fichier reste sur disque, libre pour la page services.

Breakpoints :
- **≥ 900px** : `.hero-top` en 2 colonnes, index services en 2 colonnes.
- **≤ 899px** : `.hero-top` et `.hero-lede` en `display: contents`, ordre
  H1 → photo → description → CTA → chiffres → services.
- **≤ 767px** : description ET ligne de chiffres masquees, CTA centre (le libelle passe sur deux lignes, `text-align: center` sur le bouton). **≤ 619px** : la fleche `.svc-go` doit etre
  placee explicitement (`grid-column: 2; grid-row: 1`), sinon elle tombe sous la
  description. **≤ 559px** : les chiffres s'empilent.

Pieges :
- `style-v2.css` definit `.hero-container { grid-template-columns: 1fr 1fr }` a
  ≥1024px et `.hero-cta { justify-content: center }`. Le bloc inline **doit**
  redeclarer les deux, sinon le hero et les services se retrouvent cote a cote et
  tout se centre sur mobile.
- Le CTA est passe de `btn-secondary` (contour delave) a `btn-primary` (aplat
  teal). Un bouton fantome sur un aplat pale ne se voit pas.
- Les accents de couleur des services viennent des classes
  `.card--teal|blue|lavender|sage|peach` qui posent `--card-accent` (fleche,
  nom au survol, voile de fond).

### Badges Quiz (sous le marquee)
4 badges style HIMS avec images PNG transparentes flottantes + ombre elliptique.
Voir section Quiz ci-dessous pour details.

### Sections dans l'ordre
1. Hero unifie (accroche + photo + chiffres cles + index des 6 services)
2. Marquee banner (services defilants)
3. Badges quiz (4 categories)
4. Dernier article blog (auto-fetch depuis blog.html)
5. Marque a decouvrir (rotation aleatoire)
6. Stats bar (40+ ans, 4.9 Google, 6j/7, 100% conseil)

### Ordre Services

Ordre de lecture de `.hero-services-grid` (3 colonnes desktop, 2 rangees) :

1. Delivrance d'ordonnances
2. Parapharmacie
3. Vaccinations
4. Produits naturels
5. Materiel medical
6. **Livraison a domicile** (toujours en dernier)

---

## Quiz

**Hub :** `Quizzes/guide-quizzes-sante-pharmacie-queven.html` — page d'accueil des quiz. Design (juillet 2026) : bannière hero plein largeur + **cartes illustrées style HIMS** (photo produit flottante par catégorie sur fond pastel : vert naturels / mint dermo / ambre compléments / lavande automédication). Conteneur 1200px, sections centrées. Base 16px (alignée sur le reste du site).

**Design (HIMS-inspired):**
- Fonts: Fraunces (display) + DM Sans (body)
- Boutons: fond teal-pro, radius 8px
- Variables CSS pastels + spacing 8pt

**Disponibles:** quiz-soin-peau.html ✅, quiz-automedication.html ✅, quiz-produits-naturels.html ✅, quiz-complement.html ✅

**Inventaire photos produit :** `docs/INVENTAIRE-PRODUITS-QUIZZ.md` — liste de travail pour photographier chaque produit recommandé (PNG transparent, style badges homepage). Guide de construction des quiz : `Quizzes/README.md`.

### Badges Quiz (Style HIMS)

Les 4 badges homepage utilisent des images PNG transparentes (RGBA) avec ombre elliptique au sol.
Guide complet : `Guide Badge produit style HIMS.md`

| Badge | Image | Fichier |
|---|---|---|
| Produits naturels | Feuilles eucalyptus/menthe | `images/naturels-product.png` |
| Dermocosmetique | Pot de creme jaune | `images/dermocosmetique-product.png` |
| Complements alimentaires | Capsules rouges | `images/complements-product.png` |
| Automedication | Pilules jaunes | `images/automedication-product.png` |

**CSS cle :**
- `.product-feature-img-wrap::after` : ombre elliptique (`radial-gradient`)
- `.product-feature-visual` : `margin-top: -24px`
- Image : 140px mobile / 220px desktop, `scale(1.05)` au hover
- Fond : `var(--beige)` par defaut, couleur au hover par categorie

**Creation d'image :** `rembg[cpu]` pour supprimer le fond → verifier mode RGBA

---

## Checklist Nouvelle Page (OBLIGATOIRE)

Quand Claude cree une nouvelle page HTML :

**1. Head — SEO meta :**
- [ ] `<link rel="canonical" href="https://www.pharmaciecharnal.com/[path]">`
- [ ] `<meta name="robots" content="index, follow">` (ou `noindex` pour placeholders)
- [ ] `<meta property="og:url" content="https://www.pharmaciecharnal.com/[path]">`
- [ ] `<meta property="og:image" content="https://www.pharmaciecharnal.com/images/pharmacie-charnal-logo.png">`
- [ ] Toutes les URLs en `https://www.pharmaciecharnal.com` (JAMAIS .fr)

**2. Head — Schema JSON-LD :**
- [ ] BreadcrumbList en JSON-LD avec URLs absolues (PAS de Microdata)
- [ ] Si la page concerne la pharmacie : reference `{"@id": "https://www.pharmaciecharnal.com/#pharmacy"}` — NE PAS dupliquer le schema Pharmacy complet
- [ ] Le schema Pharmacy complet n'existe QUE sur `index.html`

**3. Fichiers a mettre a jour :**
- [ ] `sitemap.xml` — ajouter la nouvelle URL avec `<lastmod>`
- [ ] `llms.txt` — ajouter si c'est une page importante

**4. Contenu :**
- [ ] Google Analytics (G-2Q64V6B0QE) dans `<head>`
- [ ] Images avec attribut `alt`
- [ ] Liens internes relatifs
- [ ] Mobile menu present
- [ ] Marques verifiees (pas d'invention)
- [ ] CTAs → venir en pharmacie
- [ ] Footer complet avec mentions legales
- [ ] Accents francais corrects

**5. Performance — articles blog uniquement :**
- [ ] Hero image : `<img loading="eager" fetchpriority="high">` — PAS de `<link rel="preload" as="image">` (redondant quand `fetchpriority="high"` est sur l'`<img>`)
- [ ] `<script src="../animations.js" defer></script>` — JAMAIS sans `defer`

---

## Architecture Schema (IMPORTANT)

**Principe: schema Pharmacy unique sur la homepage, references @id partout ailleurs.**

```
index.html (homepage)
├── Pharmacy schema complet (@id: #pharmacy)
│   └── Contient : address, telephone, openingHours, aggregateRating (4.9),
│       sameAs, geo, areaServed, reviews, foundingDate, medicalSpecialty
├── WebSite schema (@id: #website, publisher → #pharmacy)
└── BreadcrumbList JSON-LD (si applicable)

Autres pages
├── Schema specifique a la page (WebPage, ContactPage, Blog, etc.)
│   └── Reference : {"@id": "https://www.pharmaciecharnal.com/#pharmacy"}
└── BreadcrumbList JSON-LD avec URLs absolues
```

**Interdit :** Copier-coller le schema Pharmacy (address, openingHours, reviews) sur d'autres pages.
**aggregateRating :** Toujours `"4.9"`, valeur unique, definie uniquement sur la homepage.

---

## Pages Marques (Nos-marques/)

### Structure `<head>` obligatoire

Chaque page marque doit contenir dans cet ordre:
1. Google Analytics (`G-2Q64V6B0QE`)
2. `<meta charset>` + `<meta viewport>`
3. Favicons (5 liens: ico, png 32, png 16, png 192, apple-touch-icon) avec `../favicon/`
4. `<title>`: `NomMarque : Slogan | Pharmacie Charnal`
5. `<meta name="description">`: unique par marque, mentionner Queven
6. `<link rel="canonical">`: `https://www.pharmaciecharnal.com/Nos-marques/nom-page.html`
7. OG tags (type, url, title, description, image, locale)
8. Google Fonts, **pattern async obligatoire** (voir section Performance Mobile), JAMAIS `rel="stylesheet"` synchrone
10. `<style>` inline avec variables CSS de la marque

### Hero Photo — Workflow d'intégration (standard 2026-05-12)

1. **Optimiser** : `./scripts/optimize-hero.sh ~/Downloads/photo.png {slug}` → sauve dans `logos/{BrandName}-hero.jpg`
2. **CSS hero** (remplace le gradient) :
```css
/* Supprimer background: url(...) du .hero */
.hero-img {
    position: absolute; inset: 0; width: 100%; height: 100%;
    object-fit: cover; object-position: center; z-index: 0;
}
@media (max-width: 1023px) { .hero-img { object-position: 65% center; } }
/* Ajuster % selon la position du sujet dans la photo */

.hero::before { ...; z-index: 1; } /* overlay au-dessus de l'img */
.hero-bubbles, .bubble { display: none; }
.hero-visual { display: none !important; }
@media (min-width: 1024px) { .hero-content { grid-template-columns: minmax(0, 620px); } }
@media (max-width: 1023px) {
    .hero::before { background: linear-gradient(180deg, rgba(252,245,240,0.86) 0%, rgba(252,245,240,0.56) 50%, rgba(252,245,240,0.46) 100%); }
}
```
3. **HTML** — premier enfant de `<section class="hero">` :
```html
<img src="logos/{BrandName}-hero.jpg" alt="" class="hero-img"
     fetchpriority="high" loading="eager" decoding="async" aria-hidden="true">
```
4. **h1 couleurs** : `color: var(--charcoal)` + span `color: var(--teal-dark)`
5. **Pas de `<link rel="preload" as="image">`** — le `fetchpriority="high"` sur l'`<img>` est suffisant
6. **Commit** : `git add {slug}-page.html logos/{BrandName}-hero.jpg && git commit -m "feat({slug}): add hero photo background"`

### Template

`Nos-marques/TEMPLATE-marque.html` — Copier et remplir les `{{PLACEHOLDERS}}`.
**IMPORTANT:** Le template doit etre maintenu en sync avec cette checklist.

### Polices marques

Les pages marques utilisent **Cormorant Garamond** (display) + **DM Sans** (body), pas Fraunces.

---

## Commandes Rapides

```bash
# Test local
python3 -m http.server 8000

# Deployer (branche unique: main)
git add [fichiers] && git commit -m "Message" && git push origin main
```

---

## Ressources

- **Leaflet.js:** https://leafletjs.com/reference.html
- **GitHub Pages:** https://docs.github.com/pages
- **Parent instructions:** `/Pharma/CLAUDE-Pharma.md`

---

*Derniere mise a jour: 23 juillet 2026*
