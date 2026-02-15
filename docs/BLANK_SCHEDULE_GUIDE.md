# 📋 Guide : Créer un Planning Vide (Mode Avancé)

## 📝 Description

Le mode "Créer un planning vide (avancé)" permet de créer un planning **personnalisé depuis zéro** sans utiliser un modèle existant.

---

## 🚀 Comment utiliser

### Étape 1 : Accéder au mode planning vide

1. Aller à **Manager Dashboard**
2. Scroller à **"Gestion des plannings"**
3. Cliquer sur **"✏️ Créer un planning vide (avancé)"**

```
┌─────────────────────────────────────────┐
│ Gestion des plannings                   │
│                                         │
│ [📋 Choisir modèle] [✏️ Planning vide]  │
│                          ↑              │
│                      CLIQUER ICI        │
└─────────────────────────────────────────┘
```

---

### Étape 2 : Remplir le formulaire

L'éditeur s'affiche avec une structure **par défaut** :

```
NOUVEAU PLANNING (vide)

Nom de l'employée : [_____________]

Rôle : ⚫ Préparatrice
       ○ Pharmacien

─ SEMAINE PAIRE ──────────────────────
Lundi    ☑ AM [9h-12h30]  ☑ PM [14h-19h15]
Mardi    ☑ AM [9h-12h30]  ☑ PM [14h-19h15]
Mercredi ☑ AM [9h-12h30]  ☑ PM [14h-19h15]
Jeudi    ☑ AM [9h-12h30]  ☑ PM [14h-19h15]
Vendredi ☑ AM [9h-12h30]  ☑ PM [14h-19h15]
Samedi   ☑ AM [9h-12h30]  ○ PM

─ SEMAINE IMPAIRE ─────────────────────
(Même interface...)

Total : 47.5h/semaine (moy.)

[Annuler] [👁 Prévisualiser] [✓ Créer]
```

---

## ⚙️ Actions possibles

### 1. **Modifier le nom**
- Entrer le nom de l'employée (ex: "Marie Dupont")
- Obligatoire

### 2. **Choisir le rôle**
```
○ Pharmacien     (horaires flexibles, validation requise)
⚫ Préparatrice  (par défaut)
```

### 3. **Configurer les horaires**

#### Décocher un créneau
```
☑ AM [9h-12h30]  → ☐ PM          (supprime le PM)
```
Le champ de texte devient grisé et inactif.

#### Modifier les horaires
```
Cliquer sur le texte des heures pour éditer
[9h-12h30] → [10h-13h]    ✓ Enregistré automatiquement
```

#### Format attendu
```
[HEURE]-[HEURE]  ou  [H]-[H]
9h-12h30         ✓
14h-19h15        ✓
10h-13h          ✓
```

---

## 📊 Horaires par défaut

Le planning vide propose une **structure complète** dès le départ :

### Semaine paire
```
Jour       | Matin      | Après-midi
-----------|------------|----------
Lundi      | 9h-12h30   | 14h-19h15
Mardi      | 9h-12h30   | 14h-19h15
Mercredi   | 9h-12h30   | 14h-19h15
Jeudi      | 9h-12h30   | 14h-19h15
Vendredi   | 9h-12h30   | 14h-19h15
Samedi     | 9h-12h30   | (vide)
           | TOTAL: 47h30
```

### Semaine impaire
```
(Identique à la semaine paire par défaut)
```

---

## 💡 Cas d'usage courants

### Cas 1 : Employée à temps partiel (22.5h/sem)
```
1. Garder lundi, mardi, jeudi (journée complète)
2. Décocher les autres jours
3. Résultat: 3 jours × 7.5h = 22.5h
```

### Cas 2 : Employée part-time le week-end
```
1. Décocher lundi-vendredi
2. Garder samedi matin
3. Résultat: 3.5h/sem (samedi matin)
```

### Cas 3 : Horaires spéciaux
```
1. Garder tous les jours
2. Modifier mardi: 10h-13h au lieu de 9h-12h30
3. Modifier mercredi: 14h-18h au lieu de 14h-19h15
4. Résultat: horaires personnalisés
```

