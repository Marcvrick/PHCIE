# Quiz Builder — Pharmacie Charnal

Guide pour Claude : comment construire un quiz produit pour le site Pharmacie Charnal.

---

## Principe fondamental

**Chaque quiz vend des produits que la pharmacie a en stock.**

On ne recommande jamais un produit "populaire" au hasard. On part de l'inventaire reel, on identifie les produits a ecouler (surstock, dormants, rotation lente), et on construit un quiz dont les resultats pointent vers ces produits.

L'objectif est double :
1. **Ecouler le stock** — en priorite les produits en surstock ou dormants
2. **Conseiller le client** — le quiz doit rester pertinent et honnete, jamais forcer un produit inadapte

---

## Workflow complet

### Etape 1 — Choisir une categorie

Identifier la categorie de produits visee. Categories disponibles dans l'inventaire :

| Categorie | Description | Marques principales |
|-----------|-------------|---------------------|
| Hydratation visage | Cremes, baumes, soins jour/nuit | Avene, Bioderma, CeraVe, La Roche-Posay, Nuxe |
| Nettoyage / Demaquillage | Eaux micellaires, gels moussants, laits | Bioderma, Avene, CeraVe, Nuxe, La Roche-Posay |
| Reparation cutanee | Cicalfate, Cicaplast, Cicabio | Avene, La Roche-Posay, Bioderma |
| Protection solaire | SPF50+, apres-soleil, sticks | Bioderma, Avene, La Rosee, Nuxe, La Roche-Posay |
| Anti-age | Serums, cremes anti-rides, eclat | Avene, Nuxe, Bioderma |
| Anti-imperfections / Acne | Sebium, Cleanance, Effaclar | Avene, Bioderma, CeraVe, La Roche-Posay |
| Hygiene corporelle | Gels douche, deodorants | Nuxe, La Rosee |
| Capillaire | Shampoings, soins, masques | Klorane, Nuxe |
| Complements alimentaires | Probiotiques, vitamines, mineraux | PiLeJe, Nat&Form, Aragan |

### Etape 2 — Analyser le stock

**Source des donnees :**
```
/Pharma/GESTION/0-MANAGEMENT/Analyse des ventes/
  Analyse des ventes par Marque/
    Analyse ventes Parapharmacie 2025/
```

