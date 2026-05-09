# Nos Marques - Guide de Création des Pages

Ce guide documente le processus de création des pages dédiées aux marques pour le site Pharmacie Charnal.

> **📅 Dernière mise à jour majeure : 2026-05-09**
> Nouveau standard : **3 sections SEO/AEO** (Innovations + FAQ + **Le conseil de Laure**) + **navigation 3-button** (prev/catalog/next) + **photos hero éditoriales** style Air France
> 15 pages harmonisées avec le design system officiel (template `la-roche-posay-page.html`)
> Marques : Arkopharma remplacée par S.I.D Nutrition (mai 2026), Ducray et Caudalie retirées, La Rosée ajoutée
> Nouveaux fichiers : [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md) + [`scripts/optimize-hero.sh`](scripts/optimize-hero.sh)

---

## Structure du Dossier

```
Nos-marques/
├── README.md                    # Ce fichier
├── HERO-IMAGE-PROMPTS.md        # 🎯 Prompts photos hero (style Air France) — 1 par marque
├── TEMPLATE-marque.html         # Template placeholders (mis à jour 2026-05-09 avec Innovations + FAQ + Laure)
├── nosmarques.html              # 🎯 Page catalogue officielle (harmonisée avec index-redesign)
├── scripts/                     # Scripts utilitaires
│   └── optimize-hero.sh         # 🎯 Pipeline d'optimisation photos hero (sips + cjpeg)
├── logos/                       # Logos + photos hero (source unique)
│   ├── {brand-logos}.{png,jpg,svg,avif}
│   ├── SID-Nutrition-hero.jpg   # 📷 Hero photo S.I.D Nutrition
│   ├── Biocanina-hero.jpg       # 📷 Hero photo Biocanina
│   ├── Klorane-hero.jpg         # 📷 Hero photo Klorane
│   ├── La-Rosee-hero.jpg        # 📷 Hero photo La Rosée
│   ├── Nuxe-hero.jpg            # 📷 Hero photo Nuxe
│   ├── Avene-hero.jpg           # 📷 Hero photo Avène
│   ├── Bioderma-hero.jpg        # 📷 Hero photo Bioderma
│   └── La-Roche-Posay-hero.jpg  # 📷 Hero photo La Roche-Posay (autres à venir)
├── la-roche-posay-page.html     # 🎯 TEMPLATE OFFICIEL - Copier pour nouvelles marques
├── bioderma-page.html           # ✅ Page dédiée Bioderma
├── avene-page.html              # ✅ Page dédiée Avène
├── nuxe-page.html               # ✅ Page dédiée Nuxe
├── larosee-page.html            # ✅ Page dédiée La Rosée (créée 2026-02-11)
├── klorane-page.html            # ✅ Page dédiée Klorane (+ hero photo 2026-05-09)
├── biogaran-page.html           # ✅ Page dédiée Biogaran
├── bion3-page.html              # ✅ Page dédiée Bion 3
├── boiron-page.html             # ✅ Page dédiée Boiron
├── biocanina-page.html          # ✅ Page dédiée Biocanina (+ hero photo 2026-05-09)
├── sid-nutrition-page.html      # ✅ Page dédiée S.I.D Nutrition (créée 2026-05-09, remplace Arkopharma, hero photo)
├── pileje-page.html             # ✅ Page dédiée PiLeJe
├── mustela-page.html            # ✅ Page dédiée Mustela
├── natform-page.html            # ✅ Page dédiée Nat&Form
├── aragan-page.html             # ✅ Page dédiée Aragan
├── caudalie-page.html           # ❌ DÉPRÉCIÉ - Non lié (remplacée par La Rosée)
└── *.md                         # Briefs/contenus pour futures pages
```

---

## Vue d'ensemble

### État actuel
- **15 marques actives** avec pages dédiées complètes
- **Page catalogue** : `nosmarques.html` (grille responsive avec filtrage par catégorie)
- **Template officiel** : `la-roche-posay-page.html` (design system harmonisé)
- **Template avec placeholders** : `TEMPLATE-marque.html` (grille benefits 2x2, nav avec Contact dropdown)
- **Tous les liens fonctionnels** entre le catalogue et les pages individuelles
- **✅ 15 pages harmonisées** avec le nouveau design system

### Dernières mises à jour

#### 2026-05-09 — Nouveau standard sections + photos hero éditoriales

