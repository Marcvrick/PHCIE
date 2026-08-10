---
title: Prix indicatifs des produits des quiz
tags: [quiz, prix, produits, pharmacie]
category: Référence
type: inventaire
created: 2026-08-09
updated: 2026-08-10
---

# Prix indicatifs des produits des quiz

Prix tels qu'ils s'affichent sur les cartes résultat des 4 quiz (`Quizzes/quiz-*.html`, champ `price` du JS). Ce sont les valeurs **servies au visiteur** sur www.pharmaciecharnal.com, pas un tarif de vente.

**65 produits sur 65 portent un prix** (depuis le 2026-08-10 : les 42 produits d'automédication ont reçu leur champ `price`, et `renderProductCard()` affiche désormais le bloc « prix indicatif » comme les trois autres quiz).

| Quiz | Produits | Avec prix | Fourchette |
|---|---|---|---|
| Dermocosmétique | 3 | 3 | 13,50 € – 24,90 € |
| Produits naturels | 15 | 15 | ~8 € – ~28 € |
| Compléments | 5 | 5 | 12,90 € – 24,90 € |
| Automédication | 42 | 42 | 1 € – 10 € |

Voir aussi : [INVENTAIRE-PRODUITS-QUIZZ.md](INVENTAIRE-PRODUITS-QUIZZ.md) (suivi des photos produit).

---

## 1. Dermocosmétique — `quiz-soin-peau.html`

| Produit | Marque | Prix indicatif | Format |
|---|---|---|---|
| Hydrance Riche | AVENE | **13,50 €** | 40 ml |
| Gel-Crème Oil Control SPF25 | CERAVE | **15,90 €** | 52 ml |
| Pigmentbio Daily Care SPF50+ | BIODERMA | **24,90 €** | 40 ml |

## 2. Produits naturels — `quiz-produits-naturels.html`

Prix préfixés `~` dans la source : ce sont des ordres de grandeur, pas des montants exacts. Trois marques par thème, du moins cher au plus cher.

| Thème | Produit | Marque | Approche | Prix indicatif | Format |
|---|---|---|---|---|---|
| Sommeil & Relaxation | Valériane Bio | NAT&FORM | Phytothérapie | **~8 €** | 200 gélules |
| Sommeil & Relaxation | Sommeil Triple Action | PHYTOSUN ARÔMS | Aromathérapie | **~11 €** | 30 comprimés |
| Sommeil & Relaxation | SOM•ACTIFS | ARAGAN | Micronutrition | **~15 €** | 30 gélules |
| Stress & Sérénité | Rhodiola Bio | NAT&FORM | Phytothérapie | **~9 €** | 200 gélules |
| Stress & Sérénité | Stress Triple Action | PHYTOSUN ARÔMS | Aromathérapie | **~9 €** | 30 capsules |
| Stress & Sérénité | SEREN•ACTIFS | ARAGAN | Micronutrition | **~17 €** | 30 gélules |
| Immunité & Vitalité | Échinacée Bio | NAT&FORM | Phytothérapie | **~8 €** | 200 gélules |
| Immunité & Vitalité | Aromadoses Défenses Naturelles | PHYTOSUN ARÔMS | Aromathérapie | **~9 €** | 30 capsules |
| Immunité & Vitalité | IMMUN•ACTIFS | ARAGAN | Micronutrition | **~15 €** | 30 gélules |
| Digestion & Confort | Artichaut Bio | NAT&FORM | Phytothérapie | **~8 €** | 200 gélules |
| Digestion & Confort | Aromadoses Digestion Transit | PHYTOSUN ARÔMS | Aromathérapie | **~8 €** | 30 capsules |
| Digestion & Confort | BIOTIC•P7 ENTÉRO | ARAGAN | Micronutrition | **~28 €** | 30 gélules |
| Respiration & Confort ORL | Thym Bio | NAT&FORM | Phytothérapie | **~8 €** | 200 gélules |
| Respiration & Confort ORL | Aromadoses Nez & Gorge | PHYTOSUN ARÔMS | Aromathérapie | **~8 €** | 30 capsules |
| Respiration & Confort ORL | RHIN•ACTIFS BIO | ARAGAN | Micronutrition | **~10 €** | 15 gélules |

## 3. Compléments alimentaires — `quiz-complement.html`

| Produit | Marque | Prix indicatif | Format / durée de cure |
|---|---|---|---|
| Lactibiane Référence | PiLeJe | **17,50 €** | 30 gélules — 1 mois |
| Formag | PiLeJe | **24,90 €** | 90 comprimés — 1 à 3 mois |
| Chronobiane LP | PiLeJe | **15,90 €** | 30 comprimés — 1 mois |
| D3 Biane Spray 1000 UI | PiLeJe | **14,50 €** | 20 ml — 4 mois (1 spray/jour) |
| Curcuma Bio | Nat&Form | **12,90 €** | 60 gélules — 1 à 2 mois |

## 4. Automédication — `quiz-automedication.html`

Les 42 produits portent un `price` en euros entiers, affiché sous les mises en garde. Pas de champ `format` sur ce quiz : la carte montre posologie, durée et mises en garde, puis le prix.

| Produit                         | Marque           | Positionnement                              | Prix indicatif |
| ------------------------------- | ---------------- | ------------------------------------------- | -------------- |
| Paracétamol 1000 mg             | BIOGARAN CONSEIL | Antalgique et antipyrétique                 | **2 €**              |
| Ibuprofène 400 mg               | BIOGARAN CONSEIL | Anti-inflammatoire                          | **2 €**              |
| Cétirizine 10 mg                | BIOGARAN CONSEIL | Antihistaminique 2ème génération            | **2 €**              |
| Pastilles Amylmétacrésol        | BIOGARAN CONSEIL | Antiseptique local miel-citron              | **7 €**              |
| Collutoire Spray                | BIOGARAN CONSEIL | Antiseptique + anesthésiant local           | **7 €**              |
| Macrogol 10 g                   | BIOGARAN CONSEIL | Laxatif osmotique doux                      | **3 €**              |
| Lopéramide 2 mg                 | BIOGARAN CONSEIL | Anti-diarrhéique                            | **2 €**              |
| Métopimazine 7,5 mg             | BIOGARAN CONSEIL | Anti-nauséeux orodispersible                | **2 €**              |
| Phloroglucinol 80 mg            | BIOGARAN CONSEIL | Antispasmodique                             | **3 €**              |
| Oméprazole 20 mg                | BIOGARAN CONSEIL | Anti-acide (IPP)                            | **10 €**             |
| Oxomémazine Sirop               | BIOGARAN CONSEIL | Antitussif pour toux sèche                  | **5 €**              |
| Carbocistéine Sirop 5%          | BIOGARAN CONSEIL | Fluidifiant bronchique pour toux grasse     | **4 €**              |
| Trolamine 0,67% Émulsion        | BIOGARAN CONSEIL | Soin des brûlures superficielles            | **6 €**              |
| Chlorhexidine Spray             | BIOGARAN CONSEIL | Antiseptique cutané                         | **5 €**              |
| Levure Saccharomyces boulardii  | BIOGARAN CONSEIL | Probiotique intestinal                      | **6 €**              |
| Alginate de Sodium/Bicarbonate  | BIOGARAN CONSEIL | Pansement gastrique                         | **5 €**              |
| Chlorhexidine Bain de Bouche    | BIOGARAN CONSEIL | Antiseptique bucco-dentaire                 | **2 €**              |
| Racécadotril 100 mg             | BIOGARAN CONSEIL | Antisécrétoire intestinal                   | **4 €**              |
| Efferalgan 1000 mg              | UPSA             | Paracétamol effervescent                    | **1 €**              |
| Dafalgan 1000 mg                | UPSA             | Paracétamol comprimé pellicúlé              | **1 €**              |
| Aspirine UPSA Vitamine C        | UPSA             | Antalgique + Vitamine C                     | **7 €**              |
| Fervex État Grippal             | UPSA             | Paracétamol + Antihistaminique + Vitamine C | **7 €**              |
| Mucomyst 200 mg                 | UPSA             | Mucolytique - Fluidifiant bronchique        | **6 €**              |
| Oxomémazine UPSA                | UPSA             | Sirop antitussif pour toux sèche            | **6 €**              |
| Phytovex Maux de Gorge Spray    | UPSA             | Dispositif médical naturel                  | **9 €**              |
| Smecta 3 g                      | UPSA             | Pansement digestif - Diosmectite            | **5 €**              |
| Smecta Enfant                   | UPSA             | Pansement digestif pédiatrique              | **5 €**              |
| Macrogol 4 g Enfant             | BIOGARAN CONSEIL | Laxatif osmotique pédiatrique               | **2 €**              |
| Donormyl 15 mg                  | UPSA             | Antihistaminique sédatif                    | **3 €**              |
| UPSA Vitamine C 1000 mg         | UPSA             | Complément alimentaire effervescent         | **5 €**              |
| UPSA Acérola 1000 Bio           | UPSA             | Vitamine C naturelle Bio                    | **10 €**             |
| Paracétamol Sirop Pédiatrique   | BIOGARAN CONSEIL | Sirop avec pipette doseuse                  | **1 €**              |
| Efferalgan Pédiatrique Sirop    | UPSA             | Sirop fraise avec seringue doseuse          | **1 €**              |
| Ibuprofène Sirop Enfant         | BIOGARAN CONSEIL | Sirop anti-inflammatoire pédiatrique        | **2 €**              |
| Cétirizine Gouttes Pédiatriques | SUR ORDONNANCE   | Solution buvable en gouttes (prescription)  | **2 €**              |
| Carbocistéine Sirop Enfant 2%   | BIOGARAN CONSEIL | Fluidifiant bronchique pédiatrique          | **5 €**              |
| Maalox Maux d'Estomac           | SANOFI / OPELLA  | Antiacide action rapide                     | **8 €**              |
| Dulcolax 5 mg                   | SANOFI / OPELLA  | Laxatif stimulant ponctuel                  | **9 €**              |
| Maxilase Comprimés              | SANOFI / OPELLA  | Anti-inflammatoire naturel (adulte)         | **3 €**              |
| Maxilase Sirop                  | SANOFI / OPELLA  | Anti-inflammatoire naturel (sirop)          | **6 €**              |
| Alpha-amylase Sirop             | BIOGARAN CONSEIL | Anti-inflammatoire naturel (sirop)          | **4 €**              |
| Homéogène 9                     | BOIRON           | Homéopathie mal de gorge                    | **8 €**              |

---

## Ce qu'il faudrait trancher

- ~~**Écart de traitement entre quiz.**~~ Réglé le 2026-08-10 : les 4 quiz affichent un prix.
- **Trois conventions de prix cohabitent.** Naturels en `~8 €` (arrondi avec tilde), automédication en `2 €` (entier sans tilde), dermocosmétique et compléments en `13,50 €` (au centime). Choisir laquelle généraliser.
- **Aucune date de relevé.** Les prix sont en dur dans le JS, sans mention de quand ils ont été constatés. Un prix de complément qui bouge ne se voit pas.



