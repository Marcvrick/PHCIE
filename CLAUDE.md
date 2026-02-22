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
git add [fichiers] && git commit -m "Message" && git push origin main
```

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
annuaire-sante.html, planning.html
```

**Blog:** `blog/*.html` (8 articles)
**Marques:** `Nos-marques/*.html` (16 pages + nosmarques.html index + TEMPLATE-marque.html)
**Quiz:** `Quizzes/*.html` (quiz-automedication, quiz-soin-peau, quiz-produits-naturels, quiz-coming-soon, guide-quizzes-sante)
**Assets:** `images/`, `style.css`, `style-v2.css`, `animations.js`
**Guides:** `Guide Badge produit style HIMS.md`

---

## Règles de Contenu Web

### Marques Approuvées

**RÈGLE:** Seules les marques réellement vendues peuvent être mentionnées.

**Cosmétiques:** Bioderma, La Roche-Posay, Avène, Nuxe, La Rosée, Mustela, Klorane
**Compléments:** PiLeJe, Arkopharma, Boiron, Aragan, Nat&Form, Bion 3, Biogaran

**❌ Ne JAMAIS inventer de marques**

### CTAs (Calls-to-Action)

**✅ Autorisé:** "Passez nous voir", "Venez en pharmacie", "N'hésitez pas à venir"
**❌ Interdit:** "Contactez-nous", "Appelez-nous", "Prenez rendez-vous"

### Ton de Voix Blog (Voix de Laure — OBLIGATOIRE)

**Chaque article de blog doit être écrit dans la voix de Laure.** Référence: article "Moral en berne".

- **"Je" pour l'expertise personnelle:** "L'alternative que je privilégie", "Je vérifie toujours..."
- **"Nous" pour l'équipe/la pharmacie:** "Passez nous voir", "Chez nous", "Nous prendrons le temps"
- **Conversationnel:** Parle comme au comptoir, pas comme une encyclopédie médicale
- **Franche et empathique:** "Parlons franchement", "vous n'êtes pas seul(e)"
- **Ancrée localement:** Météo bretonne, vie à Quéven, références concrètes
- **Vulgarisatrice:** Images parlantes ("la boule au ventre"), mécanismes expliqués simplement

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

- `style-v2.css`: Pages principales (index, services, histoire, contact, pharmacie-de-garde, recrutement, annuaire-sante, nosmarques index)
- `style.css`: Blog, mentions-legales, donnees-personnelles
- **Pages marques (Nos-marques/*-page.html):** CSS inline (pas de stylesheet externe). Chaque page contient ~3400 lignes de `<style>` avec variables CSS propres + couleurs de la marque.

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

### Hero Section
- Titre : "Votre sante, notre priorite"
- Description + **CTA bouton outline** (`btn-secondary`) : "Quel medicament pour vos symptomes?" → `Quizzes/quiz-automedication.html`
- Le CTA utilise `.hero-cta` (animation fadeInUp 0.3s)

### Badges Quiz (sous le marquee)
4 badges style HIMS avec images PNG transparentes flottantes + ombre elliptique.
Voir section Quiz ci-dessous pour details.

### Sections dans l'ordre
1. Hero + CTA
2. Marquee banner (services defilants)
3. Badges quiz (4 categories)
4. Services (6 cartes)
5. Dernier article blog (auto-fetch depuis blog.html)
6. Marque a decouvrir (rotation aleatoire)
7. Stats bar (40+ ans, 4.9 Google, 6j/7, 100% conseil)

### Ordre Services

1. Delivrance d'ordonnances
2. Parapharmacie
3. Vaccinations
4. Produits naturels
5. Materiel medical
6. **Livraison a domicile** (toujours en dernier)

---

## Quiz

**Design (HIMS-inspired):**
- Fonts: Fraunces (display) + DM Sans (body)
- Boutons: fond teal-pro, radius 8px
- Variables CSS pastels + spacing 8pt

**Disponibles:** quiz-soin-peau.html ✅, quiz-automedication.html ✅, quiz-produits-naturels.html ✅
**En préparation:** Compléments alimentaires

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

---

## Architecture Schema (IMPORTANT)

**Principe : schema Pharmacy unique sur la homepage, references @id partout ailleurs.**

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
**aggregateRating :** Toujours `"4.9"` — valeur unique, definie uniquement sur la homepage.

---

## Pages Marques (Nos-marques/)

### Structure `<head>` obligatoire

Chaque page marque doit contenir dans cet ordre :
1. Google Analytics (`G-2Q64V6B0QE`)
2. `<meta charset>` + `<meta viewport>`
3. Favicons (5 liens : ico, png 32, png 16, png 192, apple-touch-icon) avec `../favicon/`
4. `<title>` : `NomMarque : Slogan | Pharmacie Charnal`
5. `<meta name="description">` : unique par marque, mentionner Queven
6. `<link rel="canonical">` : `https://www.pharmaciecharnal.com/Nos-marques/nom-page.html`
7. OG tags (type, url, title, description, image, locale)
8. Google Fonts (Cormorant Garamond + DM Sans)
9. `<style>` inline avec variables CSS de la marque

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

*Derniere mise a jour: 12 Fevrier 2026*
