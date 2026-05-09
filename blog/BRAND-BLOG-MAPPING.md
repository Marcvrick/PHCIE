# Brand → Blog Article Mapping

**But :** chaque page marque (`Nos-marques/*-page.html`) doit avoir un bloc "Pour aller plus loin sur le blog" pointant vers un article qui mentionne la marque ou son univers produit. Cela renforce le maillage SEO interne et donne aux pages marques un signal de fraîcheur via leurs liens entrants.

**Bloc cible** : `<div class="laure-blog-link">` à la fin de la section "Conseil de Laure" sur chaque page marque.

**Dernière mise à jour** : 7 mai 2026

---

## 🔗 État du mapping (16 marques, hors Caudalie retirée)

### ✅ Marques liées à un article (déjà fait — commit `be69f98` du 6 mai)

| Marque | Article blog cible | Statut |
|---|---|---|
| **Avène** | Premiers soleils : protéger sa peau dès le printemps | ✅ Lié |
| **Bioderma** | Premiers soleils : protéger sa peau dès le printemps | ✅ Lié |
| **La Roche-Posay** | Premiers soleils : protéger sa peau dès le printemps | ✅ Lié |
| **La Rosée** | Premiers soleils : protéger sa peau dès le printemps | ✅ Lié |
| **Nuxe** | Premiers soleils : protéger sa peau dès le printemps | ✅ Lié |
| **Aragan** | Détox après les fêtes : mythe ou réalité? | ✅ Lié |
| **Natform** | Compléments alimentaires : pharmacie ou internet? | ✅ Lié |
| **Pileje** | Compléments alimentaires : pharmacie ou internet? | ✅ Lié |
| **S.I.D Nutrition** | Troubles du sommeil : solutions naturelles | ✅ Lié |

### 🟡 Marques en cours de liaison (article rédigé, lien à poser au moment de la mise en ligne du HTML)

| Marque | Article blog cible | Statut |
|---|---|---|
| **Klorane** | #18 Quel shampoing pharmacie choisir? Klorane, Nuxe, Bioderma, Avène (lundi 11 mai) | 🟡 Article .md prêt, lien à ajouter sur klorane-page.html |
| **Nuxe** (lien complémentaire) | #18 Shampoings (lien secondaire en plus du lien solaire) | 🟡 Optionnel — la page Nuxe a déjà un lien solaire |
| **Biocanina** | #19 Chien et chat : les essentiels santé en pharmacie pour le printemps (lundi 18 mai) | 🟡 Article .md prêt, lien à ajouter sur biocanina-page.html |

### 📝 Marques à lier (article à rédiger)

| Marque | Article blog cible (proposé) | Date publication cible |
|---|---|---|
| **Mustela** | #20 Bébé 0-3 ans : la routine soin essentielle (et la grossesse aussi) | Lundi 25 mai 2026 |
| **Biogaran** | #21 Génériques : pourquoi votre boîte change parfois (et c'est OK) | Lundi 1 juin 2026 |
| **Bion3** | #22 Probiotiques et multivitamines : à quoi ça sert vraiment? | Automne 2026 (octobre) |
| **Boiron** | #23 L'homéopathie au comptoir : pour qui, pour quoi, quand? | Automne 2026 (novembre) |

---

## 🔄 Comment poser le lien sur une page marque

Au moment où on publie un nouvel article qui cible une marque, ajouter ce bloc en bas de la section "Conseil de Laure" sur la page marque correspondante :

```html
<div class="laure-blog-link" style="margin-top: 32px; padding: 20px 24px; background: var(--brand-pastel-1); border-left: 4px solid var(--brand-color);">
    <p style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--brand-color); margin-bottom: 8px;">Pour aller plus loin sur le blog</p>
    <a href="../blog/19-chiens-chats-pharmacie/chiens-chats-pharmacie-queven.html" style="font-size: 1.1rem; font-weight: 600; color: var(--charcoal); text-decoration: none;">
        Chien et chat : les essentiels santé en pharmacie pour le printemps →
    </a>
</div>
```

**Attention** : ne pas utiliser `var(--space-20)` qui n'est défini nulle part — toujours hardcoder les paddings (cf. fix du 7 mai 2026, commit `fe9252a`).

---

## 📊 Couverture après publications mai-juin 2026

Une fois les articles #18, #19, #20, #21 publiés et liés aux pages marques, **12 marques sur 16 auront un article blog dédié**. Restent Bion3 et Boiron pour l'automne 2026 (saisons cohérentes : immunité de rentrée pour Bion3, ORL d'hiver pour Boiron).

**Statut final cible (fin novembre 2026)** : 16/16 marques liées à un article.
