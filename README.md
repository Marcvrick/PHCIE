# Site Web - Pharmacie Charnal (Version 2)

Site internet statique pour la Pharmacie Charnal à Quéven (56530).

## 📁 Structure du site

```
pharmacie-charnal/
├── index-v2.html       # Page d'accueil
├── histoire-v2.html    # Notre Histoire (Laure Charnal)
├── services-v2.html    # Liste détaillée des services
├── blog-v2.html        # Actualités et conseils santé
├── contact-v2.html     # Contact et localisation
├── style-v2.css        # Feuille de style principale
├── animations.js       # Animations et interactions
├── blog/               # Dossier des articles de blog
│   ├── GUIDE-REDACTION-BLOG.md           # Guide de rédaction & E-E-A-T
│   ├── PLANNING-BLOG-PHARMACIE.md        # Planning éditorial
│   ├── prevenir-maux-hiver-queven.html   # Article publié (31 Déc 2025)
│   ├── vaccination-adulte-guide-pratique.html  # Article publié (20 Déc 2025)
│   └── prevenir-maux-hiver-reference.md  # Document de référence
├── images /            # Dossier des images
│   └── Pharmacie Charnal logo.png        # Logo de la pharmacie (48×48px)
└── README.md           # Ce fichier (documentation complète)
```

## 🎨 Caractéristiques du design

**Design "Wellness Minimal Raffiné"** - moderne et apaisant

