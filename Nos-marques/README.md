# Nos Marques - Guide de Création des Pages

Ce guide documente le processus de création des pages dédiées aux marques pour le site Pharmacie Charnal.

> **📅 Dernière mise à jour majeure : 2026-02-06**
> 17 pages harmonisées avec le design system officiel (template `la-roche-posay-page.html`)

---

## Structure du Dossier

```
Nos-marques/
├── README.md                    # Ce fichier
├── TEMPLATE-marque.html         # ⚠️ OBSOLÈTE - Ne plus utiliser
├── nosmarques.html              # 🎯 Page catalogue officielle (harmonisée avec index-redesign)
├── logos/                       # Logos des marques (source unique)
│   ├── Avene.jpeg
│   ├── Biocanina.png
│   ├── Bioderma.png
│   ├── biogaran_logo.jpg
│   ├── Bion3_logo.png
│   ├── boiron-logo-png-transparent.png
│   ├── Caudalie.png
│   ├── DUCRAY_logo.*
│   ├── Klorane.png
│   ├── La-roche-posay.png
│   ├── logo-arkopharma-2.png
│   ├── Mustella.*
│   ├── NatForm.avif
│   ├── Nuxe.jpeg
│   ├── Pileje-Logo.jpg
│   ├── aragan_logo.jpg
│   └── Vichy.png
├── la-roche-posay-page.html     # 🎯 TEMPLATE OFFICIEL - Copier pour nouvelles marques
├── vichy-page.html              # ✅ Page dédiée Vichy (harmonisée 2026-02-06)
├── bioderma-page.html           # ✅ Page dédiée Bioderma (harmonisée 2026-02-06)
├── avene-page.html              # ✅ Page dédiée Avène (harmonisée 2026-02-06)
├── nuxe-page.html               # ✅ Page dédiée Nuxe (harmonisée 2026-02-06)
├── caudalie-page.html           # ✅ Page dédiée Caudalie (harmonisée 2026-02-06)
├── klorane-page.html            # ✅ Page dédiée Klorane (harmonisée 2026-02-06)
├── biogaran-page.html           # ✅ Page dédiée Biogaran (harmonisée 2026-02-06)
├── bion3-page.html              # ✅ Page dédiée Bion 3 (harmonisée 2026-02-06)
├── boiron-page.html             # ✅ Page dédiée Boiron (harmonisée 2026-02-06)
├── biocanina-page.html          # ✅ Page dédiée Biocanina (harmonisée 2026-02-06)
├── arkopharma-page.html         # ✅ Page dédiée Arkopharma (harmonisée 2026-02-06)
├── pileje-page.html             # ✅ Page dédiée PiLeJe (harmonisée 2026-02-06)
├── mustela-page.html            # ✅ Page dédiée Mustela (harmonisée 2026-02-06)
├── ducray-page.html             # ✅ Page dédiée Ducray (harmonisée 2026-02-06)
├── natform-page.html            # ✅ Page dédiée Nat&Form (harmonisée 2026-02-06)
├── aragan-page.html             # ✅ Page dédiée Aragan (harmonisée 2026-02-06)
└── *.md                         # Briefs/contenus pour futures pages
```

---

## Vue d'ensemble

### État actuel
- **17 marques actives** avec pages dédiées complètes
- **Page catalogue** : `nosmarques.html` (grille responsive avec filtrage par catégorie)
- **Template officiel** : `la-roche-posay-page.html` (design system harmonisé)
- **Tous les liens fonctionnels** entre le catalogue et les pages individuelles
- **✅ 16 pages harmonisées** avec le nouveau design system (mise à jour 2026-02-06)

### Dernières mises à jour (2026-02-06)

**16 pages mises à niveau vers le design system officiel** :

✅ **Pages à jour** :
1. la-roche-posay-page.html (template de référence)
2. avene-page.html
3. biocanina-page.html
4. bioderma-page.html
5. biogaran-page.html
6. bion3-page.html
7. caudalie-page.html
8. klorane-page.html
9. nuxe-page.html
10. pileje-page.html
11. vichy-page.html
12. boiron-page.html
13. mustela-page.html
14. arkopharma-page.html
15. ducray-page.html
16. natform-page.html
17. aragan-page.html

