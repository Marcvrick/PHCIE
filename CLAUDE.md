# CLAUDE.md - Website Pharmacie Charnal

Documentation technique pour le site web de la Pharmacie Charnal (Quéven).

---

## 🌐 Configuration GitHub Pages

### Repository Settings
- **GitHub Repository:** `https://github.com/Marcvrick/Pharmacie-Charnal`
- **Branche principale:** `main` (déploiement automatique)
- **Branche de travail:** `pharmacie-charnal`
- **GitHub Pages:** Activé sur la branche `main`

### Custom Domain
- **Domaine:** `www.pharmaciecharnal.com`
- **Fichier CNAME:** Contient `www.pharmaciecharnal.com`
- **DNS Configuration:** CNAME record pointant vers `marcvrick.github.io`
- **HTTPS:** Activer "Enforce HTTPS" dans Settings > Pages (peut prendre jusqu'à 24h après configuration DNS)

### Workflow Git
```bash
# Travailler sur la branche pharmacie-charnal
git checkout pharmacie-charnal
git add [fichiers]
git commit -m "Message"
git push origin pharmacie-charnal

# Déployer sur main (production)
git checkout main
git merge pharmacie-charnal
git push origin main
git checkout pharmacie-charnal  # Retourner sur la branche de travail
```

---

## 🎨 Charte Graphique & Design

### Palette de Couleurs (CSS Variables)

```css
:root {
    /* Colors - Organic Wellness Palette */
    --sage: #7C9885;           /* Vert naturel principal */
    --sage-light: #9DB3A4;     /* Vert clair */
    --sage-dark: #5F7A68;      /* Vert foncé */
    --teal: #2D5F5D;           /* Teal professionnel */
    --teal-dark: #1E4644;      /* Teal foncé */
    --blue: #4A7C8E;           /* Bleu confiance */
    --cream: #F5F1E8;          /* Crème chaleureux */
    --white: #FFFFFF;
    --black: #1A1A1A;

    /* Accent */
    --accent: #b4a6d7;         /* Lavande pour "Au Comptoir" */
    --accent-hover: #9b8bc4;
    --accent-active: #8270b1;
}
```

### Typographie

**Polices actuelles (système - fallback):**
- **Headings:** Georgia, Crimson Pro (à installer), serif
- **Body:** -apple-system, San Francisco, Segoe UI, DM Sans (à installer), sans-serif

**Note:** Les fichiers de polices custom (Crimson Pro et DM Sans) sont commentés dans `style.css` car les fichiers .woff2 ne sont pas encore uploadés. Le site utilise les polices système jusqu'à leur ajout.

### Éléments de Design

- **Logo:** `images/pharmacie-charnal-logo.png`
- **Hero badge:** Texte "Plus de 40 ans" (pas "Depuis plus de 40 ans")
- **Gradient text:** Utilisé pour les titres principaux (`class="gradient-text"`)
- **Cards:** `service-card`, `banner-item` avec hover effects
- **Mobile menu:** Hamburger menu avec 3 lignes, accessible sur tous les articles de blog

---

## 📁 Structure des Fichiers

### Pages Principales
```
index.html              # Accueil
histoire.html          # Notre Histoire
services.html          # Services
marques.html          # Nos Marques (avec ancres #cosmetiques, #complements, #premiers-soins)
blog.html             # Au Comptoir (liste des articles)
contact.html          # Contact
mentions-legales.html
donnees-personnelles.html
```

### Blog Articles
```
blog/
  ├── detox-apres-fetes-mythe-realite-queven.html
  ├── prevenir-maux-hiver-queven.html
  ├── professionnels-sante-queven-2026.html  # Carte interactive Leaflet
  └── vaccination-adulte-guide-pratique.html
```

### Assets
```
images/                # Photos et logo
style.css             # CSS principal (variables, composants, responsive)
animations.js         # Animations scroll et interactions
professionnels-sante-queven-carte.csv  # Données carte Leaflet
```

---

## 🏥 Contenu - Règles Strictes

### Marques de Produits

**RÈGLE CRITIQUE:** Seules les marques réellement vendues à la pharmacie peuvent être mentionnées.

**Vérification obligatoire:** Consulter les fichiers dans `/Users/mc/Documents/MarcOS/Pharma/` avant d'ajouter une marque.

**Marques approuvées:**

**Cosmétiques & Hygiène:**
- Dermatologie: Bioderma, La Roche-Posay, Avène, Nuxe, Vichy, Caudalie, Ducray
- Bébé: Mustela, Klorane Bébé
- Solaires: La Roche-Posay Anthelios, Avène, Bioderma, NUXE
- Capillaires: Klorane, Ducray, Vichy

**Compléments Alimentaires:**
- Vitamines: Bion 3, Biogaran
- Phytothérapie: PiLeJe, Arkopharma, Boiron, Aragan, Nat&Form
- Probiotiques: PiLeJe Lactibiane

**❌ Ne JAMAIS inventer de marques** (exemple d'erreurs passées: Elmex, Meridol, GUM, Parodontax)

### Informations Pharmacie

**Adresse:** 32 Place de Toulouse, 56530 Quéven
**Téléphone:** 02 97 05 09 31
**Horaires:**
- Lun-Ven: 9h-12h30 / 14h-19h15
- Samedi: 9h-12h30
- Dimanche: Fermé

**Réseaux sociaux:**
- Instagram: `https://www.instagram.com/pharmaciecharnalqueven/`
- Facebook: `https://www.facebook.com/pharmaciecharnal/`

---

## 🔧 Fonctionnalités Techniques

### Mobile Menu
- Hamburger icon à 3 lignes
- Toggle avec JavaScript
- Présent sur TOUTES les pages (y compris articles de blog)
- ARIA attributes pour accessibilité

### Carte Interactive (Leaflet.js)

**Fichier:** `blog/professionnels-sante-queven-2026.html`

**Configuration:**
- **Leaflet:** v1.9.4 (sans integrity hash pour éviter les erreurs)
- **PapaParse:** v5.4.1 pour parser le CSV
- **Données:** `professionnels-sante-queven-carte.csv` (15 professionnels de santé)
- **Tiles:** OpenStreetMap
- **Markers:** Pharmacie Charnal en rouge (icône custom), autres en bleu

**Important:** Ne pas ajouter d'attribut `integrity` aux CDN Leaflet (cause des erreurs de chargement).

### Animations

**Fichier:** `animations.js`

- Fade-in au scroll (IntersectionObserver)
- Parallax léger sur hero sections
- Smooth scroll pour ancres
- Stats counter animation

---

## 🎯 Navigation & UX

### Ordre des Services (Homepage)

1. Délivrance d'ordonnances
2. **Parapharmacie**
3. Vaccinations
4. Produits naturels
5. Matériel médical
6. **Livraison à domicile** (TOUJOURS en dernier)

### Bouton "Au Comptoir"

- Couleur: `#b4a6d7` (lavande)
- Hover: `#9b8bc4`
- Active: `#8270b1`
- Distingué du reste de la navigation

### Liens vers Marques

Les images banner sur homepage pointent vers:
- Médicaments → `marques.html`
- Hygiène buccodentaire → `marques.html#cosmetiques`
- Produits cosmétiques → `marques.html#cosmetiques`
- Produits bébé → `marques.html#cosmetiques`
- Compléments → `marques.html#complements`
- Premiers soins → `marques.html#premiers-soins`

---

## 🐛 Issues Résolus

### ✅ Leaflet Integrity Hash
- **Problème:** Script ne chargeait pas à cause de l'integrity hash mismatch
- **Solution:** Retirer les attributs `integrity` et `crossorigin` des tags Leaflet

### ✅ Fonts 404 Errors
- **Problème:** Fichiers .woff2 manquants (DMSans, CrimsonPro)
- **Solution:** @font-face commenté dans style.css, utilisation de polices système

### ✅ Version Control Confusion
- **Problème:** Multiples versions du site (vieille v2, nouvelle version)
- **Solution:** Nettoyage complet, fusion sur main, suppression des `-v2` files

### ✅ CSV Carte Non Présent
- **Problème:** `professionnels-sante-queven-carte.csv` manquant sur GitHub
- **Solution:** Ajout du fichier CSV avec données correctes

---

## 📋 Checklist Avant Déploiement

Avant chaque push vers `main`:

- [ ] Toutes les images ont un attribut `alt`
- [ ] Tous les liens internes sont relatifs (pas d'absolus avec `/`)
- [ ] Mobile menu présent sur toutes les pages
- [ ] Pas de marques inventées (vérifier fichiers Pharma)
- [ ] Informations contact à jour (adresse, téléphone, horaires)
- [ ] Polices système utilisées (ou fichiers .woff2 ajoutés)
- [ ] Pas d'integrity hash sur CDN Leaflet
- [ ] CNAME file présent
- [ ] Tester en local avant push

---

## 🚀 Commandes Utiles

```bash
# Vérifier l'état du repo
git status
git log --oneline -10

# Voir les branches
git branch -a

# Voir les remotes
git remote -v

# Tester en local (Python simple server)
python3 -m http.server 8000
# Puis ouvrir http://localhost:8000

# Lister les fichiers récemment modifiés
ls -lt | head -20
```

---

## 🔮 À Faire (Backlog)

- [ ] Ajouter fichiers de polices custom (.woff2) dans `/fonts/`
- [ ] Décommenter @font-face dans style.css une fois polices ajoutées
- [ ] Vérifier certificat SSL activé (HTTPS)
- [ ] Optimiser images (compression, WebP)
- [ ] Ajouter plus d'articles de blog
- [ ] Tests d'accessibilité (WCAG)

---

## 📞 Support & Ressources

- **Documentation GitHub Pages:** https://docs.github.com/pages
- **Leaflet.js Docs:** https://leafletjs.com/reference.html
- **Pharmacie Charnal CLAUDE-Pharma.md:** `/Users/mc/Documents/MarcOS/Pharma/CLAUDE-Pharma.md` (pour contenu)

---

*Dernière mise à jour: Janvier 2026*
*Répertoire: /Users/mc/Documents/MarcOS/Pharma/website-pharmacie-charnal/*