- **Simple et accessible** : adapté à une population plutôt âgée
- **Textes grands** : taille de police généreuse (18px de base)
- **Responsive** : s'adapte aux mobiles, tablettes et ordinateurs
- **Palette organique** : Vert sauge (#7C9885), Teal (#2D5F5D), Crème (#FAF8F5)
- **Typographie élégante** : Crimson Pro (titres) + DM Sans (texte)
- **Animations subtiles** : Effets de fade-in au scroll, transitions douces
- **Navigation glassmorphism** : Barre de navigation moderne avec effet de verre

## 🌟 Fonctionnalités

- Logo cliquable qui ramène à l'accueil
- Navigation sticky avec 5 pages principales
- Scroll fluide vers les sections
- Icônes sociales (Instagram, Facebook) dans le footer
- Animations au scroll pour une meilleure expérience
- Design professionnel et moderne tout en restant simple

## 🎨 Configuration des icônes et logos

### Logo de la pharmacie (navigation)
- **Taille** : 48px × 48px
- **Fichier** : `images /Pharmacie Charnal logo.png`
- **Emplacement** : En haut à gauche de toutes les pages
- **CSS** : `.logo-icon` dans `style-v2.css` (ligne 169-175)

### Icônes réseaux sociaux (footer)
- **Taille** : 30px × 30px
- **Instagram** :
  - Lien : https://www.instagram.com/pharmaciecharnalqueven/
  - Rectangle SVG intérieur : 20px × 20px (important pour le rendu)
- **Facebook** :
  - Lien : https://www.facebook.com/pharmaciecharnal/
- **Emplacement** : Footer de toutes les pages
- **Note** : Le rectangle à l'intérieur du SVG Instagram doit rester à 20×20 même si le conteneur SVG fait 30×30

### Autres icônes SVG
- **Icônes de calendrier** : 30px × 30px
- **Flèches "Lire la suite"** : 30px × 30px
- **Icônes de boutons** : 30px × 30px

### Couleur signature footer
- **Phrase** : "Votre pharmacie familiale depuis près de 40 ans. Une tradition de soins personnalisés et attentifs."
- **Couleur** : Beige chaud (#F5E6D3)
- **CSS** : `.footer-about p` dans `style-v2.css`

## ⏰ Informations pratiques

**Horaires** (avec fermeture déjeuner) :
- Lun-Ven: 8h30-12h30 / 14h-20h
- Samedi: 9h-12h30
- Dimanche: Fermé

**Contact** :
- Adresse: 10 Place de Toulouse, 56530 Quéven
- Téléphone: 02 97 39 73 22

**Réseaux sociaux** :
- Instagram: https://www.instagram.com/pharmaciecharnalqueven/
- Facebook: https://www.facebook.com/pharmaciecharnal/

## ✏️ Comment modifier le contenu

### 1. Modifier les textes

Ouvrez le fichier HTML de la page que vous voulez modifier avec un éditeur de texte (VS Code recommandé, ou TextEdit, Notepad).

Les textes sont entre des balises :
- `<h1>Titre principal</h1>`
- `<h2>Sous-titre</h2>`
- `<h3>Petit titre</h3>`
- `<p>Paragraphe de texte</p>`

**Exemple** :
```html
<h2>Bienvenue à la Pharmacie Charnal</h2>
<p>Votre santé est notre priorité</p>
```

### 2. Ajouter des articles de blog

Dans `blog-v2.html`, copiez ce code et modifiez-le :

```html
<article class="blog-card fade-up">
    <div class="blog-image-placeholder">🌡️</div>  <!-- Changez l'émoji -->
    <div class="blog-content">
        <span class="blog-date">15 Janvier 2025</span>
        <h2 class="blog-title">Titre de l'article</h2>
        <p class="blog-excerpt">
            Résumé de votre article...
        </p>
        <a href="blog/votre-article.html" class="blog-link">
            <span>Lire la suite</span>
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none">
                <path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2"/>
            </svg>
        </a>
    </div>
</article>
```

**Important** : Placez les articles les plus récents en premier dans le code HTML.

### 3. Modifier les horaires

Les horaires apparaissent dans le footer de chaque page :

```html
<li>Lun-Ven: 8h30-12h30 / 14h-20h</li>
<li>Samedi: 9h-12h30</li>
<li>Dimanche: Fermé</li>
```

Modifiez ces lignes dans tous les fichiers -v2.html si les horaires changent.

### 4. Ajouter des photos

**Remplacer les placeholders de photos :**

Dans `index-v2.html` et `histoire-v2.html`, trouvez :
```html
<div class="hero-image-placeholder">
    Photo de la pharmacie
</div>
```

Remplacez par :
```html
<img src="votre-photo.jpg" alt="Pharmacie Charnal" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
```

**Important** : Placez vos photos dans le même dossier que les fichiers HTML.

### 5. Configurer les réseaux sociaux

**✅ CONFIGURÉ** - Les liens sont déjà en place sur toutes les pages :

- **Instagram** : https://www.instagram.com/pharmaciecharnalqueven/
- **Facebook** : https://www.facebook.com/pharmaciecharnal/

**Si vous devez modifier les liens :** Cherchez dans le footer de chaque page et remplacez les URLs.

**⚠️ Important pour l'icône Instagram :**
```html
<!-- Le SVG conteneur fait 30×30 -->
<svg width="30" height="30" viewBox="0 0 24 24" fill="none">
    <!-- MAIS le rectangle intérieur doit rester à 20×20 -->
    <rect x="2" y="2" width="20" height="20" rx="5" .../>
</svg>
```
Si vous modifiez la taille du SVG, ne changez PAS le rectangle intérieur.

### 6. Google Maps

**✅ CONFIGURÉ** - La carte Google Maps est déjà intégrée sur la page contact.

Si vous devez modifier l'adresse :
1. Allez sur [Google Maps](https://www.google.com/maps)
2. Recherchez votre nouvelle adresse
3. Cliquez sur "Partager" → "Intégrer une carte"
4. Copiez le code `<iframe>` fourni
5. Remplacez l'iframe existant dans `contact-v2.html`

### 7. Modifier les couleurs

Dans `style-v2.css`, trouvez cette section au début :

```css
:root {
    /* Couleurs principales */
    --sage: #7C9885;           /* Vert sauge */
    --sage-light: #A4BFA9;     /* Sauge clair */
    --sage-dark: #5A7A61;      /* Sauge foncé */
    --teal: #2D5F5D;           /* Teal */
    --cream: #FAF8F5;          /* Crème */
    /* ... */
}
```

Changez les codes couleur (format #XXXXXX) pour modifier la palette du site.

## 🌐 Comment mettre le site en ligne

### Option 1 : Netlify (GRATUIT et SIMPLE - recommandé)

1. Allez sur [netlify.com](https://www.netlify.com)
2. Créez un compte gratuit
3. Cliquez sur "Add new site" → "Deploy manually"
4. Glissez-déposez le dossier `pharmacie-charnal` sur la zone
5. Votre site sera en ligne en quelques secondes !
6. Vous obtiendrez une URL comme `pharmacie-charnal.netlify.app`
7. Vous pouvez ensuite configurer votre propre nom de domaine

### Option 2 : GitHub Pages (GRATUIT)

1. **Créer un compte GitHub** : [github.com](https://github.com)
2. **Créer un repository** :
   - Nom : `pharmacie-charnal`
   - Public
3. **Uploader vos fichiers** (tous les fichiers -v2.html, .css, .js)
4. **Activer GitHub Pages** :
   - Settings → Pages
   - Source : "main" branch
   - Save
5. Site accessible à : `https://votre-nom.github.io/pharmacie-charnal`

**Important** : Renommez `index-v2.html` en `index.html` avant de déployer !

### Option 3 : Hébergeur traditionnel

Uploadez tous les fichiers via FTP chez votre hébergeur (OVH, O2Switch, Ionos, etc.).

**Avant le déploiement** : Renommez tous les fichiers :
- `index-v2.html` → `index.html`
- `histoire-v2.html` → `histoire.html`
- `services-v2.html` → `services.html`
- `blog-v2.html` → `blog.html`
- `contact-v2.html` → `contact.html`
- `style-v2.css` → `style.css`

Et mettez à jour tous les liens internes dans le HTML en conséquence.

## 📝 Checklist avant mise en ligne

### Contenu essentiel
- [x] **Configurer les liens Instagram et Facebook** ✅
- [x] **Écrire les premiers articles de blog** (2 articles publiés) ✅
- [x] **Vérifier que tous les horaires sont corrects** ✅
- [x] **Vérifier le numéro de téléphone** (02 97 39 73 22) ✅
- [x] **Ajouter la carte Google Maps sur la page contact** ✅
- [ ] Ajouter de vraies photos de la pharmacie
- [ ] Ajouter une photo de Laure Charnal
- [ ] Vérifier et compléter l'histoire de la pharmacie (si nécessaire)

### Tests techniques
- [x] **Tester le site localement** (tous les liens fonctionnent) ✅
- [ ] Tester le site sur mobile
- [ ] Tester le site sur tablette
- [ ] Vérifier tous les liens internes
- [ ] Vérifier que les icônes s'affichent correctement

### Avant le déploiement
- [ ] **Renommer les fichiers -v2 en version finale** :
  - `index-v2.html` → `index.html`
  - `histoire-v2.html` → `histoire.html`
  - `services-v2.html` → `services.html`
  - `blog-v2.html` → `blog.html`
  - `contact-v2.html` → `contact.html`
  - `style-v2.css` → `style.css`
- [ ] Mettre à jour tous les liens internes dans le HTML après renommage
- [ ] Tester une dernière fois après renommage

## 📱 Tester le site

**Sur votre ordinateur** :
- Double-cliquez sur `index-v2.html`
- Le site s'ouvrira dans votre navigateur
- Testez tous les liens et la navigation

**Tester le responsive (mobile)** :
- Appuyez sur F12 dans votre navigateur
- Cliquez sur l'icône mobile/tablette (ou Cmd+Shift+M sur Mac)
- Redimensionnez pour voir comment le site s'affiche sur différents écrans

**Tester les animations** :
- Scrollez sur les pages pour voir les animations fade-in
- Testez le bouton "Nos services" qui scroll automatiquement
- Vérifiez que le logo ramène bien à l'accueil

## ✅ Accessibilité et simplicité

Le site v2 a été conçu pour être accessible aux personnes âgées :

- ✅ Textes GRANDS et lisibles (18px+)
- ✅ Navigation SIMPLE et CLAIRE
- ✅ Couleurs DOUCES et bien contrastées
- ✅ Design ÉPURÉ et professionnel
- ✅ Boutons GRANDS et faciles à cliquer
- ✅ Animations SUBTILES, non distrayantes
- ✅ Responsive pour tous les appareils

## 🎯 Prochaines étapes (optionnel)

1. **Système de rendez-vous** : Intégrer Doctolib ou Maiia
2. **Formulaire de contact** : Ajouter un formulaire avec Formspree ou Netlify Forms
3. **Analytics** : Ajouter Google Analytics pour suivre les visites
4. **Référencement (SEO)** :
   - Ajouter des meta descriptions personnalisées
   - Optimiser les images
   - Créer un sitemap.xml
5. **Newsletter** : Service comme Mailchimp ou Brevo pour envoyer des actualités
6. **Blog dynamique** : Passer à un CMS simple comme Wordpress ou Webflow pour gérer facilement les articles

## 🔧 Support technique

Pour toute modification complexe ou question :
- Consultez la documentation HTML/CSS en ligne
- Utilisez un éditeur comme [VS Code](https://code.visualstudio.com) avec extensions HTML/CSS
- Pour des changements majeurs, consultez un développeur web

## 📊 Technologies utilisées

- **HTML5** : Structure des pages
- **CSS3** : Styles et animations (variables CSS, flexbox, grid)
- **JavaScript** : Animations au scroll (Intersection Observer), smooth scroll
- **Fonts** : Google Fonts (Crimson Pro, DM Sans)
- **SVG** : Icônes et illustrations vectorielles

## 📝 Articles de Blog & Stratégie SEO

> **Guide de rédaction** : Consultez `blog/GUIDE-REDACTION-BLOG.md` pour le ton, le style et les bonnes pratiques à adopter pour tous les articles.

### Article 1 : Prévenir les maux de l'hiver à Quéven

**📄 Fichier** : `/blog/prevenir-maux-hiver-queven.html`
**📅 Date** : 31 Décembre 2025
**📏 Longueur** : ~1 300 mots (optimisé E-E-A-T)

**🎯 Stratégie SEO :**

**Mots-clés principaux (ciblés) :**
- `prévenir maux hiver` (titre H1, meta, contenu)
- `rhume hiver` (8 occurrences)
- `grippe` / `grippe hiver` (10 occurrences)
- `infections respiratoires` (7 occurrences)
- `renforcer immunité` / `système immunitaire` (6 occurrences)

**Mots-clés SEO local :**
- `Quéven` (6 occurrences) - localisation prioritaire
- `Bretagne` (4 occurrences) - contexte régional
- `pharmacie Quéven` (meta description)
- `pharmacienne Quéven` (référence à Laure)

**Mots-clés longue traîne (questions naturelles) :**
- "Comment éviter d'attraper un rhume cet hiver ?"
- "Quelle vitamine prendre pour renforcer son immunité en hiver ?"
- "Les remèdes naturels sont-ils vraiment efficaces contre la grippe ?"
- "Combien de temps dure un rhume ou une grippe ?"

**Optimisations techniques :**
- ✅ Meta description 160 caractères avec mots-clés prioritaires
- ✅ Title tag 58 caractères optimisé
- ✅ URL parlante : `prevenir-maux-hiver-queven.html`
- ✅ Structure H1 → H2 (8) → H3 (4) avec mots-clés
- ✅ Section FAQ (4 questions) pour Featured Snippets Google
- ✅ Liens internes vers services (vaccination, produits naturels)
- ✅ Personnalisation avec "Laure" (pharmacienne)

---

### Article 2 : Vaccination à l'âge adulte - Le guide pratique

**📄 Fichier** : `/blog/vaccination-adulte-guide-pratique.html`
**📅 Date** : 20 Décembre 2025
**📏 Longueur** : ~2 000 mots (optimisé E-E-A-T)

**🎯 Stratégie SEO :**

**Mots-clés principaux (ciblés) :**
- `vaccination adulte` (titre H1, meta, contenu)
- `vaccin adulte` (7 occurrences)
- `rappel vaccinal` (12 occurrences)
- `calendrier vaccinal adulte` (5 occurrences)

**Mots-clés secondaires :**
- `vaccin HPV` (8 occurrences)
- `vaccination grossesse` (6 occurrences)
- `vaccin coqueluche adulte` (5 occurrences)
- `vaccin zona` (3 occurrences)
- `vaccin grippe` (4 occurrences)
- `immunité collective` (2 occurrences)

**Mots-clés longue traîne (questions naturelles) :**
- "Pourquoi se faire vacciner adulte ?"
- "Quel vaccin à 25 ans ?"
- "Quel vaccin à 45 ans ?"
- "Quel vaccin à 65 ans ?"
- "Vaccin HPV pour les garçons ?"
- "Peut-on se faire vacciner enceinte ?"

**Optimisations techniques :**
- ✅ Meta description 159 caractères avec mots-clés prioritaires
- ✅ Title tag optimisé
- ✅ URL parlante : `vaccination-adulte-guide-pratique.html`
- ✅ Structure H1 → H2 (9) → H3 (12) avec mots-clés
- ✅ Section FAQ (5 questions) pour Featured Snippets Google
- ✅ Liens internes vers services (vaccination)
- ✅ Liens internes vers contact
- ✅ Personnalisation avec "Laure" (pharmacienne)

**Cibles d'audience :**
- Adultes 25-45 ans (rappels vaccins)
- Parents d'adolescents (vaccin HPV)
- Femmes enceintes (vaccination grossesse)
- Seniors 65+ (vaccins spécifiques)
- Grand public recherchant info sur calendrier vaccinal

**Objectifs de ranking :**
- Position 1-5 pour "vaccination adulte" + localisation
- Featured Snippet pour questions FAQ sur rappels
- Recherches "quand faire rappel vaccin"
- Longue traîne "vaccination grossesse", "vaccin HPV garçon"

---

### Articles masqués (non publiés)

Les articles suivants sont commentés dans `blog-v2.html` et n'apparaissent pas sur le site :

1. **Les bienfaits de la phytothérapie** (20 Déc 2024) - 🌿
2. **Protéger sa peau en hiver** (10 Déc 2024) - 🧴
3. **Nouveau : Service Drive disponible** (1 Déc 2024) - 🚗
4. **Nos engagements pour votre santé** (15 Nov 2024) - 💚

**Pour les réactiver :** Supprimer les balises `<!--` et `-->` autour de chaque article dans `blog-v2.html`.

---

## 📝 Historique des modifications

### 31 Décembre 2025
- ✅ Ajout de l'article "Vaccination à l'âge adulte : le guide pratique"
- ✅ Masquage de 4 articles non publiés dans blog-v2.html
- ✅ Configuration des liens réseaux sociaux (Instagram & Facebook)
- ✅ Ajustement des tailles d'icônes :
  - Logo navigation : 48×48px (agrandi de 40px)
  - Icônes sociales footer : 30×30px (agrandi de 20px)
  - Correction du rectangle Instagram : 20×20px (pour rendu correct)
  - Autres icônes SVG : 30×30px
- ✅ Amélioration visuelle footer : phrase signature en beige chaud (#F5E6D3)
- ✅ Ajout de la carte Google Maps interactive sur la page contact
- ✅ Documentation complète dans README.md
- ✅ **Site prêt pour mise en ligne**

### Prochaines étapes suggérées
- [ ] Créer l'article "Les bienfaits de la phytothérapie"
- [ ] Créer l'article "Protéger sa peau en hiver"
- [ ] Ajouter de vraies photos de la pharmacie
- [ ] Configurer un nom de domaine personnalisé
- [ ] Optimiser meta descriptions de tous les articles

---

**Site créé pour la Pharmacie Charnal - Quéven (56530)**
*Version 2 - Janvier 2025*
*Design: Wellness Minimal Raffiné*
*Dernière mise à jour : 31 Décembre 2025*
