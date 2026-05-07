# Site Web - Pharmacie Charnal

Site internet statique pour la Pharmacie Charnal à Quéven (56530).
Déployé sur GitHub Pages : **www.pharmaciecharnal.com**

---

## 📁 Structure du site

```
website-pharmacie-charnal/
├── index.html              # Accueil
├── histoire.html           # Notre Histoire
├── services.html           # Services
├── blog.html               # Au Comptoir (liste des articles)
├── contact.html            # Contact
├── recrutement-preparatrice-pharmacie-queven.html  # Offre d'emploi préparatrice
├── pharmacie-de-garde-queven-hennebont-lorient.html  # Page pharmacie de garde
├── mentions-legales.html   # Mentions légales
├── donnees-personnelles.html  # Données personnelles
├── style.css               # Styles legacy (anciennes pages)
├── style-v2.css            # Design System HIMS v2 (nouvelles pages)
├── animations.js           # Animations scroll
├── favicon.svg             # Favicon
├── robots.txt              # Directives crawlers
├── sitemap.xml             # Plan du site
├── feed.json               # JSON Feed pour AI Search
├── CNAME                   # Custom domain (www.pharmaciecharnal.com)
├── professionnels-sante-queven-carte.csv  # Données carte Leaflet
├── Nos-marques/            # Section marques
│   ├── nosmarques.html     # Page catalogue marques (ancres: #cosmetiques, #complements, #premiers-soins)
│   ├── biogaran-page.html  # Page dédiée Biogaran (+ 15 autres pages marques)
│   ├── TEMPLATE-marque.html # Template pour nouvelles pages marques
│   ├── logos/              # Logos des marques (Avene, Bioderma, Biogaran, etc.)
│   └── *.md                # Articles marques (briefs pour futures pages)
├── Quizzes/                # Quiz interactifs santé
│   ├── guide-quizzes-sante-pharmacie-queven.html  # Page guide SEO (hub)
│   ├── quiz-automedication.html      # Quiz automédication ✅
│   ├── quiz-soin-peau.html           # Quiz soin de la peau ✅
│   ├── quiz-produits-naturels.html   # Quiz produits naturels ✅
│   └── quiz-coming-soon.html         # Placeholder (compléments alimentaires)
├── planning/               # Redirection vers l'app planning RH (repo PLPH séparé)
│   └── index.html          # Meta-refresh → https://marcvrick.github.io/PLPH/
├── blog/                   # Articles de blog (8 articles)
│   ├── GUIDE-REDACTION-BLOG.md            # Guide rédactionnel Laure
│   ├── PLANNING-BLOG-PHARMACIE.md         # Planning éditorial
│   ├── SEO blog strategy.md               # Stratégie SEO blog
│   ├── detox-apres-fetes-mythe-realite-queven.html
│   ├── gastro-enterite-prevention-bons-reflexes-queven.html
│   ├── humidite-douleurs-articulaires-queven.html
│   ├── prevenir-maux-hiver-queven.html
│   ├── professionnels-sante-queven-2026.html  # Carte Leaflet interactive
│   ├── vaccination-adulte-guide-pratique.html
│   ├── Moral en berne/fatigue-moral-fin-hiver-queven.html
│   └── Peau Seche/proteger-peau-seche-hiver-breton-queven.html
├── fonts/                  # Fonts auto-hébergées (RGPD) - À TÉLÉCHARGER
└── images/                 # Logo et ressources visuelles
```

---

## 🎨 Design & Identité Visuelle

### ⚠️ Migration en cours vers style-v2.css (HIMS-inspired)

Le site migre progressivement d'un design "Wellness Minimal" vers un nouveau design system inspiré de HIMS avec des pastels doux et une typographie plus moderne.

**Pages migrées vers style-v2.css :**
- ✅ `Nos-marques/nosmarques.html` (+ réduction 80% du contenu)
- ✅ `annuaire-sante.html`
- ✅ `pharmacie-de-garde-queven-hennebont-lorient.html`
- ✅ `services.html`
- ✅ `histoire.html`
- ✅ `contact.html`
- ✅ `blog.html`
- ✅ `recrutement-preparatrice-pharmacie-queven.html`

**Pages encore sur style.css (à migrer) :**
- ⏳ `index.html`
- ⏳ `mentions-legales.html`
- ⏳ `donnees-personnelles.html`
- ⏳ `index-ordonnance.html`

**Pages marques (`Nos-marques/*-page.html`)** : Utilisent style.css avec overrides inline

---

### Palette de Couleurs - style-v2.css (HIMS)

```css
:root {
    /* Couleurs principales */
    --teal-pro: #2D5F5D;       /* Couleur primaire */
    --sage-natural: #7C9885;   /* Vert naturel */
    --sage-light: #9DB3A4;
    --sage-dark: #5F7A68;

    /* Pastels HIMS */
    --pastel-sage: #E8F0EA;
    --pastel-mint: #DFF5ED;
    --pastel-teal: #D4E8E7;
    --pastel-peach: #FBE8DC;
    --pastel-lavender: #EDE8F5;

    /* Neutres */
    --cream: #F5F1E8;
    --cream-warm: #FAF7F2;
    --beige: #D9C9B0;
    --beige-dark: #C4B49A;
    --white: #FFFFFF;
    --charcoal: #1F2121;       /* Footer sombre */
    --gray-600: #6B7280;       /* Texte secondaire */

    /* Accent Blog "Au Comptoir" */
    --accent: #b4a6d7;         /* Lavande */
}
```

### Palette Legacy - style.css

```css
:root {
    --sage: #7C9885;
    --teal: #2D5F5D;
    --cream: #F5F1E8;
    --gray: #6B7280;
    /* ... voir style.css pour la liste complète */
}
```

### Mapping Variables (migration)

