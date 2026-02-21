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

**8 articles actuellement en ligne:**

1. **Détox après les fêtes** - `detox-apres-fetes-mythe-realite-queven.html`
2. **Humidité et douleurs articulaires** - `humidite-douleurs-articulaires-queven.html`
3. **Prévenir les maux d'hiver** - `prevenir-maux-hiver-queven.html`
4. **Professionnels de santé à Quéven** - `professionnels-sante-queven-2026.html` (carte Leaflet)
5. **Protéger sa peau sèche** - `Peau Seche/proteger-peau-seche-hiver-breton-queven.html`
6. **Vaccination adulte** - `vaccination-adulte-guide-pratique.html`
7. **Fatigue et moral en fin d'hiver** - `Moral en berne/fatigue-moral-fin-hiver-queven.html` (pub 16 fév)
8. **Gastro-entérite : prévention et bons réflexes** - `gastro-enterite-prevention-bons-reflexes-queven.html` (pub 21 fév)

**Stratégie éditoriale**:
- Ton: Voix de Laure (pharmacienne pédagogue, professionnelle accessible)
- SEO local: Quéven, Bretagne, Morbihan, climat océanique
- E-E-A-T médical: Expertise + sources + mécanismes biologiques
- Optimisé pour AI Search (FAQ, questions naturelles)

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

**Dernière mise à jour**: 20 Février 2026
**Version du site**: Production (main branch) - Migration style-v2.css en cours
**Statut**: ✅ En ligne sur www.pharmaciecharnal.com
