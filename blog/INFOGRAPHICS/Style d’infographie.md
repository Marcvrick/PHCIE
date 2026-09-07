# Style d’infographie: poster éditorial autour d’un sujet

Référence: deux posters (grenouille *Rana Dardo Dorado* ; poisson *Hábitat Plástico*). Même famille visuelle, deux températures.

---

## Ce que ces images ont en commun

Ce n’est pas un dashboard, pas un carrousel Instagram, pas une illustration. C’est une **page magazine verticale**: un grand sujet photographié, découpé, posé sur du papier, et autour de lui des **cartes de faits**.

### Architecture

1. **Le sujet est le centre.** Animal, objet, plante, organe: une photo réaliste, découpée sur fond uni, grande, nette. Le reste de l’affiche gravite autour. On peut parfois le montrer deux fois (gros plan + second angle plus petit).
2. **Format portrait**, type page A3 / A4. Marge crème ou blanche. Pas de fond photo, pas de sous-bois, pas de texture 3D.
3. **Titre en haut, centré ou calé à gauche.** Très gros. Une ligne scientifique ou un kicker juste dessous. Puis 1 à 2 phrases d’intro, petites.
4. **Information en modules.** Chaque fait vit dans sa propre boîte: carte à bord fin, pastille icône, bulle, mini-carte, pastille de couleur, pictogramme. Pas de longs paragraphes libres.
5. **Une seule couleur d’accent** pour tout le système (titres secondaires, fonds de cartes, chiffres clés, filets). Le reste est crème / blanc / charcoal / gris.
6. **Hybride photo + icône + donnée.** Photo réaliste du sujet + pictos plats + mini-viz (barre, pictogrammes de personnes, bouteilles, camions, carte silhouette). Jamais tout illustré, jamais tout photo.
7. **Chiffres géants** comme points d’accroche: `55 mm`, `+10`, `84.5%`, `100%`. On lit d’abord le nombre, ensuite la légende.
8. **Bas de page = conclusion.** Famille / taxonomie, ou “du problème à la solution” en 3 étapes numérotées. L’affiche a un début (titre), un milieu (faits autour du sujet), une fin.

### Typographie

- Titre: serif ou sans condensé, très gras, très grand.
- Kicker / nom latin: petites capitales, couleur d’accent.
- Corps: sans-serif étroit, corps petit mais lisible, gris anthracite.
- Mots importants en gras ou dans la couleur d’accent, jamais tout le bloc en couleur.
- Source en tout petit, coin supérieur droit.

### Couleur: deux variantes du même système

| Variante | Fond | Accent | Usage |
|---|---|---|---|
| Encyclopédie / spécimen | Crème chaud `#FAF6EB` | Or / moutarde | Nature, espèce, fiche pédagogique |
| Enquête / alerte | Blanc froid | Rouge unique | Danger, statistique, santé publique |

Dans les deux cas: **une** accent, pas un arc-en-ciel. Les cartes jaunes (grenouille) ou le overlay rouge du poisson sont la même idée: la couleur d’accent *colore le sujet ou les cartes*, elle ne décore pas.

### Objets visuels qui reviennent

- Photo découpée du sujet (parfois recouverte d’un voile de la couleur d’accent, comme le poisson moitié gris / moitié rouge)
- Cartes à coins légèrement arrondis, filet fin or ou gris
- Pictos line-art dans un carré (os, crâne, nuage, cœur, os)
- Comparaison d’échelle (trombone, pièce, main)
- Mini-carte géographique + pastille de lieu
- Nuancier (3 ronds de couleur)
- Pictogrammes quantitatifs (10 silhouettes humaines, 5 bouteilles)
- Formule / schéma simple dans un encadré
- Bulle ronde type “!” pour l’avertissement
- Lignes de rappel (leader lines) du chiffre vers une zone du sujet
- Barres horizontales de ranking
- Bandeau noir pour un titre de section
- Drapeaux / icônes de pays
- Frise 1-2–3 en pied de page

### Densité

Riche, pas vide. On scanne en 3 secondes (titre + sujet + 2 gros chiffres) et on peut lire 8 à 12 micro-faits si on s’arrête. Les cartes ne se chevauchent pas. Le sujet photo peut passer *devant* ou *entre* les cartes, jamais dessus un texte.

