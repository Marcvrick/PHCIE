---
title: "Anti-Slop Guide — Blog Pharmacie Charnal"
tags:
  - style-guide
  - blog
  - anti-slop
  - voix-laure
category: Pharma/Blog
type: style-guide
created: 2026-04-26
reference: "[[fatigue-moral-fin-hiver-queven]]"
---

# Anti-Slop Guide — Blog Pharmacie Charnal

> **Article de référence :** `06-fatigue-moral-fin-hiver/fatigue-moral-fin-hiver-queven.md` — c'est le standard. En cas de doute, comparer avec cet article.
> **Voix de référence :** [VOIX-Marc.md](../../../../Voix Marc/VOIX-Marc.md) — ton, pronoms, rythme.

---

## Principe directeur

Ce blog parle comme Laure parlerait à quelqu'un qu'elle connaît bien, debout face au comptoir. Pas une encyclopédie médicale. Pas une newsletter de labo. Une vraie conversation où les chiffres sont précis, le ton direct, et le lecteur respecté.

**Ce que ce blog n'est jamais :**
- Un article de santé magazine ("5 astuces pour booster vos défenses !")
- Un communiqué de presse ("Nous sommes ravis de vous informer que...")
- Un contenu SEO bourré de mots-clés ("vitamine D hiver Bretagne Quéven défenses immunitaires")

---

## 1. Ponctuation et typographie — règles absolues

| Interdit | Remplacer par |
|---|---|
| **Tiret cadratin `—`** | Point, virgule, deux-points, ou nouvelle phrase |
| **Double tiret `--`** | Même règle |
| **Emojis dans les bullets** (💡 ⚠️ ✅) | Texte en gras (voir tableau ci-dessous) |
| **Espace avant `!` `?` `:`** | Coller au mot : `symptomes?`, `Venez!` |
| **Conjonction en début de phrase** après `.` `?` `!` (`Et`, `Mais`, `Donc`, `Car`, `Ou`) | Supprimer la conjonction ou reformuler |

**Reformulations standards des callouts (validées avr 2026) :**

| Banni | Remplacer par |
|---|---|
| `💡 Bon à savoir` | `**Notre conseil:**` ou `**À savoir:**` ou `**À retenir:**` |
| `⚠️ Important` / `⚠️ Attention` | `**Attention:**` |
| `✅` en début de bullet pédagogique | Supprimer (le texte se suffit) |
| `❌` en début de bullet pédagogique | Supprimer ou reformuler en phrase |

**Conjonction après point — exemple de correction :**

❌ "Résultat sous 15 jours. Et pourtant, seuls 34% des Français le font."
✅ "Résultat sous 15 jours. Pourtant, seuls 34% des Français le font."

❌ "Le tétanos ne fait pas de distinction. Et même une simple égratignure peut suffire."
✅ "Le tétanos ne fait pas de distinction. Même une simple égratignure peut suffire."

**Pourquoi :** "Et/Mais/Donc/Car/Ou" en début de phrase est un tic anglo-saxon. En français écrit, ça sonne traduit et casse le rythme. Tolérance : 1× max par article comme effet rhétorique délibéré.

**Em-dash — exemple de correction :**

❌ "La vitamine D — essentielle pour l'immunité — manque souvent en hiver."
✅ "La vitamine D manque souvent en hiver. Elle est essentielle pour l'immunité."

**Emojis — exemple de correction :**

❌ "💡 Conseil pharmacie : Venez nous voir pour un bilan personnalisé."
✅ "**Notre conseil :** Passez nous voir pour faire le point sur votre situation."

---

## 2. Phrases et formules bannies

Ces formules ont déjà été utilisées ou sont des signatures IA reconnues. Interdites dans tous les articles futurs.

### Superlatifs et adjectifs creux

| Banni | Remplacer par |
|---|---|
| "scientifiquement prouvé(s)" | Citer l'étude ou le mécanisme concret |
| "particulièrement intense/rigoureux" | Donner le chiffre : "547 cas pour 100 000" |
| "révolutionnaire", "exceptionnel" | Supprimer ou nommer le fait concret |
| "qui boostent vos défenses" | "qui soutiennent votre système immunitaire" ou mécanisme précis |
| "incontournable", "essentiel" | Expliquer pourquoi à la place |
| "tout simplement" | Supprimer |

### Formules de remplissage

| Banni | Remplacer par |
|---|---|
| "il est important de noter que" | Aller droit au fait |
| "il convient de souligner" | Idem |
| "n'oubliez pas que" | Idem |
| "comme nous l'avons vu" | Idem |
| "dans le cadre de" | Reformuler directement |
| "au niveau de" | Reformuler directement |
| "premier recours santé" | "pharmacien", "nous" |
| "accompagnement personnalisé" | Ce qu'on fait concrètement |

### Slogans et conclusions creuses

Ces formules ont été utilisées — ne jamais réutiliser :