| style.css (old) | style-v2.css (new) |
|-----------------|-------------------|
| `--teal` | `--teal-pro` |
| `--sage` | `--sage-natural` |
| `--gray` | `--gray-600` |
| `--gradient` | `linear-gradient(135deg, var(--teal-pro) 0%, var(--sage-natural) 100%)` |
| `--space-xs` | `--space-8` |
| `--space-sm` | `--space-12` |
| `--space-md` | `--space-16` |
| `--space-lg` | `--space-24` |
| `--space-xl` | `--space-32` |
| `--space-2xl` | `--space-48` |
| `--space-3xl` | `--space-80` |

---

### Typographie

**style-v2.css (Google Fonts) :**
- **Display**: Fraunces (serif élégant)
- **Body**: DM Sans (sans-serif lisible)

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
```

**style.css (fallback système) :**
- **Headings**: Georgia, "Crimson Pro", serif
- **Body**: -apple-system, "DM Sans", sans-serif
- **Taille de base**: 18px (accessibilité seniors)

### Navigation & UX

**Dropdown Services (toutes pages) :**
1. Notre Histoire
2. Nos Marques
3. Pharmacie de garde
4. Annuaire Santé
5. **Quiz santé** ← Lien vers page guide quiz

**Ordre des Services (Homepage):**
1. Délivrance d'ordonnances
2. **Parapharmacie**
3. Vaccinations
4. Produits naturels
5. Matériel médical
6. **Livraison à domicile** (toujours en dernier)

**Bouton "Au Comptoir":**
- Couleur distinctive: `#b4a6d7` (lavande)
- Se distingue du reste de la navigation

**Navbar style-v2.css :**
- Pas de soulignement au hover des liens
- Dropdown avec "invisible bridge" (pas de gap entre le toggle et le menu)

### Pages de Marques - Personnalisation des Couleurs

Chaque page de marque (`Nos-marques/*-page.html`) peut avoir sa propre palette de couleurs basée sur l'identité visuelle de la marque. **Le header et le footer restent identiques sur toutes les pages** pour maintenir la cohérence du site Pharmacie Charnal.

**Éléments personnalisables par marque :**
- Fond de page (hero, sections)
- Couleurs des titres et accents
- Dégradés des cartes produits
- Bulles et effets visuels
- Ombres (teinte)

**Éléments fixes (ne pas modifier) :**
- Header/Navigation (couleurs Charnal)
- Footer (gradient `#2D5F5D` → `#5A7563`)
- Structure des sections

**Palette des marques :**

| Marque | Couleur principale | Couleur sombre | Pastels |
|--------|-------------------|----------------|---------|
| **Biogaran** | `#0066CC` (bleu) | `#004C99` | `#E3F2FD`, `#E8F4FC`, `#F0F7FF` |

**Pour ajouter une nouvelle marque :**
1. Copier le template `TEMPLATE-marque.html`
2. Remplacer les variables CSS `:root` avec les couleurs de la marque
3. Adapter les dégradés du hero et des sections
4. Conserver le header et footer d'origine
5. Ajouter le logo dans `logos/`

**Ressources couleurs :** Consulter `/Users/mc/Documents/MarcOS/Pharma/GESTION/1-RESSOURCES/Fiche par Marque/` pour les informations sur les marques.

### Footer

**Design unifié sur toutes les pages** - Copyright à gauche, liens légaux à droite.

```
┌─────────────────────────────────────────────────────────────────┐
│ © 2026 Pharmacie Charnal. Tous droits réservés.    Mentions légales    Politique de confidentialité │
└─────────────────────────────────────────────────────────────────┘
```

**Structure HTML:**
```html
<div class="footer-bottom">
    <p class="footer-copyright">&copy; 2026 Pharmacie Charnal. Tous droits réservés.</p>
    <div class="footer-legal">
        <a href="mentions-legales.html">Mentions légales</a>
        <a href="donnees-personnelles.html">Politique de confidentialité</a>
    </div>
</div>
```

**CSS (style.css):**
```css
.footer-bottom {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-md);
    padding-top: var(--space-xl);
    border-top: 1px solid rgba(255, 255, 255, 0.15);
}

.footer-copyright {
    color: var(--white);
    opacity: 0.7;
    font-size: var(--text-sm);
}

.footer-legal {
    display: flex;
    gap: var(--space-lg);
}
```

**Note pour sous-dossiers (Nos-marques/, blog/):** Utiliser `../mentions-legales.html` et `../donnees-personnelles.html` pour les chemins relatifs.

---

## ⏰ Informations Pharmacie

**Adresse**: 32 Place de Toulouse, 56530 Quéven
**Téléphone**: 02 97 05 09 31
**Email**: *(non public sur le site)*

**Horaires**:
- Lundi-Vendredi: 9h-12h30 / 14h-19h15
- Samedi: 9h-12h30
- Dimanche: Fermé

**Réseaux sociaux**:
- Instagram: https://www.instagram.com/pharmaciecharnalqueven/
- Facebook: https://www.facebook.com/pharmaciecharnal/

---

## 🌐 Déploiement Vercel (Clean URLs)

### Configuration `vercel.json`

Le fichier `vercel.json` à la racine active les URLs propres (sans `.html`) sur Vercel.

**Ce que ça change :**

| Avant (GitHub Pages) | Après (Vercel) |
|----------------------|----------------|
| `/histoire.html` | `/histoire` |
| `/services.html` | `/services` |
| `/blog/detox-apres-fetes-mythe-realite-queven.html` | `/blog/detox-apres-fetes-mythe-realite-queven` |
| `/Nos-marques/biogaran-page.html` | `/Nos-marques/biogaran-page` |
| `/Quizzes/quiz-automedication.html` | `/Quizzes/quiz-automedication` |

**Options actives :**
- `cleanUrls: true` — sert les `.html` sans extension
- `trailingSlash: false` — pas de slash final (`/histoire` pas `/histoire/`)

**Cas spéciaux — articles dans des sous-dossiers avec espaces :**

Les deux articles stockés dans des sous-dossiers (`Moral en berne/`, `Peau Seche/`) sont aplatis via rewrites + redirects :