### Ce que ce style n’est pas

- Pas de fond forestier / ambiance photo
- Pas de mascotte cartoon
- Pas de mockup d’écran, pas d’UI
- Pas de 3D isométrique
- Pas de 6 couleurs d’accent
- Pas de texte collé jusqu’aux bords

---

## Prompt générique

Remplacer les blocs entre `[CROCHETS]`. Garder le reste tel quel. Une infographie = un sujet, une couleur d’accent, une langue, une liste courte de faits.

```
Editorial magazine infographic poster, portrait A3, printed-paper look.

A large photorealistic cutout of [SUJET] sits in the center of a plain [FONDS: warm cream paper OR cold white] background, like a specimen on a museum page. The subject is sharp, well-lit, isolated, not in a scene. Around it, many small self-contained fact cards with thin borders. The subject can overlap empty space between cards but never covers text.

One accent color only: [COULEUR D’ACCENT, ex. mustard gold #E4B51C OR alert red #E03A2D OR pharmacy teal #2D5F5D]. Use it for section headers, card fills, key numbers, thin decorative rules, and optional overlay on part of the subject. Everything else is cream/white, charcoal, and muted gray.

Typography: huge title at the top "[TITRE]", a small kicker in accent color "[SOUS-TITRE / NOM LATIN]", then a two-line intro. Body text in a clean narrow sans-serif, dark charcoal, high contrast, large enough to read. Giant numbers as visual hooks. Perfect spelling in [LANGUE]. No extra words, no invented statistics, no English unless the language is English. Source line in tiny gray at the top right: "[SOURCE]".

Layout, top to bottom:
1) Title block.
2) A ring of 6 to 10 modules around the hero: icon+label cards, one mini-map, one size comparison, one color/attribute chip row, two giant stats, one warning bubble. Each module = one fact from the list below.
3) The hero cutout of [SUJET], large.
4) Bottom band: either a taxonomy/family box, or a 3-step "what to do" row with numbered circular icons.

Visual devices allowed: flat line icons, pictograms (people, objects), mini silhouette map, horizontal ranking bars, leader lines from a number to a part of the subject, a round "!" callout, a second smaller photo of the same subject in a corner. Hybrid of photography + flat icons + simple data. Not a cartoon, not a dashboard, not a photo collage, not isometric 3D.

Facts to place, exactly these, one per card — do not add others:
- [FAIT 1]
- [FAIT 2]
- [FAIT 3]
- [FAIT 4]
- [FAIT 5]
- [FAIT 6]
- [FAIT 7]
- [STAT GÉANTE, ex. "1 320"]
- [AVERTISSEMENT COURT]
- [PIED DE PAGE / MARQUE]

Generous margins. Cards aligned to an invisible grid. No watermarks, no QR code, no logos except [MARQUE SI BESOIN].
```

---

## Comment remplir

| Placeholder | Règle |
|---|---|
| `SUJET` | Un objet reconnaissable au centre (amanite, panier, foie, flacon…). Un seul. |
| `FONDS` | Crème = pédagogique. Blanc = alerte / data. |
| `COULEUR D’ACCENT` | Une. Or = nature. Rouge = danger. Teal Charnal `#2D5F5D` = pharmacie. |
| `FAITS` | 6 à 10 max. Une idée par ligne. Chiffre + 8 mots, pas une phrase d’article. |
| `STAT GÉANTE` | Le nombre qu’on doit voir à 2 mètres. |
| `LANGUE` | Tous les libellés dans cette langue, écrits déjà corrects dans le prompt. |

Moins de cartes = plus lisible. Si le texte sort tordu, régénérer avec **moins de faits**, pas plus d’instructions.

---

## Mini-exemple (champignons, variante alerte)

```
SUJET: a photorealistic Amanita phalloides (death cap), green-olive cap, white gills, ring, volva at the base, cutout
FONDS: cold white
COULEUR: alert red #C0673C plus charcoal
TITRE: Champignons
SOUS-TITRE: Bretagne — bien les reconnaître
STAT GÉANTE: 1 320
LANGUE: French
```