- "Prenez soin de vous, nous prenons soin de vous !" → 01-prevenir-maux-hiver
- "trio gagnant : alimentation équilibrée + gestes barrières + défenses naturelles" → 01-prevenir-maux-hiver
- "Votre pharmacie, partenaire santé de proximité" → 01-prevenir-maux-hiver
- "chaque geste compte" → formule générique
- "Bonne nouvelle :" en début de paragraphe → 01-prevenir-maux-hiver (acceptable une fois, jamais deux)

### Répétitions de formule d'un article à l'autre

Avant de publier, grep le dossier blog/ pour vérifier qu'une formule n'a pas déjà été utilisée :
```bash
grep -r "PHRASE_À_VÉRIFIER" blog/
```

---

## 3. Structure — ce qui génère du slop

### Listes à bullets systématiques

Les bullets sont acceptables pour des listes de produits, des posologies, des gestes précis. Elles deviennent du slop quand elles remplacent un raisonnement.

❌ **Slop :**
"Voici pourquoi vous êtes fatigué(e) en hiver :
- Le manque de lumière
- La vitamine D
- Le stress
- Les virus"

✅ **Voix Laure :**
"Sous nos latitudes, les jours courts combinés au ciel couvert bretonisent votre moral au sens propre : moins de lumière = moins de sérotonine. La vitamine D s'effondre au même moment. Ce n'est pas dans votre tête."

### Numérotation décorative des sections

❌ "1. L'alimentation / 2. Les gestes / 3. Les alliés naturels / 4. Par âge / 5. Aux premiers signes"
→ Structure copiée-collée d'un article à l'autre, reconnaissable immédiatement.

✅ Les H2 naissent de la question réelle du lecteur, pas d'un plan en 5 points symétrique.

### Conclusions en "appel à l'action empilé"

❌ "Que vous ayez besoin de A, de B, ou de C, nous sommes là pour vous accompagner avec D, E et F."
✅ Une seule invitation, concrète, locale : "Passez nous voir — on prend le temps."

---

## 4. Patterns positifs à répliquer (référence : Moral en berne)

Ces techniques fonctionnent. Les appliquer systématiquement.

### Ouverture en trois coups

**Mi-février. Il pleut. Encore.**

Trois phrases très courtes. Chacune une image. Pas d'explication. Le lecteur est dans la scène avant d'avoir lu un seul conseil. Ne pas répéter cette ouverture exacte, mais répliquer la technique : ancrer dans le moment, la météo, le ressenti breton.

Exemples valides (non utilisés) :
- "Début mars. Les arbres ne bourgeonnent toujours pas. Vous attendez."
- "Vendredi soir. Jambes lourdes. Troisième étage, sans ascenseur."

**Règle :** chaque article commence différemment. Jamais la même structure d'ouverture deux articles de suite.

### La phrase courte après un bloc factuel

Après deux ou trois phrases avec des chiffres ou des mécanismes, une phrase courte de 5 à 8 mots qui résume ou tranche.

✅ "Ce n'est pas « dans votre tête ». C'est de la biochimie."
✅ "Ça se traite."
✅ "80% des Français. Pas une exception."

La phrase courte doit être **spécifique** au sujet de l'article. Si elle pourrait apparaître dans n'importe quel article santé, c'est du slop.

### Le chiffre avant le conseil

Jamais conseiller sans poser le chiffre d'abord.

❌ "La vitamine D est importante en hiver, pensez à vous supplémenter."
✅ "80% des Français présentent une insuffisance en hiver. Une supplémentation en D3 d'octobre à mars est souvent nécessaire."

### L'ancrage breton — une fois par article, pas plus

Une référence à Quéven, au Morbihan, au ciel couvert, à la pluie bretonne. Une seule par article. Elle doit être naturelle, pas insérée pour le SEO.

✅ "Sous nos latitudes, cette synthèse est quasi nulle d'octobre à mars."
✅ "Le ciel breton ne nous aide pas vraiment sur ce point."
❌ "À Quéven, dans le Morbihan, en Bretagne, notre pharmacie est là pour vous aider." (SEO visible)

---

## 5. Usage des pronoms — règle précise

| Pronom | Usage | Exemple |
|---|---|---|
| **"Je"** | Expertise personnelle, conseil direct, observation terrain | "L'alternative que je privilégie", "Je vérifie toujours..." |
| **"Nous"** | Équipe, invitation, accueil | "Passez nous voir", "Chez nous", "Nous prenons le temps" |
| **"Vous"** | Dialogue direct, question rhétorique | "Vous vous demandez si...", "Voici ce que vous pouvez faire" |
| **"On"** | Universel inclusif, ton conversationnel | "On hésite souvent entre...", "On pense à tort que..." |

**Interdit :** "À la Pharmacie Charnal, nous recommandons..." → répétition du nom de marque inutile. Utiliser "Chez nous" ou "nous".