| URL encodée (moche) | URL servie (propre) |
|---------------------|---------------------|
| `/blog/Moral%20en%20berne/fatigue-...` | `/blog/fatigue-moral-fin-hiver-queven` |
| `/blog/Peau%20Seche/proteger-...` | `/blog/proteger-peau-seche-hiver-breton-queven` |

Le redirect (301) assure que les anciennes URLs redirigent vers les propres ; le rewrite sert le bon fichier .html.

### Déployer sur Vercel

```bash
# Installer CLI Vercel (une fois)
npm i -g vercel

# Déployer (depuis la racine du projet)
vercel --prod
```

Ou connecter le repo GitHub sur [vercel.com](https://vercel.com) → déploiement automatique à chaque push `main`.

**Note domaine :** Pointer `www.pharmaciecharnal.com` vers Vercel dans le DNS (supprimer le CNAME GitHub Pages actuel, ajouter le CNAME Vercel fourni dans le dashboard).

---

## 🌐 Déploiement GitHub Pages

### Configuration actuelle

- **Repository**: `https://github.com/Marcvrick/Pharmacie-Charnal`
- **Branche unique**: `main` (travail + déploiement automatique)
- **Custom Domain**: `www.pharmaciecharnal.com` (fichier CNAME)
- **GitHub Pages**: Activé sur branche `main`

### Workflow Git

```bash
# Workflow simplifié - une seule branche
git add [fichiers]
git commit -m "Message descriptif"
git push origin main
```

**Note**: Le site se déploie automatiquement à chaque push sur `main`.

---

## 🔒 Conformité RGPD

### État actuel: ~85% conforme

| Élément | Transfert données | Conformité |
|---------|-------------------|------------|
| **Fonts (Google Fonts)** | ✅ Commentées (fallback système) | ✅ Conforme |
| **Google Maps** | ⚠️ Google US | ⚠️ Notice RGPD présente |
| **Liens sociaux** | ✅ Pas de transfert | ✅ Conforme |
| **Analytics** | ✅ Aucun | ✅ Conforme |
| **Cookies** | ✅ Aucun | ✅ Conforme |

**Point d'attention**: Google Maps (page contact) est le seul service externe. Une notice RGPD claire est affichée.

**Fonts auto-hébergées**: Prévues mais pas encore téléchargées. Le site utilise actuellement les polices système (Georgia, San Francisco, Segoe UI).

---

## 🔍 Optimisation SEO & AI Search

### SEO Classique

✅ **Toutes les pages** disposent de:
- Meta descriptions optimisées (150-160 caractères) avec "proche Lorient" sur pages stratégiques
- Schema.org markup (Pharmacy, Blog, FAQPage, ItemList)
- FAQ Schema sur `services.html` (5 Q&A) et `pharmacie-de-garde` (7 Q&A)
- Open Graph (Facebook) et Twitter Cards
- URLs canoniques
- Structure H1 → H2 → H3 propre

### AI Search Optimization (AEO)

✅ **Articles de blog** optimisés pour ChatGPT, Perplexity, Claude:
- Schema.org MedicalWebPage complet
- FAQ Schema intégré (3-5 Q&A par article)
- Citation meta tags (académique)
- JSON Feed (`feed.json`)
- H2/H3 formulés en questions naturelles
- Hyper-localisation (Quéven, Bretagne, climat océanique)

**Crawlers AI autorisés** dans `robots.txt`:
- GPTBot (OpenAI)
- PerplexityBot
- Claude-Web
- Google-Extended (Gemini)

**Voir** `/blog/GUIDE-REDACTION-BLOG.md` pour les règles d'optimisation complètes.

---

## 📝 Articles de Blog Publiés

**17 articles en ligne + 2 en préparation** — publication hebdomadaire, chaque lundi. Voir [`blog/`](blog/) pour les sources `.md` organisées en dossiers numérotés (alignés sur les posts GMB). Mapping article → page marque dans [`blog/BRAND-BLOG-MAPPING.md`](blog/BRAND-BLOG-MAPPING.md).

| # | Date | Article | Source |
|---|------|---------|--------|
| 17 | 5 mai 2026 | Stress des examens : comment aider les ados | [`17-stress-examens-ados/`](blog/17-stress-examens-ados/) |
| 16 | 28 avr 2026 | Courbatures et reprise du sport au printemps | [`16-courbatures-reprise-sport/`](blog/16-courbatures-reprise-sport/) |
| 15 | 21 avr 2026 | Jambes lourdes : comprendre et soulager | [`15-jambes-lourdes/`](blog/15-jambes-lourdes/) |
| 14 | 14 avr 2026 | Paracétamol, ibuprofène, aspirine : lequel choisir ? | [`14-paracetamol-ibuprofene-aspirine/`](blog/14-paracetamol-ibuprofene-aspirine/) |
| 13 | 8 avr 2026 | Compléments alimentaires : pharmacie ou internet ? | [`13-complements-alimentaires/`](blog/13-complements-alimentaires/) |
| 12 | 31 mars 2026 | Troubles du sommeil : solutions naturelles | [`12-troubles-sommeil/`](blog/12-troubles-sommeil/) |
| 11 | 24 mars 2026 | Premiers soleils : protéger sa peau dès le printemps | [`11-protection-solaire/`](blog/11-protection-solaire/) |
| 10 | 16 mars 2026 | Allergie au pollen en Bretagne | [`10-allergie-pollen/`](blog/10-allergie-pollen/) |
| 09 | 10 mars 2026 | Mars Bleu : dépistage cancer colorectal | [`09-mars-bleu/`](blog/09-mars-bleu/) |
| 07 | 3 mars 2026 | Gastro-entérite : prévention et bons réflexes | [`07-gastro-enterite/`](blog/07-gastro-enterite/) |
| 08 | 22 fév 2026 | Crampes abdominales : comprendre et soulager | `crampes-abdominales-comprendre-soulager-queven.html` |
| 06 | 16 fév 2026 | Fatigue et moral en fin d'hiver | [`06-fatigue-moral-fin-hiver/`](blog/06-fatigue-moral-fin-hiver/) |
| 05 | hiver 2026 | Humidité et douleurs articulaires | [`05-humidite-douleurs-articulaires/`](blog/05-humidite-douleurs-articulaires/) |
| 04 | 12 jan 2026 | Détox après les fêtes : mythe ou réalité ? | [`04-detox-apres-fetes/`](blog/04-detox-apres-fetes/) |
| 03 | déc 2025 | Guide santé Quéven (carte Leaflet) | `professionnels-sante-queven-2026.html` |
| 02 | déc 2025 | Vaccination adulte : guide pratique | `vaccination-adulte-guide-pratique.html` |
| 01 | 31 déc 2025 | Prévenir les maux de l'hiver à Quéven | [`01-prevenir-maux-hiver/`](blog/01-prevenir-maux-hiver/) |

**Articles rédigés en attente de publication :**

| # | Date cible | Article | Marque ciblée | Source |
|---|------------|---------|---------------|--------|
| 18 | **Lundi 11 mai 2026** | Quel shampoing pharmacie choisir? Klorane, Nuxe, Bioderma, Avène | Klorane + Nuxe | [`18-shampoings-pharmacie/`](blog/18-shampoings-pharmacie/) |
| 19 | **Lundi 18 mai 2026** | Chien et chat : les essentiels santé en pharmacie pour le printemps | Biocanina | [`19-chiens-chats-pharmacie/`](blog/19-chiens-chats-pharmacie/) |
| 25 | Début juillet 2026 | Tiques en Bretagne : prévention et réaction | — | [`25-tiques-bretagne/`](blog/25-tiques-bretagne/) |

**Stratégie éditoriale** :
- Ton : Voix de Laure (pharmacienne pédagogue, professionnelle accessible) — voir [`blog/README.md`](blog/README.md) pour le guide complet
- SEO local : Quéven, Bretagne, Morbihan, climat océanique
- E-E-A-T médical : expertise + sources (HAS, ANSM, VIDAL, EMA, Cochrane) + mécanismes biologiques
- Optimisé pour AI Search (FAQ Schema.org, H2 en questions, paragraphes answer-first 40-60 mots)
- Pipeline blog + GMB multi-canal : skill [`pharmacie-charnal-blog`](../../../Claude-skills/pharmacie-charnal-blog/) (article + 6 sections GMB/Instagram/Facebook/LinkedIn/Photo/Timing)

---

## 🔧 Fonctionnalités Techniques

### Mobile Menu
- Hamburger icon 3 lignes
- JavaScript toggle
- Présent sur toutes les pages
- ARIA attributes (accessibilité)

### Responsive Mobile (max-width: 767px)

**Réduction globale de ~40% des éléments sur mobile pour une meilleure lisibilité.**

| Élément | Desktop | Mobile | Réduction |
|---------|---------|--------|-----------|
| `.section-title` | `var(--text-3xl)` | `calc(var(--text-3xl) * 0.75)` | 25% |
| `.section-badge` | `var(--text-sm)` | `calc(var(--text-sm) * 0.85)` | 15% |
| `.section-header` margin | `var(--space-3xl)` | `calc(var(--space-3xl) * 0.6)` | 40% |
| `.service-card` padding | `var(--space-xl)` | `calc(var(--space-xl) * 0.6)` | 40% |
| `.service-icon` | `64px` | `~38px` | 40% |
| `.why-card` padding | `var(--space-xl)` | `calc(var(--space-xl) * 0.6)` | 40% |
| `.why-number` | `var(--text-3xl)` | `calc(var(--text-3xl) * 0.6)` | 40% |
| `.contact-card` padding | `var(--space-xl)` | `calc(var(--space-xl) * 0.6)` | 40% |
| `.contact-icon` | `64px` | `~38px` | 40% |
| `.timeline-card` padding | `var(--space-xl)` | `calc(var(--space-xl) * 0.6)` | 40% |
| `.timeline-year` | `var(--text-3xl)` | `calc(var(--text-3xl) * 0.6)` | 40% |
| `.pharmacist-image` height | `480px` | `240px` | 50% |
| `.banner-grid` (produits) | 6 colonnes | 3 colonnes | 2 rangées |
| `.hero` padding | `var(--space-3xl)` | `calc(var(--space-3xl) * 0.5)` | 50% |
| `.hero-image` | Visible | `display: none` | Masquée |
| `.services` padding | `var(--space-3xl)` | `calc(var(--space-3xl) * 0.5)` | 50% |
| `.services-grid` margin | `var(--space-2xl)` | `var(--space-md)` | Réduit |
| `.why-us` padding | `var(--space-3xl)` | `calc(var(--space-3xl) * 0.5)` | 50% |

**Classes CSS utilisées (toutes les pages):**
- `.hero`, `.hero-image` - Section hero (image masquée sur mobile)
- `.section-header`, `.section-badge`, `.section-title` - Titres de section
- `.services`, `.services-grid` - Section services
- `.service-card`, `.service-icon` - Cartes services (homepage)
- `.why-us`, `.why-card`, `.why-number` - Section "Pourquoi nous choisir"
- `.contact-card`, `.contact-icon` - Page contact
- `.timeline-card`, `.timeline-year` - Timeline (page histoire)
- `.pharmacist-grid`, `.pharmacist-image` - Section Laure Charnal
- `.banner-grid`, `.banner-item` - Grille catégories produits

**Note:** Les règles utilisent `!important` pour surcharger les styles inline (notamment `.service-icon` sur la page services.html qui a des styles inline `80px`).

#### Page Recrutement (styles internes)

La page `recrutement-preparatrice-pharmacie-queven.html` a ses propres règles mobile dans un `<style>` interne :

| Élément | Desktop | Mobile | Réduction |
|---------|---------|--------|-----------|
| `.job-title` | `var(--text-4xl)` | `calc(var(--text-3xl) * 0.75)` | ~25% |
| `.job-subtitle` | `var(--text-xl)` | `calc(var(--text-xl) * 0.85)` | 15% |
| `.job-meta-item` | `var(--text-base)` | `calc(var(--text-base) * 0.9)` | 10% |
| `.job-section-title` | `var(--text-2xl)` | `calc(var(--text-2xl) * 0.75)` | 25% |
| `.benefit-icon` | `48px` | `calc(48px * 0.7)` | 30% |
| `.benefits-grid` | auto-fit | `1fr` (1 colonne) | Simplifié |
| `.job-cta h2` | `var(--text-3xl)` | `calc(var(--text-3xl) * 0.75)` | 25% |

### Page Pharmacie de Garde

**Fichier**: `pharmacie-de-garde-queven-hennebont-lorient.html`

**État actuel**: Affiche uniquement le numéro **3237** pour trouver la pharmacie de garde.

**Fonctionnalité masquée (prête à être activée)**:
- Carte affichant la pharmacie de garde du jour
- Données des gardes de février à juin 2026 intégrées dans le JavaScript
- Logique pour afficher garde de jour/nuit selon l'heure

**Pour réactiver la carte pharmacie du jour**:

1. Dans le HTML, remettre la section "Today's Guard" :
```html
<section class="today-guard-section">
    <div class="container">
        <div class="today-guard-card" id="todayGuardCard">
            <div class="today-guard-date" id="todayDate">Chargement...</div>
            <div class="today-guard-pharmacie" id="todayPharmacie">-</div>
            <div class="today-guard-ville" id="todayVille">-</div>
        </div>
    </div>
</section>
```

2. Le JavaScript `renderTodayGuard()` est déjà présent et fonctionnel.

3. Mettre à jour les données `gardesData` avec les nouveaux mois si nécessaire.

---

### Carte Interactive Leaflet.js
**Fichier**: `blog/professionnels-sante-queven-2026.html`

- Leaflet v1.9.4 (CDN sans integrity hash)
- PapaParse v5.4.1 pour CSV
- Données: `professionnels-sante-queven-carte.csv` (15 professionnels)
- Markers: Pharmacie Charnal rouge, autres professionnels bleus

### Animations (animations.js)
- Fade-in au scroll (IntersectionObserver)
- Parallax léger sur hero sections
- Smooth scroll pour ancres
- Stats counter animation

---

## 📋 Checklist Maintenance

### Avant chaque déploiement (main)

- [ ] Toutes les images ont un attribut `alt`
- [ ] Tous les liens internes fonctionnent
- [ ] Mobile menu présent et fonctionnel
- [ ] Informations contact à jour (adresse, tél, horaires)
- [ ] CTAs invitent à venir en pharmacie (pas "contactez-nous")
- [ ] Marques mentionnées sont vendues en pharmacie
- [ ] robots.txt autorise les crawlers AI
- [ ] Tester sur mobile/tablette
- [ ] Tester en local avant push

### Nouvel article de blog

**Structure & navigation :**
- [ ] Ajouter la navigation "Article précédent/suivant" en bas de l'article (voir modèle ci-dessous)
- [ ] Mettre à jour l'article précédent pour ajouter le lien "Article suivant" vers le nouveau
- [ ] Ajouter l'article dans blog.html (liste des articles) — **en première position** (le script homepage récupère le premier)
- [ ] Vérifier que l'image a un nom ASCII-safe (pas d'accents, espaces → tirets)
- [ ] Mettre à jour sitemap.xml, llms.txt et feed.json

