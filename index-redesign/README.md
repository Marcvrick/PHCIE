# Index Redesign - Pharmacie Charnal

Homepage redesign inspiree de HIMS.com, adaptee a l'identite de Pharmacie Charnal.

---

## Philosophie de design

La page reprend les codes visuels de **HIMS.com** (DTC wellness brand) et les adapte au contexte d'une **pharmacie de quartier familiale**. L'objectif : un site qui respire la modernite et la confiance, sans perdre la chaleur humaine de la pharmacie.

**Principes HIMS adaptes :**
- Pastels doux en fonds de section (jamais deux pastels identiques consecutifs)
- Beaucoup de whitespace (40-50% d'espace vide)
- Typographie serif display pour les titres (autorite douce)
- Animations subtiles au scroll (fade-up)
- Marquee banner defilant (signature HIMS)
- Layouts editoriaux deux colonnes alternees
- Promise pills (marqueurs de confiance en pilules)

**Adaptation pharmacie :**
- Remplacement du noir HIMS (#000) par **teal-pro (#2D5F5D)** partout (boutons, marquee, badges, CTA)
- Raison : le noir est trop agressif pour une pharmacie de quartier. Le teal maintient un contraste AAA (7.8:1) tout en evoquant le medical et la confiance
- Ton plus chaleureux et familial vs le ton trendy/masculin de HIMS

---

## Palette de couleurs

### Pastels (fonds de sections, style HIMS)
| Variable | Hex | Usage |
|---|---|---|
| `--pastel-sage` | `#E8F0EA` | Fond editorial 1 (blog), hero gradient |
| `--pastel-mint` | `#D4E8E0` | Fond services, hero gradient |
| `--pastel-teal` | `#D0E5E4` | Fond derriere hero image, icon backgrounds |
| `--pastel-cream` | `#FBF9F6` | Fond sections claires |
| `--pastel-peach` | `#FEF0E6` | Disponible |
| `--pastel-lavender` | `#EDE8F5` | Fond section marque spotlight |

### Couleurs principales (marque)
| Variable | Hex | Usage |
|---|---|---|
| `--teal-pro` | `#2D5F5D` | **Couleur primaire partout** : boutons, marquee, badges, liens, CTA |
| `--sage-natural` | `#7C9885` | Accents secondaires |
| `--sage-dark` | `#5A7563` | Hover sur liens |
| `--bleu-confiance` | `#4A7C8E` | Gradient CTA (teal -> bleu) |
| `--emerald` | `#50A686` | Disponible |

### Neutres
| Variable | Hex | Usage |
|---|---|---|
| `--cream` | `#FFFEF9` | Background body |
| `--charcoal` | `#1F2121` | Texte principal, footer background |
| `--gray-500` | `#6B7280` | Texte secondaire |
| `--gray-600` | `#4B5563` | Description hero |
| `--copper` | `#B0732B` | Etoiles avis Google |

---

## Typographie

| Role | Font | Fallback | Usage |
|---|---|---|---|
| Display (titres) | **Fraunces** (optical-size serif) | Georgia, serif | Tous les h1, h2, h3, stats, badges |
| Body (corps) | **DM Sans** (geometric sans) | system-ui, sans-serif | Paragraphes, navigation, boutons, labels |

**Echelle typographique :**
- Hero title : `clamp(2.5rem, 6vw, 3.75rem)` — responsive fluid
- Section titles : `clamp(1.875rem, 4vw, 3rem)`
- Body text : `1rem` (16px) / line-height 1.6
- Small labels : `0.75rem-0.875rem` uppercase avec letter-spacing

**Effet signature :** les mots-cles dans les titres utilisent `.highlight` — couleur teal + italique (Fraunces italique est tres distinctif grace a l'optical sizing).

---

## Grille et espacements

- **Systeme 8pt grid** : toutes les valeurs de spacing sont des multiples de 8 (`--space-8` a `--space-128`)
- **Container** : `max-width: 1280px`, padding responsive (24px mobile, 48px tablette, 64px desktop)
- **Breakpoints** :
  - `768px` : tablette (nav visible, grilles 2 colonnes)
  - `1024px` : desktop (hero 2 colonnes, grilles 3+ colonnes, image hero visible)
  - `1440px` : large desktop (padding container augmente)

---

## Structure des sections (ordre de la page)

| # | Section | Fond | Classes cles |
|---|---|---|---|
| 1 | **Navigation** | Glass blur (rgba blanc 0.92) | `.navbar`, `.nav-dropdown` |
| 2 | **Hero** | Gradient sage -> mint -> cream | `.hero`, `.hero-container` |
| 3 | **Marquee banner** | Teal-pro (#2D5F5D) | `.marquee-banner`, `.marquee-track` |
| 4 | **Product feature cards** | Cream | `.product-features`, `.product-features-grid` |
| 5 | **Services** | Pastel mint | `.services`, `.services-grid` |
| 6 | **Editorial - Dernier article blog** | Pastel sage | `.editorial--sage`, `#latest-article-section` |
| 7 | **Brand Spotlight** | Pastel lavender | `.brand-spotlight`, `#brand-spotlight` |
| 8 | **Stats bar** | Blanc | `.stats-bar`, `.stats-grid` |
| 9 | **CTA** | Gradient teal -> bleu | `.cta-section` |
| 10 | **Footer** | Charcoal | `.footer`, `.footer-grid` |

**Regle d'alternance :** jamais deux fonds identiques consecutifs. La sequence suit : sage gradient -> teal -> cream -> mint -> sage -> lavender -> blanc -> teal gradient -> charcoal.

---

## Composants cles

### Navigation
- **Desktop** : barre fixe avec blur backdrop, dropdowns au hover (Services -> Notre Histoire / Pharmacie de garde / Annuaire Sante ; Contact -> Recrutement)
- **Mobile** : hamburger menu, fullscreen overlay avec sous-liens indentes + bordure verte a gauche
- Le dropdown a un triangle CSS (`clip-path`) qui pointe vers le lien parent
- CTA "Appeler" visible uniquement desktop

### Boutons
- `.btn-primary` : fond teal-pro, texte blanc, hover scale(1.02) + shadow teal
- `.btn-secondary` : bordure grise, hover fond gris leger
- `.btn-sm` / `.btn-lg` : variantes de taille
- **Pas de noir** : tous les CTA sont teal-pro

### Product feature cards (style HIMS)
- **Inspiration** : la rangee de cartes produits sur hims.com (ex: "Lose weight", "Have better sex", etc.)
- **Adaptation** : 4 cartes categories pharmacie — Produits naturels, Dermocosmetique, Complements alimentaires, Automedication
- **Layout** : 4 colonnes desktop, 2 colonnes mobile (2x2 grid)
- **Structure par carte** : titre avec mot-cle en accent colore + chevron fleche + icone SVG sur fond pastel
- **Accents colores** : `.accent-green` (sage), `.accent-teal` (teal-pro), `.accent-copper` (cuivre), `.accent-blue` (bleu-confiance)
- **Fonds icones** : `.bg-sage`, `.bg-teal`, `.bg-peach`, `.bg-lavender` — pastels assortis
- **Responsive** : les cartes passent de `min-height: 260px` (desktop) a `140px` (mobile), avec titre/icone/fleche reduits proportionnellement
- **Liens** : chaque carte mene vers la page services ou marques correspondante
- **Hover** : translateY(-4px) + shadow + fleche glisse a droite + fond chaud unique par carte :
  - `.card--naturels` : olive-sage `#C5D08C`
  - `.card--dermo` : vert-menthe `#9DCCAE`
  - `.card--complements` : miel-peche `#E9B870`
  - `.card--medical` : lavande `#ADA5D7`

### Marquee banner
- Defilement infini CSS (`@keyframes marquee` translateX 0 -> -50%)
- Contenu duplique pour boucle seamless
- Pause au hover
- Items : Ordonnances, Vaccinations, Produits naturels, Livraison, Cosmetiques, Automedication, Conseil, Phytotherapie

### Editorial layouts
- Grille 2 colonnes desktop (1fr 1fr), 1 colonne mobile
- `.editorial-grid.reverse` inverse l'ordre via `direction: rtl` (pas de `order` CSS)
- Chaque section a : label uppercase, titre Fraunces, paragraphe, link-arrow avec fleche animee
- Image avec zoom subtil au hover (scale 1.03)

### Promise pills
- Flexbox wrap centre
- Icones SVG inline + texte
- Hover : translateY(-2px) + changement de fond

### Auto-fetch blog article (JS)
- **Comment ca marche** : au chargement, JS fait `fetch('../blog.html')`, parse le HTML avec `DOMParser`, extrait le premier `.blog-card`
- **Donnees extraites** : titre (`.blog-title`), extrait (`.blog-excerpt`), date (`.blog-date`), image (`.blog-image-placeholder img`), lien (premier `<a>`)
- **Injection** : via `getElementById` sur les placeholders dans le HTML
- **Fallback** : le contenu du dernier article est code en dur dans le HTML (titre, date, extrait, image). Si le fetch echoue (ex: mode `file://` local, CORS), le contenu par defaut s'affiche correctement
- **Pour mettre a jour** : ajouter un nouvel article en haut de blog.html. Sur le serveur, la homepage se met a jour automatiquement. En local, mettre a jour les valeurs par defaut dans le HTML

### Brand Spotlight (JS)
- **Comment ca marche** : un tableau JS contient 9 marques (nom, categorie, tagline, description, chemin logo, lien page). Au chargement, `Math.random()` en selectionne une aleatoirement
- **Marques incluses** : Bioderma, Nuxe, Avene, La Roche-Posay, Klorane, Vichy, Caudalie, Biocanina, Biogaran
- **Donnees par marque** : `name`, `category`, `tagline`, `description`, `logo` (chemin vers `logos/`), `page` (lien vers `../Nos-marques/`)
- **Pour ajouter une marque** : ajouter un objet dans le tableau `brands` du JS + placer le logo dans `logos/`
- **Rotation** : aleatoire a chaque chargement de page

### Scroll animations
- IntersectionObserver avec `threshold: 0.1`
- Classe `.fade-up` : opacity 0, translateY(30px) -> visible
- Stagger via `.stagger-1` a `.stagger-6` (delay 0.1s increments)
- Observer unobserve apres premiere apparition (animation one-shot)

---

## Responsive (mobile-first)

| Element | Mobile | Desktop (1024px+) |
|---|---|---|
| Hero image | `display: none` | `display: block` |
| Hero content | Centre, text-align center | Aligne gauche |
| Hero CTA | Centre | Flex-start |
| Hero padding | 104px top / 48px bottom | 120px top / 64px bottom |
| Hero min-height | Auto | Auto (plus de 100vh) |
| Product feature cards | 2 colonnes, 140px min-height, taille reduite | 4 colonnes, 260px min-height |
| Nav links | Cache (hamburger) | Flex visible |
| Categories grid | 2 colonnes | 6 colonnes |
| Services grid | 1 colonne | 3 colonnes |
| Editorial grid | 1 colonne | 2 colonnes |
| Brand spotlight grid | 1 colonne | 2 colonnes |
| Footer grid | 2 colonnes (Contact + Horaires cote a cote), Navigation cachee | 4 colonnes |

**Footer mobile compact :**
- Navigation (`.footer-nav`) : `display: none` sur mobile
- Contact et Horaires : grid 2 colonnes cote a cote via `grid-template-areas`
- Padding reduit : `--space-48` au lieu de `--space-80`
- Polices reduites : `--text-sm` au lieu de `--text-base`
- Icones sociales : 40px au lieu de 44px

**Decision sur le hero :** le hero n'utilise plus `min-height: 100vh` — il se dimensionne naturellement a son contenu pour eviter un grand espace vide. L'image disparait completement en mobile (`display: none`). Pas de stacking sous le texte — decision deliberee pour garder le hero compact et focus sur le texte + CTA.

**Images en mobile (< 768px) :**
- Editorial images : aspect-ratio passe de 4/3 a 3/2 (< 480px : 1/1 avec max-height 280px)
- Brand spotlight logo : padding et taille max reduits
- Category images : 60px (< 480px : 48px) au lieu de 80px
- Sections : padding vertical reduit de `--space-96` a `--space-64`

---

## SEO et meta

- **Schema.org** : `@type: Pharmacy` avec adresse, telephone, horaires, coordonnees GPS, note Google aggregate
- **Open Graph + Twitter Cards** : titre, description, image du logo
- **Canonical** : `https://www.pharmaciecharnal.fr/index.html`
- **Google Analytics** : gtag.js avec ID `G-2Q64V6B0QE`

---

## Animations et transitions

| Element | Effet | Duration | Easing |
|---|---|---|---|
| Scroll elements | fadeInUp (opacity + translateY) | 0.6s | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Hero elements | fadeInUp staggered (0s, 0.1s, 0.2s, 0.3s, 0.4s) | 0.6-0.8s | idem |
| Buttons hover | scale(1.02) + box-shadow | 250ms | idem |
| Cards hover | translateY(-4px) + shadow-lg | 250ms | idem |
| Link arrows | gap increase + svg translateX | 250ms | idem |
| Editorial images | scale(1.03) on hover | 0.8s | idem |
| Marquee | translateX infini | 30s linear | linear |
| Blog image | opacity 0 -> 1 on load | 0.4s | ease |
| Mobile menu | slideDown (opacity + translateY) | 400ms | idem |

**Easing global** : `cubic-bezier(0.16, 1, 0.3, 1)` — c'est l'easing signature HIMS, un ease-out tres prononce qui donne un mouvement "naturel et precis".

---

## Shadows

Systeme de shadows tres subtiles (opacite 0.04 a 0.12), fidele a HIMS :
- `--shadow-xs` : 0 1px 2px rgba(0,0,0,0.04)
- `--shadow-sm` : 0 2px 8px rgba(0,0,0,0.06)
- `--shadow-md` : 0 4px 12px rgba(0,0,0,0.08)
- `--shadow-lg` : 0 8px 24px rgba(0,0,0,0.10)
- `--shadow-xl` : 0 12px 32px rgba(0,0,0,0.12)

Les boutons teal utilisent une shadow teintee : `rgba(45, 95, 93, 0.25)`.

---

## Arborescence des images

Les images sont referencees depuis le dossier parent `images/` (relatif a l'emplacement du site) :
- `images/pharmacie-charnal-logo.png` — logo (nav + footer)
- `images/Pharmacie Charnal Queven vectorielle.jpg` — hero
- `images/medicaments.jpg` — categorie medicaments
- `images/hygiene-bucodentaire.jpg` — categorie hygiene
- `images/produits-cosmetiques.jpg` — categorie cosmetiques
- `images/produits-bebe.jpg` — categorie bebe
- `images/complements-alimentaires.jpg` — categorie complements
- `images/premiers-soins.jpg` — categorie premiers soins
- `images/Detox en Janvier.jpeg` — image par defaut du dernier article blog
- Image du blog : codee en dur (fallback) + mise a jour dynamique via JS fetch `../blog.html`

**Logos marques** (dans `logos/`) :
- `logos/Bioderma.png`, `logos/Nuxe.jpeg`, `logos/Avene.jpeg`, `logos/La-roche-posay.png`, `logos/Klorane.png`, `logos/Vichy.png`, `logos/Caudalie.png`, `logos/Biocanina.png`, `logos/biogaran_logo.jpg`
- Source originale : `/Nos-marques/logos/` — copies dans `index-redesign/logos/` pour fonctionnement local

**Note sur les chemins :** le dossier `images/` et `logos/` sont des copies locales dans `index-redesign/` pour garantir le fonctionnement en mode `file://` local (les liens symboliques ne fonctionnent pas avec le protocole `file://`). Le fetch blog utilise `../blog.html` (repertoire parent). Les liens vers les pages marques utilisent `../Nos-marques/`.

---

## Ton et voix

- **Chaleureux et professionnel** : pas le ton clinique d'un hopital, pas le ton trendy d'un HIMS
- **Familial** : "pharmacie familiale", "tradition", "depuis plus de 40 ans"
- **Confiance** : "pharmaciens diplomes", "conseil confidentiel", "100% conseil personnalise"
- **Proximite** : "au coeur de Queven", "votre pharmacien", "notre equipe"
- **Langue** : francais, pas d'anglicismes sauf termes techniques CSS/JS
- Vouvoiement (politesse francaise standard pour un commerce de sante)

---

## Dependances externes

- **Google Fonts** : Fraunces + DM Sans (preconnect + CSS link)
- **Google Analytics** : gtag.js (G-2Q64V6B0QE)
- **Aucun framework CSS/JS** : tout est vanilla, zero dependance npm/CDN
- **Pas de jQuery, pas de Bootstrap, pas de Tailwind** — CSS custom pur

---

## Fichiers de reference

- **Design system HIMS** : `/Pharma/Pharma online/articles pour futur pages/Hims website codes/hims-design-complete.md`
- **Charte graphique Charnal** : `/Pharma/Charte-Graphique/CHARTE_GRAPHIQUE_PHARMACIE_CHARNAL.md`
- **Page d'origine** : `/Pharma/Pharma online/website-pharmacie-charnal/index.html`
- **Page blog** : `/Pharma/Pharma online/website-pharmacie-charnal/blog.html`

---

## Decisions de design a retenir

1. **Teal, pas noir** : tous les CTAs et elements d'accentuation sont en `--teal-pro` (#2D5F5D), jamais en noir. Le noir est trop dur pour une pharmacie familiale.
2. **Hero compact** : plus de `min-height: 100vh`. Le hero se dimensionne a son contenu avec un padding serre (120px top, 64px bottom desktop). L'image disparait en mobile (`display: none`), pas de stacking.
3. **Product feature cards (style HIMS)** : rangee de 4 cartes categories juste apres le marquee, inspirees des cartes produits hims.com. 2 colonnes en mobile avec taille reduite (140px), 4 colonnes en desktop (260px). Chaque carte a un titre avec accent colore + chevron + icone SVG sur fond pastel.
4. **Blog : fallback en dur + auto-fetch** : le dernier article est code en dur dans le HTML (image, titre, date, extrait) pour fonctionner en local. Le JS tente un fetch `../blog.html` pour mettre a jour automatiquement sur le serveur.
5. **Pas de framework** : site statique pur HTML/CSS/JS vanilla. Aucune build step. Editable directement.
6. **Direction RTL pour reverse grid** : les layouts editoriaux inverses utilisent `direction: rtl` plutot que CSS `order` — plus simple et plus fiable.
7. **Optical sizing Fraunces** : la police Fraunces utilise l'axe `opsz` (optical size 9-144) qui ajuste automatiquement les details selon la taille. A petite taille les traits s'epaississent, a grande taille ils s'affinent.
8. **"Pourquoi nous choisir" deplace vers contact.html** : la section bento grid a ete retiree de la homepage et ajoutee sur la page contact, visible uniquement en mobile (max-width: 768px), juste au-dessus de la carte Google Maps. 3 cartes : 01 Experience, 02 Equipe, 03 Approche naturelle (grille 2 colonnes mobile).
9. **Note Google a 4.9** : mise a jour de la note de 4.8 a 4.9 dans le schema.org, la rating strip et les stats.
10. **Navigation font-size** : liens nav passes de `--text-sm` a `--text-base` pour meilleure lisibilite.
11. **Product feature cards : icones alignees** : ajout de `min-height` sur `.product-feature-header` pour que les zones d'icones aient la meme hauteur sur toutes les cartes, meme quand un titre passe sur 2 lignes.
12. **Automedication au lieu de Materiel medical** : la categorie "Materiel medical" a ete remplacee par "Automedication" (conseils douleurs, rhume, digestion, premiers soins). Icone : pilule SVG.
13. **Footer mobile compact** : sur mobile (< 768px), la colonne Navigation est cachee, Contact et Horaires sont cote a cote (grid 2 colonnes), et le padding/espaces sont reduits pour un footer moins imposant.

---

## TODO / Ameliorations futures

- [x] ~~Ajuster les chemins relatifs~~ — images et logos copies localement, fetch blog ajuste a `../blog.html`
- [ ] Optimiser les images (WebP, srcset, lazy loading)
- [ ] Ajouter un favicon SVG dedie au redesign si different
- [ ] Tester sur tous les navigateurs (Safari, Firefox, Chrome, Edge)
- [ ] Tester le mode sombre (pas implemente, a considerer)
- [ ] Ajouter des micro-interactions sur les categories cards (ex: icone animee)
- [ ] Ajouter les marques sans logo au brand spotlight (Arkopharma, PiLeJe, Boiron, Ducray, Mustela, etc.)
- [ ] Envisager un systeme de blog JSON au lieu du fetch HTML si le site grandit