---

## 6. Checklist d'audit — appliquer à chaque article existant

### Ponctuation et typographie
- [ ] Zéro em dash `—` dans le corps de l'article
- [ ] Zéro emoji dans les bullets ou les titres
- [ ] Ponctuation `!` `?` `:` collée au mot précédent (règle française)

### Formules
- [ ] Grep "scientifiquement prouvé" → 0 résultat
- [ ] Grep "particulièrement intense" → max 1 occurrence sur tout le blog
- [ ] Grep "partenaire santé" → 0 résultat
- [ ] Grep "trio gagnant" → 0 résultat
- [ ] Grep "prendre soin" → vérifier si dupliqué entre articles
- [ ] Grep "chaque geste compte" → 0 résultat
- [ ] Grep "il est important de noter" → 0 résultat
- [ ] Grep "Bonne nouvelle :" → max 1 occurrence sur tout le blog
- [ ] Grep "tout simplement" / "Tout simplement" → 0 résultat
- [ ] Grep "n'oubliez pas" → 0 résultat
- [ ] Grep "premier recours santé" → 0 résultat
- [ ] Grep "Au comptoir, (nous|on)" → 0 résultat dans le corps (autorisé uniquement comme nom de section dans la nav, breadcrumb, schema)
- [ ] Grep `\. (Et|Mais|Donc|Car|Ou) ` → 0 résultat (conjonction en début de phrase)
- [ ] Grep "Prenez soin de vous!" → 0 résultat (signature interdite)

### Structure
- [ ] L'ouverture n'est pas une liste numérotée
- [ ] La conclusion n'est pas un "appel à l'action empilé" (A, B, C nous sommes là pour D, E, F)
- [ ] Pas de section intitulée "Votre pharmacie, [quelque chose]"

### Voix
- [ ] Au moins un chiffre précis avec sa source dans l'article
- [ ] Le "je" est utilisé pour l'expertise, pas pour l'autopromotion
- [ ] La conclusion invite à venir, sans empiler les CTAs

---

## 7. Articles à auditer (état au 26 avril 2026)

| Article | Problèmes identifiés | Priorité |
|---|---|---|
| `01-prevenir-maux-hiver` | Emojis 💡⚠️, "scientifiquement prouvés", "épidémie particulièrement intense" ×2, "trio gagnant", conclusion slogan, structure 5 sections numérotées | Haute |
| `04-detox-apres-fetes` | À auditer | Normale |
| `05-humidite-douleurs-articulaires` | À auditer | Normale |
| `06-fatigue-moral-fin-hiver` | **Référence** — pas d'intervention | — |
| `07-gastro-enterite` | À auditer | Normale |
| `09-mars-bleu` | À auditer | Normale |
| `10-allergie-pollen` | À auditer | Normale |
| `11-protection-solaire` | À auditer | Normale |
| `12-troubles-sommeil` | À auditer | Normale |

---

## 8. Procédure d'audit d'un article

1. **Grep automatique** sur les formules bannies (section 2)
2. **Lecture à voix haute** du premier et du dernier paragraphe : est-ce que ça sonne comme une vraie conversation ou comme un article généré?
3. **Test du "n'importe quel blog santé"** : les phrases pourraient-elles apparaître sur doctolib.fr, ameli.fr, ou un blog de complément alimentaire? Si oui, les réécrire à partir d'un fait spécifique à l'article.
4. **Compter les chiffres** : chaque section conseils doit contenir au moins un chiffre sourcé.
5. **Vérifier la conclusion** : une seule invitation, sans liste d'arguments, sans slogan.

### Sweep grep automatique (à passer avant publication)

```bash
cd blog/
file=mon-article-queven.html  # remplacer par le fichier cible

# 1. Em-dash (objectif: 0 dans le corps, tolérance: 0 dans biblio aussi)
grep -c "—" "$file"

# 2. Emojis pédagogiques
grep -E "💡|⚠️|✅|❌|🌿|🔬" "$file"

# 3. Formules bannies
grep -niE "trio gagnant|premier recours santé|n'oubliez pas|Bonne nouvelle:|tout simplement|partenaire santé|scientifiquement prouv|chaque geste compte|particulièrement intense|Prenez soin de vous!" "$file"

# 4. "Au comptoir" dans le corps (false positives à exclure : breadcrumb, nav, schema)
grep -niE "au comptoir" "$file" | grep -viE "BreadcrumbList|name.*Au comptoir|>Au comptoir<|<title>|content="

# 5. Conjonction en début de phrase
grep -nE "\. (Et|Mais|Donc|Car|Ou) " "$file"

# 6. Espace avant ponctuation française
grep -nE " [!?:]" "$file" | grep -vE "https?://|http :|<!--|aria-|^\s*<|setAttribute|contains"
```

**Sortie attendue :** zéro résultat (sauf les exceptions documentées). Si non zéro, corriger AVANT publication.