**SEO obligatoire (chaque article doit respecter) :**
- [ ] **H2/H3 en questions** : au moins 50% des headings doivent être des questions explicites (ex: "Comment éviter...?" plutôt que "Prévention")
- [ ] **Schema.org** : MedicalWebPage (ou WebPage) + FAQPage (3-5 Q&A) + BreadcrumbList + BlogPosting
- [ ] **dateModified** dans les schemas — mettre à jour à chaque modification de l'article
- [ ] **OG image spécifique** : utiliser l'image de l'article (pas le logo générique) pour og:image et twitter:image
- [ ] **Liens internes** : minimum 3 liens vers d'autres pages du site (articles, quizzes, services, annuaire, contact)
- [ ] **Citation meta tags** : citation_title, citation_author, citation_author_institution, citation_publication_date, citation_language
- [ ] **Hyper-localisation** : mentionner Quéven, Bretagne, Morbihan au moins 2-3 fois
- [ ] **E-E-A-T** : sources/références en fin d'article, mécanismes biologiques, dosages précis

**Modèle bouton "Article précédent"** (à placer après les références, avant `</div></article>`) :
```html
<!-- Navigation article précédent -->
<nav style="margin-top: var(--space-3xl); padding-top: var(--space-xl); border-top: 1px solid var(--beige);">
    <a href="NOM-ARTICLE-PRECEDENT.html" style="display: flex; align-items: center; gap: var(--space-md); padding: var(--space-lg); background: linear-gradient(135deg, var(--cream) 0%, #f9f5ed 100%); border-radius: var(--radius-lg); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.transform='translateX(-4px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='none';">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        <div>
            <span style="display: block; font-size: var(--text-sm); color: var(--gray); margin-bottom: var(--space-xs);">Article précédent</span>
            <span style="display: block; font-size: var(--text-lg); color: var(--charcoal); font-weight: 600;">TITRE DE L'ARTICLE PRÉCÉDENT</span>
        </div>
    </a>
</nav>
```