**Modifications appliquées** :
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
| **Vichy** | `#2D5F5D` (teal) | `#1E4745` | `#D4E8E7`, `#DFF5ED` |
| **Biogaran** | `#0066CC` (bleu) | `#004C99` | `#E3F2FD`, `#E8F4FC`, `#F0F7FF` |
| **Bioderma** | `#00A3E0` (bleu ciel) | `#0082B4` | `#E0F4FC`, `#F0FAFF` |
| **La Roche-Posay** | `#003D7D` (bleu marine) | `#002D5C` | `#E8F0F8`, `#F0F5FA` |
| **Avène** | `#F47920` (orange) | `#D66A1C` | `#FFF3E8`, `#FFEDE0` |
| **Nuxe** | `#C9A227` (doré) | `#A68620` | `#FDF8E8`, `#FFF9E6` |
| **Caudalie** | `#7B5E3C` (bordeaux/brun) | `#5C462D` | `#F5F0EB`, `#EDE6DF` |
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
- 4 avantages numérotés
- Cartes avec animation hover

### 5. Produits/Gammes
- Onglets de filtrage par catégorie
- 3 cartes produits avec :
  - Image de fond dégradé
  - Titre de gamme
  - Sous-titre
  - Liste de produits
  - Lien "Demander conseil"

### 6. Conseil/Coup de cœur
- Titre : "Un conseil" (pas "Notre conseil")
- Texte de conseil pharmacien
- Encart avec produit coup de cœur
- **Important** : `<strong>` dans cette section doit avoir `color: var(--white)` pour contraster avec le fond sombre

### 7. Footer (standard Charnal)

---

## Catégories pour le Filtrage

| Catégorie (data-category) | Affichage | Marques |
|---------------------------|-----------|---------|
| `dermatologie` | Dermatologie | Bioderma, La Roche-Posay, Avène, Vichy |
| `cosmetique` | Cosmétique | Nuxe, Caudalie |
| `capillaire` | Soins Capillaires | Klorane, Ducray |
| `bebe` | Bébé & Maman | Mustela |
| `homeopathie` | Homéopathie | Boiron |
| `animaux` | Santé Animale | Biocanina |
| `complements` | Compléments | Biogaran, Nat&Form, PiLeJe, Aragan, Arkopharma, Bion 3 |

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
    [ ] Grilles 2 colonnes pour .benefits-grid
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
| Grilles mobile | 1 colonne ou desktop uniquement | 2 colonnes pour "Pourquoi nous avons choisi" et "Les gammes" |
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
- Grille : 2 colonnes (`grid-template-columns: repeat(2, 1fr)`)
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

- **🎯 TEMPLATE OFFICIEL** : `la-roche-posay-page.html` — À copier pour chaque nouvelle marque
- **🎯 PAGE CATALOGUE** : `nosmarques.html` — Page principale avec grille 2 colonnes mobile
- **Ancien template (obsolète)** : `TEMPLATE-marque.html` — Ne plus utiliser
- **Ancien style (obsolète)** : `vichy-page.html` — Footer gradient, styles inline
- **Design system** : `../index-redesign/README.md` (documentation complète du design HIMS)
- **Index redesign** : `../index-redesign/index-redesign.html` (référence design system)
- **Fiches marques** : `/Users/mc/Documents/MarcOS/Pharma/GESTION/1-RESSOURCES/Fiche par Marque/`

---

## Notes sur les Logos

Les logos sont centralisés dans `/Nos-marques/logos/`. Ce dossier est la **source unique** pour tous les logos marques du site.

**Pour index-redesign** : Les logos sont copiés dans `/index-redesign/logos/` car les liens symboliques ne fonctionnent pas avec le protocole `file://` (ouverture locale). Si un nouveau logo est ajouté, il faut le copier dans les deux emplacements.

```bash
# Copier un nouveau logo vers index-redesign
cp "Nos-marques/logos/nouveau-logo.png" "index-redesign/logos/"
```