**Sections SEO/AEO ajoutées au template** (sections 7-9, voir détail plus bas) :
- ✅ **Innovations 2024-2025** : grille 4 cartes nouveautés produit, border-left couleur marque
- ✅ **FAQ avec Schema FAQPage** : 5 questions/réponses avec JSON-LD pour Google AI Overviews / GEO
- ✅ **Le conseil de Laure** : photo ronde de Laure + 3 paragraphes voix Laure + signature + lien blog (OBLIGATOIRE)

**Navigation 3-button entre marques** (toutes les pages) :
- ✅ Remplacement du bouton unique "Découvrez une autre marque" par un menu 3 colonnes : Marque précédente · Toutes les marques · Marque suivante
- ✅ Navigation circulaire (Bioderma prev = Bion 3, Bion 3 next = Bioderma)
- ✅ Mobile : prev+next côte à côte, catalogue full-width en dessous

**Photos éditoriales en hero** *(en cours de déploiement)* :
- ✅ S.I.D Nutrition : apothicaire still-life + romarin (Provence)
- ✅ Biocanina : femme + golden retriever (jardin Provence, oliviers, lavandes)
- ✅ Klorane : maman + fille (salle de bain Provence, bouquet avoine+camomille)
- 🟡 Reste à faire : Bioderma, La Roche-Posay, Avène, Nuxe, La Rosée, Biogaran, Nat&Form, PiLeJe, Boiron, Mustela, Aragan, Bion 3
- 📄 Voir [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md) pour les 15 prompts (style Air France, 1 par marque, incarnation de l'identité)

**Pattern d'intégration hero photo** (CSS appliqué) :
- Background `cover` + overlay cream gradient à gauche (lisibilité texte)
- Mobile : `background-position: 65% center` (ajustable par photo) pour centrer le sujet derrière le texte + overlay cream adouci pour laisser respirer la photo
- Logo right-card hidden (`.hero-visual { display: none !important }`) — la photo porte le branding
- Logo réintégré dans une 5e card de la section Innovations (rappel identité visuelle)

**Outil d'optimisation photos** :
- 📄 [`scripts/optimize-hero.sh`](scripts/optimize-hero.sh) : pipeline `sips` + `cjpeg` libjpeg-turbo
- Resize max 2400px, strip metadata, JPEG progressif q=82
- Usage : `./scripts/optimize-hero.sh INPUT_FILE SLUG` → sauve direct dans `logos/{BrandName}-hero.jpg` (le script convertit le slug → BrandName automatiquement)
- Gain typique : 85-92% de réduction sur PNG sources HD

**Marque remplacée** :
- ❌ **Arkopharma** retirée (rachetée par Dermapharm 2023, plus en cohérence avec positionnement français accessible)
- ✅ **S.I.D Nutrition** ajoutée (laboratoire Allauch, phytothérapie pharmaceutique française accessible)

#### 2026-02-11 — Refresh design system

**Changements :**
- ❌ **Ducray** retirée (marque non vendue en pharmacie)
- ❌ **Caudalie** retirée (remplacée par La Rosée)
- ❌ **Vichy** retirée (marque non vendue en pharmacie)
- ✅ **La Rosée** ajoutée (cosmétique naturelle, fondée par des pharmaciennes)
- ✅ Grille "Pourquoi nous avons choisi" : 2x2 au lieu de 3+1 (toutes les pages)
- ✅ Suppression des badges "Nouveau" sur les cartes produits
- ✅ Nav corrigée sur toutes les pages (Contact dropdown avec Recrutement)

✅ **15 pages actives** :
1. la-roche-posay-page.html (template de référence)
2. avene-page.html
3. biocanina-page.html
4. bioderma-page.html
5. biogaran-page.html
6. bion3-page.html
7. larosee-page.html *(nouveau 2026-02-11)*
8. klorane-page.html
9. nuxe-page.html
10. pileje-page.html
11. boiron-page.html
13. mustela-page.html
14. sid-nutrition-page.html *(remplace arkopharma-page.html, mai 2026)*
15. natform-page.html
16. aragan-page.html

**Design system appliqué (2026-02-06)** :
- ✅ `--charcoal` modifié de `#2C2C2C` → `#1F2121`
- ✅ Ajout variables CSS manquantes : `--text-xs`, `--text-sm`, `--text-base`, `--text-lg`, `--text-xl`
- ✅ Ajout `--ease-standard`, `--font-display`, `--font-body`
- ✅ Grilles mobile optimisées : 2 colonnes pour benefits et produits
- ✅ Footer harmonisé : fond `#1F2121`, layout mobile compact (Contact + Horaires)
- ✅ Responsive mobile : padding réduit, descriptions/listes masquées sur mobile

---

## Page Catalogue : nosmarques.html

### Caractéristiques
- **Police display** : Fraunces (serif élégant)
- **Police body** : Plus Jakarta Sans
- **Footer** : Gradient teal-vert (`linear-gradient(#2D5F5D, #5A7563)`)
- **Variables CSS** : Nommage simplifié (`--teal`, `--sage`, `--pastel-*`)
- **Mobile** : Grille 2 colonnes pour les cartes marques (gap 16px)
- **Filtrage** : Système de pills par catégorie
- **Animations** : Staggered fade-in pour les cartes

### Structure des sections
1. **Hero** : Badge + titre + description
2. **Filtres catégorie** : Pills interactives sticky
3. **Grille marques** : 3 colonnes desktop, 2 colonnes mobile
4. **CTA contact** : Fond gradient avec bruit subtil
5. **Footer** : Identique au footer principal du site

---

## Créer une Nouvelle Page de Marque

### Étape 1 : Rassembler les informations

**Sources d'information :**
- Fiches marques : `/Users/mc/Documents/MarcOS/Pharma/GESTION/1-RESSOURCES/Fiche par Marque/`
- Site officiel de la marque
- Briefs existants dans ce dossier (fichiers `.md`)

**Informations nécessaires :**
| Élément | Description | Exemple |
|---------|-------------|---------|
| Nom de la marque | Nom officiel | Biogaran |
| Slogan/Tagline | Phrase d'accroche | "Des vitamines accessibles et de qualité" |
| Année de fondation | Date de création | 1996 |
| Couleur principale | Code hex de la marque | `#0066CC` |
| Couleur sombre | Variante foncée | `#004C99` |
| Catégorie | Type de produits | Compléments Alimentaires |
| Description courte | 1-2 phrases | Leader français des génériques... |
| Stats clés | 2-3 chiffres marquants | 30+ ans, 345M boîtes/an |
| Gammes de produits | 3-4 catégories | Vitamines, Minéraux, Formules |
| Coup de cœur | Produit recommandé | Vitamine D |
| Logo | Fichier dans logos/ | `Biogaran logo.jpg` |

### Étape 2 : Créer la page HTML

1. **Copier le template officiel** : `la-roche-posay-page.html` → `[marque]-page.html`
2. **Remplacer les contenus** La Roche-Posay par ceux de la nouvelle marque
3. **Adapter les couleurs** dans `:root` selon l'identité de la marque (voir Palette des Marques)
4. **Vérifier le responsive** mobile (grilles 2 colonnes, footer compact)
5. **Personnaliser les 3 nouvelles sections SEO/AEO** (depuis 2026-05-09) :
   - Innovations 2024-2025 (4 cards de nouveautés produit propres à la marque)
   - FAQ : 5 questions/réponses spécifiques + Schema JSON-LD FAQPage
   - **Le conseil de Laure** : 3 paragraphes dans la voix de Laure, signature, lien blog complémentaire (cf [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md) pour le ton)
6. **Mettre à jour les liens de navigation 3-button** : prev/next selon ordre catalogue (circulaire)
7. **Générer la photo hero** (optionnel mais recommandé) :
   - Suivre le prompt brand-spécifique dans [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md)
   - Optimiser : `./scripts/optimize-hero.sh ~/Downloads/photo.jpg slug`
   - Appliquer le pattern CSS hero-photo (cf section "Hero photo intégration" plus bas)

### Étape 3 : Mettre à jour le catalogue

Ajouter la marque dans `nosmarques.html` :

1. **Ajouter le filtre** (si nouvelle catégorie) dans `.category-pills` :
```html
<button class="category-pill" data-category="[categorie]">[Nom Catégorie]</button>
```

2. **Ajouter la carte** dans `.brands-grid` :
```html
<!-- [Nom Marque] -->
<article class="brand-card" data-category="[categorie]">
    <div class="brand-card-image">
        <img src="logos/[logo-fichier]" alt="Logo [Nom Marque]" class="brand-logo">
    </div>
    <div class="brand-card-content">
        <span class="brand-category">[Catégorie Affichée]</span>
        <h3 class="brand-name">[Nom Marque]</h3>
        <p class="brand-description">
            [Description courte 1-2 phrases]
        </p>
        <a href="[marque]-page.html" class="brand-link">
            Découvrir la marque
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
        </a>
    </div>
</article>
```

---

## Personnalisation des Couleurs par Marque

### Principe

Chaque page de marque a sa propre palette de couleurs basée sur l'identité visuelle de la marque. **Le header et le footer restent identiques** sur toutes les pages pour maintenir la cohérence du site Pharmacie Charnal.

### Éléments à personnaliser

| Élément | Variable CSS | Description |
|---------|-------------|-------------|
| Couleur principale | `--teal-pro` | Remplacer par la couleur marque |
| Couleur sombre | `--teal-dark` | Version foncée de la couleur |
| Couleurs secondaires | `--sage-natural`, `--sage-soft` | Nuances complémentaires |
| Pastels | `--pastel-teal`, `--pastel-sage`, `--pastel-mint` | Fonds de sections |
| Couleur texte | `--charcoal`, `--gray` | Adapter si nécessaire |
| Ombres | `--shadow-*` | Teinter avec la couleur marque |

### Éléments fixes (NE PAS MODIFIER)

- **Header/Navigation** : Couleurs Pharmacie Charnal (styles inline)
- **Footer** : Gradient `#2D5F5D` → `#5A7563` (teal-vert)
- **Structure HTML** des sections

**IMPORTANT** : Le CSS du footer et du header doit utiliser des **couleurs fixes** (hex ou rgba), PAS des variables CSS. Sinon, la personnalisation des variables `:root` pour la marque affectera aussi le footer/header.

```css
/* CORRECT - Couleurs fixes */
.footer {
    background: linear-gradient(135deg, #2D5F5D 0%, #5A7563 100%);
    color: #fff;
}

/* INCORRECT - Variables qui seront modifiées */
.footer {
    background: var(--teal);
    color: var(--gray-light);
}
```

### Palette des Marques Existantes

| Marque | Principale | Sombre | Pastels |
|--------|-----------|--------|---------|
| **Biogaran** | `#0066CC` (bleu) | `#004C99` | `#E3F2FD`, `#E8F4FC`, `#F0F7FF` |
| **Bioderma** | `#00A3E0` (bleu ciel) | `#0082B4` | `#E0F4FC`, `#F0FAFF` |
| **La Roche-Posay** | `#003D7D` (bleu marine) | `#002D5C` | `#E8F0F8`, `#F0F5FA` |
| **Avène** | `#F47920` (orange) | `#D66A1C` | `#FFF3E8`, `#FFEDE0` |
| **Nuxe** | `#C9A227` (doré) | `#A68620` | `#FDF8E8`, `#FFF9E6` |
| **La Rosée** | `#F57EB6` (rose) | `#D4609A` | `#FDF0F6`, `#F5E0EC` |
| **Klorane** | `#00843D` (vert) | `#006830` | `#E8F5ED`, `#F0FAF4` |
| **Biocanina** | `#E31837` (rouge) | `#B81430` | `#FCE8EB`, `#FFF0F2` |

---

## Sections d'une Page de Marque

### 1. Hero
- Badge catégorie
- Titre + slogan en italique
- Description (2-3 phrases)
- Stats clés (3 chiffres)
- Boutons CTA
- Visual avec logo ou image produit

### 2. Histoire/Introduction
- Timeline avec dates clés
- Cercles animés avec année de fondation
- Texte d'introduction

### 3. Expertise/Philosophie
- Titre accrocheur
- Description de la philosophie
- 3 cartes avec icônes (points forts)
- Citation/blockquote

### 4. Pourquoi cette marque
- 4 avantages numérotés (grille 2x2, pas 3+1)
- Cartes avec animation hover

### 5. Produits/Gammes
- Onglets de filtrage par catégorie
- 3-5 cartes produits avec :
  - Image de fond dégradé
  - Titre de gamme
  - Sous-titre
  - Liste de produits
  - Lien "Demander conseil"
  - **Pas de badges "Nouveau"** (supprimés)

### 6. Conseil/Coup de cœur
- Titre : "Un conseil" (pas "Notre conseil")
- Texte de conseil pharmacien
- Encart avec produit coup de cœur
- **Important** : `<strong>` dans cette section doit avoir `color: var(--white)` pour contraster avec le fond sombre

### 7. Innovations 2024-2025 *(standard depuis 2026-05-09)*
- Section avec badge "Nouveautés 2024-2025"
- Grille de **4 cartes innovation** (`auto-fit minmax(260px)`)
- Chaque carte : catégorie (uppercase) + titre + description courte
- Border-left 4px de la couleur dominante de la marque
- Background : `var(--pastel-sage)` ou pastel marque
- **Class CSS** : `.brand-innovations` (ou `.{marque}-innovations`)

### 8. FAQ avec Schema FAQPage *(standard depuis 2026-05-09)*
- 5 questions/réponses sur la marque (`<details><summary>`)
- Background blanc, items en cards avec hover
- **Schema JSON-LD `FAQPage`** dupliquant les Q&A en plain text (sans HTML tags) — important pour Google AI Overviews / GEO
- **Class CSS** : `.brand-faq` (ou `.{marque}-faq`)

### 9. Le conseil de Laure *(standard depuis 2026-05-09 — OBLIGATOIRE)*
- **Photo de Laure** (140x140 ronde, bordure blanche 4px, ombre douce) → `images/Laure CNL.jpeg`
- Layout : grid `140px 1fr`, gap 32px, `align-items: start`
- Tagline label "Le conseil de Laure" en small caps + couleur marque
- **Titre** : H2 dans la voix de Laure (ex: "{Marque} à la pharmacie : mes recommandations par profil")
- **3 paragraphes** dans la voix de Laure (« je recommande », « chez nous », références produits concrets, ancrage local)
- Signature italique : `— Laure Charnal, pharmacienne titulaire à Quéven`
- **Article blog associé** dans une card en bas (border-left couleur marque) avec titre du blog complémentaire
- Background : pastel de la marque (solid, **PAS de cream gradient** — depuis 2026-05-09 pour éviter les zones jaune-cream qui rompent le rythme blue/white de chaque page)
- **Mobile (< 640px)** : photo passe au-dessus du texte (`grid-template-columns: 1fr`, `text-align: center`)
- **Class CSS** : `.brand-laure` (ou `.{marque}-laure`)

### 10. Navigation entre marques *(standard depuis 2026-05-09)*
- **3 boutons** dans une grille `1fr auto 1fr`:
  - **← Marque précédente** (carte blanche, hover border-color marque)
  - **Toutes les marques** (CTA central, fond `var(--teal-pro)` couleur marque)
  - **Marque suivante →** (carte blanche, hover border-color marque)
- **Navigation circulaire** (Bioderma prev = Bion 3, Bion 3 next = Bioderma)
- **Mobile (< 640px)**: prev + next côte à côte sur une ligne, "Toutes les marques" full-width en dessous (`grid-template-areas: "prev next" / "all all"`)
- **Class CSS**: `.brand-nav-section` (wrapper) + `.brand-nav-link` + `.brand-nav-prev/all/next`
- Ordre des marques = ordre dans `nosmarques.html` (Bioderma → ... → Bion 3, circulaire)

### 11. Footer (standard Charnal)

---

## Catégories pour le Filtrage

| Catégorie (data-category) | Affichage | Marques |
|---------------------------|-----------|---------|
| `dermatologie` | Dermatologie | Bioderma, La Roche-Posay, Avène |
| `cosmetique` | Cosmétique | Nuxe, La Rosée |
| `capillaire` | Soins Capillaires | Klorane |
| `bebe` | Bébé & Maman | Mustela |
| `homeopathie` | Homéopathie | Boiron |
| `animaux` | Santé Animale | Biocanina |
| `complements` | Compléments | Biogaran, Nat&Form, PiLeJe, Aragan, S.I.D Nutrition, Bion 3 |

---

## Checklist Nouvelle Marque

```
[ ] 1. Rassembler les informations (fiche marque, site officiel)
[ ] 2. Récupérer/ajouter le logo dans logos/
[ ] 3. Définir la palette de couleurs (voir Palette des Marques)
[ ] 4. Copier la-roche-posay-page.html → [marque]-page.html
[ ] 5. Personnaliser les variables CSS (:root) avec les couleurs de la marque
    [ ] Vérifier que --charcoal est #1F2121
    [ ] Vérifier que toutes les variables --text-* sont présentes
    [ ] Vérifier que --font-display et --font-body sont définis
    [ ] Vérifier que --ease-standard est défini
[ ] 6. Remplacer tous les contenus La Roche-Posay
[ ] 7. Adapter les dégradés du hero et sections
[ ] 8. Vérifier les accents français (Découvrez, qualité, Quéven, etc.)
[ ] 9. Vérifier le responsive mobile :
    [ ] Grille 2x2 pour .benefits-grid (repeat(2, 1fr) mobile ET desktop)
    [ ] Grilles 2 colonnes pour .product-cards
    [ ] Images produits 120px mobile / 220px desktop
    [ ] Descriptions et listes masquées sur mobile
    [ ] Footer layout compact (Contact + Horaires, nav cachée)
    [ ] Footer fond fixe #1F2121 (pas de variable CSS)
[ ] 10. Ajouter la carte dans nosmarques.html
[ ] 11. Ajouter le filtre si nouvelle catégorie
[ ] 12. Tester le lien et le filtrage
[ ] 13. Tester sur mobile (<768px) et desktop (≥768px)
```

---

## Accents Français

**Important** : Toujours utiliser les accents corrects en français.

Exemples courants :
- qualité, santé, beauté
- compléments, génériques
- créé, fondé, élargi
- Découvrir, Équilibre
- cœur (pas coeur)
- où (pas ou pour le lieu)

---

## Template Officiel : La Roche-Posay Page

> **IMPORTANT** : La page `la-roche-posay-page.html` est le **TEMPLATE OFFICIEL** à utiliser pour créer toutes les nouvelles pages de marque. Elle remplace `TEMPLATE-marque.html` (ancien template).

Cette page applique le design system HIMS de `index-redesign` et doit être copiée comme base pour chaque nouvelle marque.

> **✅ MISE À JOUR 2026-02-06** : Toutes les 17 pages de marques ont été harmonisées avec ce template. Le design system est maintenant appliqué de manière cohérente sur l'ensemble du site.

### Améliorations appliquées (maintenant sur toutes les pages)

| Élément | Ancien style | Nouveau style (harmonisé) |
|---------|--------------|---------------------------|
| `--charcoal` | `#2C2C2C` | `#1F2121` |
| Footer | Styles inline, couleurs variables | Classes CSS, fond fixe `#1F2121` |
| Footer mobile | 1 colonne ou inline | 2 colonnes (Contact + Horaires), Navigation cachée |
| Variables CSS | Basiques | Complètes (`--text-xs` à `--text-xl`, `--font-display`, `--font-body`, `--ease-standard`) |
| Grilles | 1 colonne ou auto-fit 3+1 | 2x2 pour "Pourquoi nous avons choisi", 2 colonnes pour "Les gammes" |
| Padding mobile | Souvent fixe | Responsive avec media queries (`24px` mobile, `32px` desktop) |
| Produits mobile | Tout visible | Description et liste masquées, images réduites (120px) |

### Responsive Mobile (< 768px)

> **✅ Ces spécifications sont maintenant appliquées sur les 17 pages de marques**

**Page Catalogue (nosmarques.html)** :
- Grille marques : 2 colonnes sur mobile (au lieu de 3 desktop)
- Gap : 16px (au lieu de 32px)
- Taille cartes : optimisée pour mobile
- Filtres catégorie : défilement horizontal

**Section "Pourquoi nous avons choisi" (.benefits-grid)** :
- Grille : **toujours 2 colonnes** (`grid-template-columns: repeat(2, 1fr)`) — layout 2+2, pas 3+1
- Gap : `var(--space-16)` mobile, `var(--space-32)` desktop
- Padding cartes : `var(--space-24)` mobile, `var(--space-32)` desktop
- Numéros : `2rem` mobile, `3rem` desktop
- Margin-bottom numéros : `var(--space-8)` mobile, `var(--space-16)` desktop

**Section "Les gammes disponibles" (.product-cards)** :
- Grille : 2 colonnes (`grid-template-columns: repeat(2, 1fr)`)
- Gap : `var(--space-16)` mobile, `var(--space-32)` desktop
- Border-radius : `var(--radius-lg)` mobile, `var(--radius-xl)` desktop
- Image produit : hauteur `120px` mobile, `220px` desktop
- Badge : `top/left: 8px, padding: 4px 8px, font: 0.625rem` mobile
- Badge : `top/left: 16px, padding: 8px 12px, font: 0.75rem` desktop
- Contenu : padding `12px` mobile, `24px` desktop
- Titre h3 : `1rem / 4px` mobile, `1.375rem / 8px` desktop
- Subtitle : `0.75rem / 8px` mobile, `0.875rem / 16px` desktop
- Description `<p>` : **masquée** sur mobile (`display: none`)
- Liste produits `.product-list` : **masquée** sur mobile (`display: none`)

**Footer** :
- Fond : `#1F2121` (fixe, pas de variable)
- Navigation : **cachée** sur mobile (`.footer-nav { display: none }`)
- Layout mobile : grid 2 colonnes (Contact + Horaires côte à côte)
- Grid areas : `"brand brand" / "contact horaires"`
- Padding : `var(--space-48)` mobile, `var(--space-80)` desktop
- Social icons : `40px` mobile, `44px` desktop
- Typographie : utilise `--text-xs`, `--text-sm`, `--text-base`

### Bonnes pratiques appliquées

1. **Contraste texte** : `<strong>` dans les zones sombres utilise `color: var(--white)` (pas la couleur globale `--charcoal`)
2. **Citations en français** : Guillemets français « » et traduction des slogans anglais
3. **Logo centré** : `justify-content: center; align-items: center` dans le hero
4. **Variables typographiques** : `--text-sm`, `--text-base`, `--text-xl` au lieu de valeurs fixes
5. **Transitions harmonisées** : `--ease-standard` (cubic-bezier HIMS)

### CSS ajoutés pour le design system

```css
/* Variables à ajouter dans :root */
--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--ease-standard: cubic-bezier(0.16, 1, 0.3, 1);
--font-display: 'Cormorant Garamond', Georgia, serif;
--font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
```

---

## Outils de Maintenance

### Script de mise à jour en masse

Un script Python (`update_brand_pages.py`) a été créé pour appliquer des modifications CSS de manière systématique à plusieurs pages simultanément.

**Utilisation** :
```bash
python3 update_brand_pages.py page1.html page2.html page3.html
```

**Capacités du script** :
- Modification de variables CSS (ex: `--charcoal` de `#2C2C2C` → `#1F2121`)
- Ajout de variables CSS manquantes (`--text-*`, `--font-*`, `--ease-standard`)
- Mise à jour des grilles responsive (mobile-first avec media queries)
- Harmonisation des paddings et marges
- Remplacement du footer (styles inline → classes CSS structurées)
- Ajout du layout footer mobile compact

**Exemple de modifications appliquées (2026-02-06)** :
```bash
python3 update_brand_pages.py \
  bioderma-page.html \
  biogaran-page.html \
  bion3-page.html \
  caudalie-page.html \
  klorane-page.html \
  nuxe-page.html \
  pileje-page.html
```

> ⚠️ **Important** : Toujours tester les pages après modification automatique et vérifier que les couleurs spécifiques à chaque marque sont préservées.

---

## Fichiers de Référence

- **🎯 TEMPLATE OFFICIEL** : [`la-roche-posay-page.html`](la-roche-posay-page.html) — À copier pour chaque nouvelle marque (inclut les 3 sections SEO/AEO depuis 2026-05-09 + nav 3-button)
- **🎯 PAGE CATALOGUE** : [`nosmarques.html`](nosmarques.html) — Page principale avec grille 2 colonnes mobile
- **Template placeholders** : [`TEMPLATE-marque.html`](TEMPLATE-marque.html) — Template avec `{{PLACEHOLDERS}}` à remplacer (mis à jour 2026-05-09 avec Innovations + FAQ + Laure)
- **🎯 PROMPTS PHOTOS HERO** : [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md) — 15 prompts uniques (style Air France, 1 par marque) pour générer les hero backgrounds avec nano banana / Midjourney / DALL-E
- **🛠️ SCRIPT D'OPTIMISATION** : [`scripts/optimize-hero.sh`](scripts/optimize-hero.sh) — Pipeline `sips` + `cjpeg` pour resize 2400px + JPEG progressif q=82
- **Page dépréciée** : `caudalie-page.html` — Non liée, à supprimer éventuellement
- **Design system** : [`../index-redesign/README.md`](../index-redesign/README.md) (documentation complète du design HIMS)
- **Index redesign** : [`../index-redesign/index-redesign.html`](../index-redesign/index-redesign.html) (référence design system)
- **Fiches marques** : `/Users/mc/Documents/MarcOS/Pharma/GESTION/1-RESSOURCES/Fiche par Marque/`

---

## Hero Photo : Intégration

> **Pattern adopté depuis 2026-05-09** : remplacer le gradient pastel + bubbles + logo card par une photo éditoriale style Air France (cohérence visuelle de série, identité marque renforcée).

### 1. Générer la photo

Utiliser le prompt brand-spécifique de [`HERO-IMAGE-PROMPTS.md`](HERO-IMAGE-PROMPTS.md) avec nano banana (Imagen 3) en HD (idéalement ≥ 2400px wide).

### 2. Optimiser

```bash
./scripts/optimize-hero.sh ~/Downloads/Photo-HD.png slug
```

Le script automatise :
- Resize à max 2400px wide (préserve l'aspect)
- Strip metadata EXIF/ICC
- Re-encode JPEG progressif qualité 82 (libjpeg-turbo)
- Sauve dans `Nos-marques/logos/{BrandName}-hero.jpg` (slug → BrandName converti auto)

**Slugs → BrandName supportés** : `aragan`→`Aragan`, `avene`→`Avene`, `biocanina`→`Biocanina`, `biogaran`→`Biogaran`, `bion3`→`Bion-3`, `bioderma`→`Bioderma`, `boiron`→`Boiron`, `klorane`→`Klorane`, `la-roche-posay`→`La-Roche-Posay`, `larosee`→`La-Rosee`, `mustela`→`Mustela`, `natform`→`NatForm`, `nuxe`→`Nuxe`, `pileje`→`PiLeJe`, `sid-nutrition`→`SID-Nutrition`

### 3. Pattern CSS à appliquer dans `{slug}-page.html`

```css
.hero {
    background: url('logos/{BrandName}-hero.jpg') center/cover no-repeat;
}

/* Overlay cream à gauche pour lisibilité texte sur desktop */
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg,
        rgba(252, 245, 240, 0.92) 0%,
        rgba(252, 245, 240, 0.75) 30%,
        rgba(252, 245, 240, 0.35) 55%,
        transparent 75%);
    pointer-events: none;
}

/* Mobile : overlay vertical PLUS DOUX + repositionnement de la photo
   pour centrer le sujet derrière le texte (et non le cropper sur le bord) */
@media (max-width: 1023px) {
    .hero::before {
        background: linear-gradient(180deg,
            rgba(252, 245, 240, 0.85) 0%,
            rgba(252, 245, 240, 0.55) 50%,
            rgba(252, 245, 240, 0.45) 100%);
    }
    .hero {
        /* Ajuster selon position du sujet dans la photo :
           65% center (centre-droit défaut), 70% (droit prononcé), center (centré) */
        background-position: 65% center;
    }
}

/* Hide decorative elements - the photo carries the visual */
.hero-bubbles { display: none; }
.bubble { display: none; }
.hero-visual { display: none !important; }

/* Hero text colors for contrast over the photo */
.hero h1 { color: var(--charcoal); }
.hero h1 span { color: var(--gray); }

/* Single-column hero content (the photo is the right-side visual) */
@media (min-width: 1024px) {
    .hero-content {
        grid-template-columns: minmax(0, 620px);
    }
}
.hero-text { max-width: 620px; }
```

### 4. Réintégrer le logo dans la section Innovations (rappel d'identité visuelle)

Comme la card logo a été masquée du hero, ajouter une 5e card dans la grille `.{slug}-innovations .innovations-grid` :

```html
<article class="innovation-card brand-logo-card reveal reveal-delay-4" style="background: var(--white); border-radius: 16px; padding: var(--space-32) var(--space-24); border-left: 4px solid var(--{slug}-color); box-shadow: 0 4px 20px rgba(0,0,0,0.05); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; min-height: 240px;">
    <img src="logos/{LOGO_FILE}" alt="Logo {Brand}" style="max-width: 70%; max-height: 100px; object-fit: contain; margin-bottom: var(--space-16);">
    <div style="font-family: var(--font-display); font-size: 1.05rem; line-height: 1.4; color: var(--gray); font-style: italic;">{Brand baseline}</div>
</article>
```

### Pages déjà migrées (référence)

| Page | Photo | Logo card | Statut |
|---|---|---|---|
| [`sid-nutrition-page.html`](sid-nutrition-page.html) | apothicaire + romarin | ❌ pas de section Innovations à compléter | ✅ |
| [`biocanina-page.html`](biocanina-page.html) | femme + golden retriever | 🟡 logo card à ajouter | 🟡 partiel |
| [`klorane-page.html`](klorane-page.html) | maman + fille bain Provence | ✅ logo dans 5e card Innovations | ✅ |

---

## Notes sur les Logos

Les logos sont centralisés dans `/Nos-marques/logos/`. Ce dossier est la **source unique** pour tous les logos marques du site.

**Pour index-redesign** : Les logos sont copiés dans `/index-redesign/logos/` car les liens symboliques ne fonctionnent pas avec le protocole `file://` (ouverture locale). Si un nouveau logo est ajouté, il faut le copier dans les deux emplacements.

```bash
# Copier un nouveau logo vers index-redesign
cp "Nos-marques/logos/nouveau-logo.png" "index-redesign/logos/"
```