### Suivi mensuel AI Search (manuel)

**Process simple (15 min/mois)**:

1. Ouvrir ChatGPT, Perplexity, Claude
2. Poser 3-5 questions clés:
   - "Comment protéger sa peau en hiver en Bretagne ?"
   - "Prévenir la grippe à Quéven pharmacie conseils"
   - "Quelle pharmacie à Quéven pour dermatologie ?"
3. Noter si Pharmacie Charnal est citée
4. Ajuster stratégie si nécessaire

---

## 📚 Documentation Connexe

**Pour travailler sur le site, consulter:**

1. **CLAUDE-Pharma.md** (`/Users/mc/Documents/MarcOS/Pharma/CLAUDE-Pharma.md`)
   - Instructions système pour Claude
   - Règles de rédaction et voix de marque
   - Standards qualité contenu
   - Optimisation AI Search (section complète)

2. **GUIDE-REDACTION-BLOG.md** (`blog/GUIDE-REDACTION-BLOG.md`)
   - Voix de Laure (ton comptoir)
   - Paramètres mesurables (formalité, certitude, rythme)
   - Patterns de phrases types
   - E-E-A-T médical

3. **PLANNING-BLOG-PHARMACIE.md** (`blog/PLANNING-BLOG-PHARMACIE.md`)
   - Calendrier éditorial
   - Idées d'articles

