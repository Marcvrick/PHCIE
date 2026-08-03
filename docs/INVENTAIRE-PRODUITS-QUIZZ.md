# Inventaire photo des produits des quiz

Référence de tous les produits recommandés par les 4 quiz du site, pour suivre la création des **photos produit** (une photo par produit). À date, **aucune photo n'est créée** — cette page est la liste de travail.

**Total : 65 produits** — Dermocosmétique 3 · Automédication 42 · Produits naturels 15 · Compléments 5.

**Source :** extrait du JS de chaque quiz (`Quizzes/quiz-*.html`), champs `name` + `brand`.

**Avancement photos : 0 / 65**

---

## Convention photo

- **Dossier cible :** `images/quiz-produits/`
- **Nom de fichier :** `{quiz}-{slug}.png` (ex. `soin-peau-hydrance-riche.png`) — slug donné dans la colonne « Slug photo » ci-dessous
- **Format :** PNG transparent (RGBA), fond retiré avec `rembg[cpu]` — même style que les badges homepage (`images/naturels-product.png`, `images/dermocosmetique-product.png`, etc.)
- **Cadrage :** produit centré, square ~1000 px, pas d'ombre dans l'image (l'ombre portée elliptique est ajoutée en CSS côté site)
- **État colonne :** ☐ à faire · ✅ fait (mettre à jour cette page au fur et à mesure)

> Workflow : photo brute → `rembg i input.jpg output.png` (vérifier le mode RGBA) → renommer en `{slug}.png` → déposer dans `images/quiz-produits/` → cocher ✅ ici.

---

## 1. Dermocosmétique — `quiz-soin-peau.html` (3)

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Hydrance Riche | AVENE | `soin-peau-hydrance-riche` | ☐ |
| Gel-Crème Oil Control SPF25 | CERAVE | `soin-peau-gel-creme-oil-control` | ☐ |
| Pigmentbio Daily Care SPF50+ | BIODERMA | `soin-peau-pigmentbio-daily-care` | ☐ |

---

## 2. Automédication — `quiz-automedication.html` (42)

### BIOGARAN CONSEIL (génériques) — 23

| Produit | Équivalent connu | Slug photo | État |
|---|---|---|---|
| Paracétamol 1000 mg | Doliprane | `automed-paracetamol-1000` | ☐ |
| Ibuprofène 400 mg | Advil | `automed-ibuprofene-400` | ☐ |
| Cétirizine 10 mg | Zyrtec | `automed-cetirizine-10` | ☐ |
| Pastilles Amylmétacrésol | Lysopaïne | `automed-pastilles-amylmetacresol` | ☐ |
| Collutoire Spray | Hexaspray | `automed-collutoire-spray` | ☐ |
| Macrogol 10 g | Forlax | `automed-macrogol-10` | ☐ |
| Lopéramide 2 mg | Imodium | `automed-loperamide-2` | ☐ |
| Métopimazine 7,5 mg | Vogalib | `automed-metopimazine` | ☐ |
| Phloroglucinol 80 mg | Spasfon | `automed-phloroglucinol-80` | ☐ |
| Oméprazole 20 mg | Mopral | `automed-omeprazole-20` | ☐ |
| Oxomémazine Sirop | Toplexil | `automed-oxomemazine-sirop` | ☐ |
| Carbocistéine Sirop 5% | Bronchokod | `automed-carbocisteine-sirop-5` | ☐ |
| Trolamine 0,67% Émulsion | Biafine | `automed-trolamine-emulsion` | ☐ |
| Chlorhexidine Spray | Biseptine | `automed-chlorhexidine-spray` | ☐ |
| Levure Saccharomyces boulardii | Ultra-Levure | `automed-levure-boulardii` | ☐ |
| Alginate de Sodium/Bicarbonate | Gaviscon | `automed-alginate-sodium-bicarbonate` | ☐ |
| Chlorhexidine Bain de Bouche | Eludril | `automed-chlorhexidine-bain-de-bouche` | ☐ |
| Racécadotril 100 mg | Tiorfan | `automed-racecadotril-100` | ☐ |
| Macrogol 4 g Enfant | Forlax enfant | `automed-macrogol-enfant` | ☐ |
| Paracétamol Sirop Pédiatrique | Doliprane sirop | `automed-paracetamol-sirop-enfant` | ☐ |
| Ibuprofène Sirop Enfant | Advil sirop | `automed-ibuprofene-sirop-enfant` | ☐ |
| Carbocistéine Sirop Enfant 2% | Bronchokod enfant | `automed-carbocisteine-sirop-enfant` | ☐ |
| Alpha-amylase Sirop | Maxilase générique | `automed-alpha-amylase-sirop` | ☐ |

### UPSA — 13

| Produit | Slug photo | État |
|---|---|---|
| Efferalgan 1000 mg | `automed-efferalgan-1000` | ☐ |
| Dafalgan 1000 mg | `automed-dafalgan-1000` | ☐ |
| Aspirine UPSA Vitamine C | `automed-aspirine-upsa-vit-c` | ☐ |
| Fervex État Grippal | `automed-fervex-etat-grippal` | ☐ |
| Mucomyst 200 mg | `automed-mucomyst-200` | ☐ |
| Oxomémazine UPSA | `automed-oxomemazine-upsa` | ☐ |
| Phytovex Maux de Gorge Spray | `automed-phytovex-maux-de-gorge` | ☐ |
| Smecta 3 g | `automed-smecta-3` | ☐ |
| Smecta Enfant | `automed-smecta-enfant` | ☐ |
| Donormyl 15 mg | `automed-donormyl-15` | ☐ |
| UPSA Vitamine C 1000 mg | `automed-upsa-vitamine-c-1000` | ☐ |
| UPSA Acérola 1000 Bio | `automed-upsa-acerola-1000-bio` | ☐ |
| Efferalgan Pédiatrique Sirop | `automed-efferalgan-pediatrique` | ☐ |

### SANOFI / OPELLA — 4

| Produit | Slug photo | État |
|---|---|---|
| Maalox Maux d'Estomac | `automed-maalox` | ☐ |
| Dulcolax 5 mg | `automed-dulcolax-5` | ☐ |
| Maxilase Comprimés | `automed-maxilase-comprimes` | ☐ |
| Maxilase Sirop | `automed-maxilase-sirop` | ☐ |

### BOIRON — 1

| Produit | Slug photo | État |
|---|---|---|
| Homéogène 9 | `automed-homeogene-9` | ☐ |

### SUR ORDONNANCE — 1

| Produit | Slug photo | État |
|---|---|---|
| Cétirizine Gouttes Pédiatriques | `automed-cetirizine-gouttes-pediatriques` | ☐ (photo facultative — non vendu en OTC) |

---

## 3. Produits naturels — `quiz-produits-naturels.html` (15)

### Sommeil

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Valériane Bio | NAT&FORM | `naturels-valeriane-bio` | ☐ |
| Sommeil Triple Action | PHYTOSUN ARÔMS | `naturels-sommeil-triple-action` | ☐ |
| SOM•ACTIFS | ARAGAN | `naturels-som-actifs` | ☐ |

### Stress

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Rhodiola Bio | NAT&FORM | `naturels-rhodiola-bio` | ☐ |
| Stress Triple Action | PHYTOSUN ARÔMS | `naturels-stress-triple-action` | ☐ |
| SEREN•ACTIFS | ARAGAN | `naturels-seren-actifs` | ☐ |

### Défenses naturelles

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Échinacée Bio | NAT&FORM | `naturels-echinacee-bio` | ☐ |
| Aromadoses Défenses Naturelles | PHYTOSUN ARÔMS | `naturels-aromadoses-defenses` | ☐ |
| IMMUN•ACTIFS | ARAGAN | `naturels-immun-actifs` | ☐ |

### Digestion

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Artichaut Bio | NAT&FORM | `naturels-artichaut-bio` | ☐ |
| Aromadoses Digestion Transit | PHYTOSUN ARÔMS | `naturels-aromadoses-digestion` | ☐ |
| BIOTIC•P7 ENTÉRO | ARAGAN | `naturels-biotic-p7-entero` | ☐ |

### Nez & Gorge

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Thym Bio | NAT&FORM | `naturels-thym-bio` | ☐ |
| Aromadoses Nez & Gorge | PHYTOSUN ARÔMS | `naturels-aromadoses-nez-gorge` | ☐ |
| RHIN•ACTIFS BIO | ARAGAN | `naturels-rhin-actifs-bio` | ☐ |

---

## 4. Compléments alimentaires — `quiz-complement.html` (5)

| Produit | Marque | Slug photo | État |
|---|---|---|---|
| Lactibiane Référence | PiLeJe | `complement-lactibiane-reference` | ☐ |
| Formag | PiLeJe | `complement-formag` | ☐ |
| Chronobiane LP | PiLeJe | `complement-chronobiane-lp` | ☐ |
| D3 Biane Spray 1000 UI | PiLeJe | `complement-d3-biane-spray` | ☐ |
| Curcuma Bio | Nat&Form | `complement-curcuma-bio` | ☐ |

---

## Branchement côté site (quand les photos existeront)

- Les cartes résultat des quiz (`Quizzes/quiz-*.html`) affichent actuellement un emoji (`p.emoji`). Remplacer par `<img src="../images/quiz-produits/{slug}.png">` quand la photo est prête.
- La page hub `Quizzes/guide-quizzes-sante-pharmacie-queven.html` utilise déjà des photos produit par catégorie (`images/{categorie}-product.png`) — ne pas confondre avec les photos par produit de cet inventaire.
- Garder le `alt` descriptif (nom produit + marque).

## Maintenance

- Cette liste est générée à partir du JS des quiz. Quand un quiz ajoute/retire un produit, **mettre à jour cette page** et ajuster le total.
- Relecture : vérifier que chaque `name`/`brand` du JS a une ligne ici.