**Fichiers par marque :**
- `AVENE.md`, `BIODERMA.md`, `CERAVE.md`, `LAROCHE_POSAY.md`, `NUXE.md`
- `La Rosee/LA ROSEE.md`, `Thuasne/THUASNE.md`
- `BIODERMA-SOLAIRES-2025.md` (solaires specifiquement)
- `SYNTHESE-EXECUTIVE-Parapharmacie.md` (vue d'ensemble)

**Metriques cles a regarder :**

| Metrique | Ce que ca veut dire | Seuil d'alerte |
|----------|---------------------|----------------|
| Ventes 12M | Unites vendues sur 12 mois | < 5/an = candidat au delistage |
| Stock | Unites en stock actuellement | — |
| Couverture stock (mois) | Stock / (Ventes 12M / 12) | > 8 mois = surstock |
| Rotation | Nombre de fois que le stock tourne par an | < 0.7x = stock dormant |
| Statut | OK, Rupture, Surstock | "Surstock" = cible prioritaire |

**Processus de selection :**

1. Ouvrir le fichier de la marque correspondant a la categorie
2. Filtrer les produits de la categorie visee (ex: soins visage)
3. Trier par couverture stock decroissante (les plus en surstock d'abord)
4. Selectionner **3 a 5 produits** qui repondent a des **besoins differents** (ex: peau seche vs grasse vs mixte)
5. Verifier que chaque produit est pertinent pour au moins un profil client credible

**Regle : ne jamais recommander un produit en rupture.** Verifier la colonne "Statut" — si "Rupture", exclure.

### Etape 3 — Comprendre les specs de chaque produit

**Sources produit :**
```
/Pharma/GESTION/1-RESSOURCES/
  Fiche par Marque/Cosmetiques/{MARQUE}/    — fiches marque detaillees
  Spec produits/                            — specs techniques
  Fiches Conseil/                           — guides conseil client
  Académie Conseil - Phie Charnal/Leçons/   — lecons par theme
```

**Lecons dermocosmétiques (chapitre 5) :**
- `Leçon-5.1-Comprendre-Types-Peau.md` — types de peau et identification
- `Leçon-5.2-BIODERMA-Les-Essentiels.md` — gammes Bioderma
- Autres lecons : La Roche-Posay, Klorane, Nuxe, La Rosee

**Lecons complements alimentaires (chapitre 6) :**
- `Leçon-6.1-Introduction-Complements-Alimentaires.md`
- PiLeJe, Nat&Form, Aragan

**Pour chaque produit selectionne, documenter :**

| Champ | Exemple |
|-------|---------|
| Nom complet | AVENE Hydrance Riche Creme Hydratante 40ml |
| Marque | Avene |
| Gamme | Hydrance |
| Type de peau | Peau seche a tres seche |
| Actifs cles | Eau thermale d'Avene, Lipides restructurants |
| Benefice principal | Hydratation intense 24h, reconstitue la barriere |
| Texture | Creme riche, onctueuse |
| SPF | Non |
| Prix approx. | ~15€ |
| Stock actuel | 18 unites |
| Pourquoi en surstock | Couverture 12.7 mois, rotation lente |

### Etape 4 — Construire les questions

**Principe : chaque question doit differencier les profils clients pour orienter vers le bon produit.**

Le quiz doit avoir **5 questions** (maximum 6). Plus = abandon.

**Structure recommandee :**

| # | Theme de la question | Ce qu'elle discrimine |
|---|---------------------|----------------------|
| Q1 | Type de peau / etat general | Segmentation primaire (seche, grasse, mixte, sensible) |
| Q2 | Problematique principale | Besoin dominant (hydratation, imperfections, eclat, protection) |
| Q3 | Preference texture / routine | Confort d'usage (leger vs riche, minimaliste vs complet) |
| Q4 | Facteur environnement | Exposition solaire, pollution, saison, interieur/exterieur |
| Q5 | Style de vie / contrainte | Budget, temps disponible, sensibilite ingredients |

**Scoring :**

Chaque reponse attribue des points a chaque produit (0 a 3).

```
Exemple avec 3 produits (A, B, C) :

Q1 "Quel est votre type de peau ?"
  - "Seche, tiraillements"       → A: 3, B: 0, C: 1
  - "Grasse, brillances"         → A: 0, B: 3, C: 1
  - "Mixte, un peu des deux"     → A: 1, B: 1, C: 2
  - "Sensible, rougeurs"         → A: 2, B: 0, C: 2
```

**Regles de scoring :**
- Le score maximum theorique doit etre atteignable pour chaque produit
- Chaque produit doit etre "gagnant" pour au moins un profil coherent
- Eviter les ex aequo frequents — si 2 produits ont presque toujours le meme score, fusionner ou differencier davantage les questions
- En cas d'egalite parfaite : privilegier le produit le plus en surstock

### Etape 5 — Construire la page HTML

**Design system obligatoire :** suivre `index-redesign/README.md`.

Regles non-negociables :
- **Fraunces** pour les titres (font-display), **DM Sans** pour le corps (font-body)
- **`--teal-pro: #2D5F5D`** comme couleur primaire partout — boutons, liens, badges, progress bar
- **Pas de gradients** sur les boutons — fond plat teal-pro
- **`border-radius: var(--radius-base)` (8px)** pour les boutons — pas de pill (radius-full)
- **`.highlight`** = `color: var(--teal-pro); font-style: italic;` pour les mots-cles dans les titres
- **`cubic-bezier(0.16, 1, 0.3, 1)`** pour tous les easings
- **Fond `--cream: #FFFEF9`** pour le body
- **Footer charcoal `#1F2121`**
- **Espacement grille 8pt** (var(--space-8), --space-16, --space-24, etc.)
- **Ombres subtiles** (0.04 a 0.12 d'opacite)
- **Fonds pastel** pour les cartes produit : `--pastel-sage`, `--pastel-teal`, `--pastel-peach`

**Structure HTML du quiz :**
```
<!DOCTYPE html>
<html lang="fr">
  <head>
    Fonts Google (Fraunces + DM Sans)
    CSS avec toutes les variables du design system
  </head>
  <body>
    <header>  Logo Pharmacie Charnal  </header>
    <progress-bar>  "Question X sur 5"  </progress-bar>

    <step id="intro">
      Badge "Quiz gratuit · 2 min"
      Titre avec .highlight
      3 features (icone + texte)
      Bouton "Commencer"
    </step>

    <step id="q1"> ... </step>
    <step id="q2"> ... </step>
    <step id="q3"> ... </step>
    <step id="q4"> ... </step>
    <step id="q5"> ... </step>

    <step id="interlude">
      Animation chargement
      "Analyse de vos reponses..."
      Barre de progression animee
    </step>

    <step id="result">
      "Votre soin ideal"
      Carte produit (pastel bg, emoji/image, nom, pourquoi, details)
      Bouton CTA "Demander conseil" ou "Commander"
      Lien "Refaire le quiz"
    </step>

    <footer> Charcoal, mentions pharmacie </footer>

    <script> Logique scoring + navigation </script>
  </body>
</html>
```

**Fichier unique, self-contained** — tout le CSS et JS est inline, pas de dependances externes (sauf Google Fonts).

### Etape 6 — Tester et ouvrir

```bash
open -a "Brave Browser" "chemin/vers/quiz.html"
```

Verifier :
- Le quiz se charge sans erreur console
- La navigation fonctionne (intro → Q1 → Q2 → ... → resultat)
- Chaque produit peut etre atteint comme resultat
- Le design est visuellement coherent avec `index-redesign.html`
- Le responsive fonctionne (tester en largeur mobile ~375px)

---

## Naming convention

```
quiz-{categorie}.html
```

Exemples :
- `quiz-soin-peau.html` — soins visage
- `quiz-solaire.html` — protection solaire
- `quiz-capillaire.html` — shampoings/soins cheveux
- `quiz-complement.html` — complements alimentaires
- `quiz-bebe.html` — soins bebe/maternite

---

## Page "Coming Soon" pour les quiz non disponibles

**Fichier :** `quiz-coming-soon.html`

**Objectif :** Rediriger les visiteurs qui cliquent sur une catégorie de quiz pas encore créée (Produits naturels, Compléments alimentaires, Automédication).

**Structure :**
- Navbar HIMS complète (logo, menu mobile, dropdowns)
- Badge "En cours de création"
- Liste des 4 catégories de quiz avec leur statut :
  - Dermocosmétique : **Disponible** (cliquable → quiz-soin-peau.html)
  - Produits naturels : **Bientôt**
  - Compléments alimentaires : **Bientôt**
  - Automédication : **Bientôt**
- Boutons CTA (vers quiz dermo + retour accueil)
- Encart conseil invitant à passer en pharmacie
- Footer cohérent avec le site

**Design :** Utilise le même design system HIMS que `quiz-soin-peau.html` (variables CSS, Fraunces/DM Sans, pastels, etc.)

**Quand mettre à jour :**
- Quand un nouveau quiz est créé, changer son statut de "Bientôt" à "Disponible" et ajouter le lien
- Quand tous les quiz sont créés, cette page peut être supprimée ou redirigée

---

## Carte produit — format resultat

Chaque resultat de quiz affiche une carte produit avec :

```
┌─────────────────────────────────────┐
│  [fond pastel]                      │
│                                     │
│        [emoji ou image]             │
│                                     │
│  MARQUE                             │
│  Nom du Produit                     │
│                                     │
│  "Pourquoi ce soin pour vous :"     │
│  Explication personnalisee 2-3      │
│  phrases liees aux reponses         │
│                                     │
│  ┌───────────┐ ┌────────────────┐   │
│  │ Type peau │ │ Actif cle      │   │
│  └───────────┘ └────────────────┘   │
│  ┌───────────┐ ┌────────────────┐   │
│  │ Texture   │ │ SPF / Non      │   │
│  └───────────┘ └────────────────┘   │
│                                     │
│  [Bouton CTA teal-pro]             │
│                                     │
│  "Ou venez nous voir en pharmacie"  │
│  Adresse + horaires                 │
│                                     │
└─────────────────────────────────────┘
```

---

## Interlude de chargement

Entre la derniere question et le resultat, afficher un ecran "analyse" de **3 secondes** avec :
- Barre de progression animee (3 etapes)
- Messages progressifs : "Analyse de vos reponses...", "Comparaison avec nos soins...", "Votre soin ideal est pret!"
- Fond pastel-mint

L'interlude est purement cosmetique (le scoring est instantane), mais il cree un sentiment de personnalisation et de valeur.

---

## CTA et conversion

Le resultat ne vend pas en ligne (pas de e-commerce). Le CTA doit orienter vers :
1. **"Demander conseil a votre pharmacien"** — lien ou numero de telephone
2. **"Venez en pharmacie"** — adresse et horaires
3. **"Refaire le quiz"** — pour explorer d'autres resultats

---

## Quand mettre a jour un quiz

Un quiz doit etre mis a jour quand :
- Le stock change (un produit recommande tombe en rupture)
- De nouveaux produits en surstock apparaissent
- La saisonnalite change (ex: solaires en mars, reparation en octobre)
- L'analyse des ventes trimestrielle revele de nouveaux dormants

**Frequence ideale :** revision trimestrielle alignee avec l'analyse des ventes.

---

## Checklist avant publication

- [ ] 3 a 5 produits en resultat, tous en stock, avec priorite surstock
- [ ] 5 questions maximum, discriminantes
- [ ] Chaque produit est gagnant pour au moins un profil coherent
- [ ] Specs produit verifiees contre les fiches marque (RESSOURCES)
- [ ] Design conforme a `index-redesign/README.md`
- [ ] Fraunces + DM Sans charges correctement
- [ ] Teal-pro (#2D5F5D) partout, pas de gradient sur boutons
- [ ] Responsive OK (mobile 375px)
- [ ] Pas d'erreur JS en console
- [ ] Footer charcoal avec mentions pharmacie
- [ ] CTA oriente pharmacie (pas e-commerce)
- [ ] Disclaimer : "Ce quiz ne remplace pas un avis medical"