### Cas 4 : Pharmacien avec contraintes
```
1. Sélectionner "Pharmacien"
2. Garder 4 jours de présence
3. Modifier horaires selon besoin
4. Système validera la présence pharmacien
```

---

## 🎯 Calcul automatique

Le total des heures se **met à jour en temps réel** :

```
Vous changez quelque chose
         ↓
"Total : X.Xh/semaine" se recalcule automatiquement
```

**Exemple:**
```
État initial: 47.5h/semaine
Vous décochez vendredi PM
         ↓
Nouveau total: 43h/semaine
```

---

## 📋 Comparaison : Modèle vs Vide

| Aspect | Avec Modèle | Planning Vide |
|--------|------------|---------------|
| **Point de départ** | Horaires existants | Horaires par défaut |
| **Utilité** | Copier une structure existante | Créer depuis zéro |
| **Flexibilité** | Modifier le modèle | Modifier librement |
| **Temps** | Rapide (5 min) | Un peu plus long (10 min) |
| **Cas d'usage** | Nouvelle employée similaire | Horaires uniques |

---

## ✅ Checklist avant création

Avant de cliquer "✓ Créer le planning" :

- [ ] Nom de l'employée saisi et valide
- [ ] Rôle sélectionné (Pharmacien ou Préparatrice)
- [ ] Au moins 1 jour de travail configuré
- [ ] Horaires au bon format (HH-HH ou Hh-Hh)
- [ ] Total heures affiché et correct
- [ ] Aucun message d'erreur

---

## ⚠️ Pièges à éviter

### ❌ Pas de nom
```
Résultat: Alert "Veuillez entrer le nom de l'employée"
```

### ❌ Tous les créneaux décochés
```
Attention: L'employée n'a pas d'horaires configurés
(Possible mais rare)
```

### ❌ Format d'heure incorrect
```
❌ 9-12          (pas de "h")
❌ 9h-12h30min   (format invalide)
✅ 9h-12h30      (bon format)
```

### ❌ Pharmacien sans présence
```
Attention: Un pharmacien sans horaires = problème
(Le système validera)
```

---

## 🔄 Après création

Après avoir cliqué "✓ Créer le planning" :

1. **Confirmation** : "Planning créé avec succès ! ✓"
2. **Données initialisées** :
   - Planning dans STAFF
   - Rôle dans ROLES
   - Contrat créé (CDI, aujourd'hui)
   - Vacances initialisées (25j)
3. **Employée visible** :
   - Vue Planning
   - Vue Demandes
   - Vue Vacances
   - Dashboard Manager

---

## 📱 Exemple complet

### Créer planning pour "Sophie Martin" (pharmacien, 30h/sem)

**Étapes :**

1. Cliquer "✏️ Planning vide"
2. Remplir :
   ```
   Nom: Sophie Martin
   Rôle: ○ Pharmacien
   ```

3. Modifier Semaine Paire :
   ```
   Lundi    ☑ AM ☑ PM
   Mardi    ☑ AM ☑ PM
   Mercredi ☑ AM ☐ PM     (décocher PM)
   Jeudi    ☑ AM ☑ PM
   Vendredi ☑ AM ☑ PM
   Samedi   ☐ AM ☐ PM     (décocher tout)
   ```

4. Modifier Semaine Impaire (identique)

5. Total affiché: 39h/semaine

6. Cliquer "✓ Créer"

7. ✅ Sophie Martin créée avec planning personnalisé

---

## 🎓 Conseils

- **Commencer simple** : Gardez la structure par défaut, modifiez juste ce qui est nécessaire
- **Tester les cas** : Vérifiez le total avant création
- **Demander à Laure** : En cas de doute sur les horaires
- **Modifier après** : Il est possible de changer le planning plus tard (Phase 2)

---

## 📞 Support

**Q: Impossible de créer le planning?**
A: Vérifier le nom et que au moins 1 jour est configuré

**Q: Les horaires ne sont pas bons?**
A: Vérifier le format (Hh-Hh30) et les totaux

**Q: Besoin de modifier après création?**
A: Contacter Laure (modification manuelle pour Phase 2)

---

**Le mode planning vide offre une flexibilité totale pour créer des horaires uniques!** 🎉