4. **PRD.md** (`PRD.md`)
   - Vision et objectifs business
   - Personas utilisateurs
   - Roadmap (phases et priorités)
   - Métriques de succès
   - ⚠️ **À mettre à jour** lors de changements majeurs (nouvelles fonctionnalités, évolution roadmap)

---

## 🎯 Prochaines Étapes Suggérées

**Migration style-v2.css (en cours) :**
- [ ] `index.html` - Page d'accueil
- [ ] `mentions-legales.html`
- [ ] `donnees-personnelles.html`
- [ ] `index-ordonnance.html`
- [ ] Pages marques individuelles (`Nos-marques/*-page.html`)

**Court terme:**
- [ ] Vérifier cohérence domain (.com vs .fr dans canonical URLs)
- [ ] Créer nouveaux articles blog (calendrier éditorial)

**Moyen terme:**
- [ ] Google Search Console (soumettre sitemap)
- [ ] Google My Business (optimiser fiche)
- [ ] Photos réelles pharmacie et équipe

**Long terme:**
- [ ] Système rendez-vous (Doctolib/Maiia)
- [ ] Formulaire contact (Formspree/Netlify Forms)
- [ ] Analytics léger et RGPD-friendly (Plausible, Fathom)

---

## 💡 Différence CLAUDE-Pharma.md vs README.md

**README.md (ce fichier)**:
- Documentation **POUR HUMAINS** (Dany, équipe)
- Décrit **CE QUI EXISTE** (structure, état actuel, config technique)
- Utilisé **POUR COMPRENDRE** le projet
- Format: Documentation technique classique

**CLAUDE-Pharma.md**:
- Instructions **POUR CLAUDE** (système IA)
- Décrit **COMMENT TRAVAILLER** (règles, voix, workflow, best practices)
- Utilisé **POUR GÉNÉRER DU CONTENU** cohérent et conforme
- Format: Règles et standards systématiques

**Exemple concret:**
- README: "Le bouton Au Comptoir utilise la couleur #b4a6d7"
- CLAUDE-Pharma: "Les CTAs doivent TOUJOURS inviter à venir en pharmacie physiquement"

Les deux fichiers sont complémentaires et doivent rester à jour.

---

---

## 📝 Changelog Récent

### 7 Mai 2026 (suite — fin de journée)

**Fix logos hero pages marques (6 pages) :**
- Symptôme : sur `avene-page.html`, le logo Avène n'apparaissait pas dans le hero. Audit étendu : 5 autres pages avaient un problème similaire (placeholder texte ou nom de fichier erroné)
- Pages corrigées :
  - `avene-page.html` : `__KEEP_AVÈNE_FILE__.jpeg` (placeholder jamais remplacé) → `Avene.jpeg`
  - `pileje-page.html` : `Pileje.jpg` (mauvais nom) → `Pileje-Logo.jpg`
  - `aragan-page.html` : `<!-- PLACEHOLDER -->` (vide) → `<img src="logos/aragan_logo.jpg">`
  - `arkopharma-page.html` : `<!-- PLACEHOLDER -->` (vide) → `<img src="logos/logo-arkopharma-2.png">`
  - `mustela-page.html` : texte serif "mustela" → `<img src="logos/Mustela.jpg">` (fichier renommé depuis `Mustella.93ej...`)
  - `boiron-page.html` : texte serif "BOIRON" → `<img src="logos/boiron-logo-png-transparent.png">`
- Commit : `6192b3f`

**Brands strip homepage : +25% logos Nuxe, Avène, Klorane (desktop) :**
- Logos Nuxe, Avène et Klorane apparaissaient visuellement plus petits que les autres dans la section "Les marques qu'on aime" sur desktop
- Règle CSS ajoutée dans un `@media (min-width: 768px)` ciblant via attribute selector `[alt="Nuxe"]`, `[alt="Avène"]`, `[alt="Klorane"]` : `max-width: 150px; max-height: 60px` (vs 120×48 par défaut)
- Mobile inchangé. Commit : `cdeb39d`

**Article #19 Chiens & chats rédigé + système de mapping marque→article :**
- Source : [`blog/19-chiens-chats-pharmacie/chiens-chats-pharmacie-queven.md`](blog/19-chiens-chats-pharmacie/) — ~2400 mots, voix de Laure, 6 H2 (66% en questions), 7 FAQ, sources : ANSES, ANMV, ESCCAP, ECDC, VIDAL Vétérinaire, CAPAE-Ouest, monographie Permetrix Biocanina
- Cible : page marque [Biocanina](Nos-marques/biocanina-page.html) (mention Fiprocat, Permetrix, vermifuges Biocanina, soins yeux/oreilles)
- Couvre : saisonnalité Bretagne (ESCCAP "pas d'interruption hivernale"), perméthrine toxique chat (mécanisme glucuronosyltransférase + risque indirect par léchage), maladies vectorielles (Lyme, piroplasmose, ehrlichiose), tableau fréquence vermifuge par profil
- Publication cible : lundi 18 mai 2026

**Mapping marque → article blog :**
- Nouveau fichier [`blog/BRAND-BLOG-MAPPING.md`](blog/BRAND-BLOG-MAPPING.md) — référence pour le maillage SEO interne (chaque page marque doit être liée à un article blog)
- État au 7 mai : 9 marques liées (commit `be69f98`), 3 en cours (Klorane, Nuxe, Biocanina via #18 et #19), 4 à lier (Mustela, Biogaran, Bion3, Boiron)
- 6 articles supplémentaires planifiés (mai-novembre 2026) pour atteindre 16/16 marques liées : voir [`blog/PLANNING-BLOG-PHARMACIE.md`](blog/PLANNING-BLOG-PHARMACIE.md)

### 7 Mai 2026

**Fix CSS — Bloc "Pour aller plus loin sur le blog" (9 pages marques) :**
- Symptôme : sur `larosee-page.html` (et 8 autres), le texte du bloc "POUR ALLER PLUS LOIN SUR LE BLOG" se collait au border-left coloré, sans aucun padding visible
- Cause : la div `.laure-blog-link` utilisait `padding: var(--space-20) var(--space-24)` en inline, mais `--space-20` n'est défini **nulle part** dans le projet (ni dans le `<style>` inline des pages marques, ni dans `style.css` / `style-v2.css`). Une `var()` non définie sans fallback dans une shorthand rend la déclaration invalide à la résolution → `padding` retombe à `0` sur les 4 côtés
- Fix : remplacement par `padding: 20px 24px` hardcodé sur les 9 pages concernées (aragan, arkopharma, avene, bioderma, la-roche-posay, larosee, natform, nuxe, pileje)
- Commit : `fe9252a`

**Homepage — Section "Quel soin vous correspond?" (4 quiz) :**
- Layout desktop passe de **3 colonnes × 2 rangées (bento asymétrique)** à **4 colonnes × 1 rangée**
- Toutes les cartes deviennent carrées et de même taille (`aspect-ratio: 1`)
- Suppression des règles spéciales `card--big` (Naturels qui s'étirait sur 2 rangées) et `card--wide` (Automédication qui s'étirait sur 2 colonnes)
- Section divisée par 2 en hauteur sur desktop. Mobile inchangé (2×2 carré)
- Commit : `2d3306d`

**Homepage — Hero mobile restructuré (< 768px uniquement) :**
- Nouveau layout sur téléphone : **H1 → photo → CTA** (à la place de : badge + H1 + description + CTA, sans photo)
- Photo `hp PC.jpg` désormais visible sur mobile (max 360px, centrée, coins arrondis), entre le titre et le bouton — apporte l'émotion qui manquait
- Masqués sur mobile : badge "Depuis 40 ans à Quéven", paragraphe de description, pills 40+/6j/7/4.9
- iPad et desktop (≥ 768px) **strictement inchangés** : badge + H1 + description + CTA à gauche, photo à droite
- Mécanisme : `display: contents` sur `.hero-content` libère ses enfants dans le flex column de `.hero-container`, puis `order: 1/2/3` pour intercaler `.hero-image`
- Commit : `6d6d7ea`

**Hero pills (40+/6j/7/4.9) — espacement :**
- `margin-top` passe de `12px` à `var(--space-24)` (24px) — les pills étaient collées sous la photo, manquaient d'air
- Commit : `41f12fc`

### 6 Mai 2026

**SEO — Audit Google Search Console + optimisations majeures :**

Diagnostic GSC :
- 18 pages indexées sur 50 soumises (32 en "Discovered/Crawled — currently not indexed")
- Position 9.8 sur "pharmacie queven" (207 impressions / 90j, seulement 2 clics)
- 95% des clics viennent de requêtes de marque (pharmacie charnal, charnal, etc.)
- Mobile = 63% des impressions mais CTR 4× inférieur au desktop (Local Pack capte les clics mobiles)
- Aucun problème non-critique signalé

Quick wins appliqués sur `index.html` (homepage) :
- **Title** : `Pharmacie Charnal — Pharmacie à Quéven (56) | Vaccination, conseil, parapharmacie`
- **Meta description** : enrichie avec Quéven (56) + Lorient + services + téléphone
- **H1** : conservé `Votre santé, notre priorité` (préférence Dany) — mot-clé "Quéven" déplacé dans la hero description
- **Canonical** : `/index.html` → `/` (corrige le "Duplicate canonical" GSC)
- **og:url, twitter:url** : alignés sur `/`
- **sitemap.xml** : home pointe sur `/`, `lastmod` actualisé

Page Pharmacie de garde — boost SEO complet :
- H1 : `Pharmacie de garde à Quéven, Hennebont & Lorient Sud`
- Title enrichi : `... — Nuit, dimanche, jour férié 2026`
- Section intro de 250+ mots ajoutée (service expliqué, 19 communes listées, callout 3237)
- Schema **Pharmacy** avec `areaServed` (8 villes : Quéven, Hennebont, Lorient, Guidel, Lanester, Caudan, Ploemeur, Pont-Scorff)
- Section "Aussi à la Pharmacie Charnal" en bas (4 cartes vers home, services, annuaire, contact)

Homepage — section blog magazine-style :
- Layout 2 colonnes : article featured (grande image + texte/CTA) à gauche, **4 mini-cartes horizontales** d'articles précédents à droite (thumbnail 120×90 + date + titre)
- Auto-population JS depuis `blog.html` (cards #1 à #5) — quand un nouvel article est publié, la home se met à jour seule
- Responsive : empilement vertical <900px, thumbs réduits <480px
- Style aligné sur les cartes services (background `--gray-100`, hover `--pastel-sage` + slide droite)

Brands strip — CTA :
- `Voir toutes nos marques` → `Découvrez leurs histoires` (pluriel, plus engageant)

Pages marques enrichies (par Dany) :
- ✅ Avène, Biocanina, Biogaran, Caudalie, La Rosée, Pileje — contenu unique par marque, schema Product, narratif local
- Sitemap `lastmod` mis à jour pour ces 6 pages

Search Console — actions manuelles :
- ✅ Réindexation demandée pour `/` + 7 pages stratégiques (pharmacie-de-garde, services, annuaire-sante, recrutement, histoire, blog, nosmarques)
- Suivi mensuel : position "pharmacie queven" (cible <5 sous 30j), pages indexées (cible 25+/50 sous 60j)

Documentation source :
- Audit complet sauvegardé dans `Pharma/Pharma online/SEO TO DO/SEO-Analysis-2026-05-06.md`

### 17 Avril 2026

**Blog — Article #15 Jambes lourdes prêt pour publication (lundi 21 avril) :**
- Article source : [`blog/15-jambes-lourdes/jambes-lourdes-circulation-veineuse-queven.md`](blog/15-jambes-lourdes/) — ~1900 mots lisibles, 8 H2 (75% en questions), answer-first 40-60 mots après chaque H2, infographie HTML 4 classes de compression, 9 références (HAS, SFMV, EMA, Ameli, DREES, VIDAL, IFOP, Cochrane, Framingham)
- Vérification médicale Perplexity : 8/10 confirmées; 2 nuancées sur les classes de compression (article utilise la norme française LPPR, pertinente pour le public; la norme européenne RAL-GZ 387 est différente mais non applicable ici)
- Post GMB multi-canal : [`GMB/POST-GMB-15-jambes-lourdes.md`](../GMB/POST-GMB-15-jambes-lourdes.md) (6 sections : GMB, Instagram, Facebook, LinkedIn, Photo, Timing)
- URL raccourcie : `https://is.gd/ghWTHi`
- Image hero + OG : `blog-15-jambes-lourdes.jpg` (1204x803) + `og-15-jambes-lourdes.jpg` (1200x630, face-aware crop) — commitées sur branche feature `blog-15-jambes-lourdes` (pas encore mergées dans main, donc non publiques)
- Article précédent (paracétamol #14) mis à jour avec lien "Article suivant" → jambes lourdes
- Navigation inter-articles : à finaliser dans le HTML lors du passage en publication le 21 avril
- [`GMB/INDEX-POSTS-GMB.md`](../GMB/INDEX-POSTS-GMB.md) : post #15 ajouté, nouvelle catégorie "Circulation veineuse" créée

### 11 Avril 2026

**Vercel + Clean URLs :**
- Ajout de `vercel.json` à la racine (`cleanUrls: true`, `trailingSlash: false`)
- Redirects 301 pour aplatir les sous-dossiers avec espaces (`Moral en berne/`, `Peau Seche/`) vers URLs propres
- Rewrites pour servir les bons `.html` depuis les URLs aplaties
- Section "Déploiement Vercel" ajoutée au README

### 5 Avril 2026

**planning.html — Fix samedi vacances:**
- Warning dynamique dans le formulaire vacances : quand la date de fin tombe un vendredi et que l'employée travaille le samedi matin, un bandeau orange s'affiche avec lien "Inclure le samedi →" pour auto-étendre la date de fin au samedi
- Ajout de `employeeTravailleSamedi(employee)` — détecte les employées concernées selon le planning paire/impaire (Laure, Claire, Sandrine, Titia, Melanie)

### 29 Mars 2026

**Homepage — Réorganisation sections:**
- Section "On s'occupe de Vous" (services) remontée au-dessus des cartes quiz couleur
- Nouveau titre "Quel soin vous correspond?" ajouté à la section quiz, aligné à gauche (même layout que "On s'occupe de Vous" — titre à gauche, grille à droite sur desktop)

### 27 Février 2026

**Homepage Hero:**
- Suppression du `::before` opaque (fond `pastel-teal`) derrière l'image hero — remplacé par un `box-shadow` subtil deux couches
- Image hero visible dès 768px (au lieu de 1024px) avec taille réduite (360px), taille complète (540px) à 1024px+
- Breakpoints hero-container et hero-cta alignés à 768px

### 20 Février 2026

**Quizzes:**
- Quiz produits naturels publié (`quiz-produits-naturels.html`) — badge homepage mis à jour
- Page guide quizzes créée (`guide-quizzes-sante-pharmacie-queven.html`) — hub SEO pour les 3 quiz
- "Quizzes santé" ajouté au dropdown Services (navbar) et footer Navigation sur toutes les pages (43 pages)
- Homepage : lien "Voir tous nos quiz" sous les badges quiz

**Blog:**
- Article "Fatigue et moral en fin d'hiver" publié (16 fév)
- Article "Gastro-entérite : prévention et bons réflexes" publié (21 fév)
- Article Peau Sèche déplacé dans sous-dossier `Peau Seche/`
- Stratégie SEO blog documentée (`SEO blog strategy.md`)

**SEO:**
- sitemap.xml mis à jour (+3 URLs : quiz produits naturels, guide quizzes, gastro)
- llms.txt mis à jour (section Quiz interactifs + articles récents)

### 6 Février 2026

**Pages de marques (`Nos-marques/*-page.html`):**
- Bouton "Découvrez une autre marque" : transformé en pill button (teal, centré) au lieu d'une carte

**nosmarques.html:**
- Logos des marques maintenant cliquables (lien vers la page de marque)

**style-v2.css:**
- Fix menu mobile dropdown : les liens "Annuaire Santé" etc. fonctionnent maintenant correctement sur mobile
- Ajout `display: flex` sur `.nav-dropdown` mobile
- Masquage du `::before` pseudo-element sur mobile (bloquait les touches)
- Ajout `touch-action: manipulation` pour réponse tactile plus rapide

**histoire.html:**
- Section "Nos Valeurs" : 2 colonnes sur mobile au lieu de 1 (4 cartes empilées)

**Blog:**
- Article "Humidité et douleurs articulaires" ajouté à blog.html avec image corrigée
- Navigation inter-articles ajoutée (Article précédent/suivant)
- `GUIDE-REDACTION-BLOG.md` : checklist obligatoire pour navigation entre articles

---

**Dernière mise à jour**: 7 Mai 2026
**Version du site**: Production (main branch) - Migration style-v2.css en cours
**Statut**: ✅ En ligne sur www.pharmaciecharnal.com
