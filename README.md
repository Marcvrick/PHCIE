# Site Web - Pharmacie Charnal

Site internet statique pour la Pharmacie Charnal à Quéven (56530).
Déployé sur GitHub Pages : **www.pharmaciecharnal.com**

---

## 📁 Structure du site

```
website-pharmacie-charnal/
├── index.html              # Accueil
├── histoire.html           # Notre Histoire
├── services.html           # Services
├── marques.html            # Nos Marques (ancres: #cosmetiques, #complements, #premiers-soins)
├── blog.html               # Au Comptoir (liste des articles)
├── contact.html            # Contact
├── recrutement-preparatrice.html  # Offre d'emploi préparatrice
├── mentions-legales.html   # Mentions légales
├── donnees-personnelles.html  # Données personnelles
├── style.css               # Styles principaux
├── animations.js           # Animations scroll
├── favicon.svg             # Favicon
├── robots.txt              # Directives crawlers
├── sitemap.xml             # Plan du site
├── feed.json               # JSON Feed pour AI Search
├── CNAME                   # Custom domain (www.pharmaciecharnal.com)
├── professionnels-sante-queven-carte.csv  # Données carte Leaflet
├── blog/                   # Articles de blog
│   ├── GUIDE-REDACTION-BLOG.md            # Guide rédactionnel Laure
│   ├── PLANNING-BLOG-PHARMACIE.md         # Planning éditorial
│   ├── detox-apres-fetes-mythe-realite-queven.html
│   ├── humidite-douleurs-articulaires-queven.html
│   ├── prevenir-maux-hiver-queven.html
│   ├── professionnels-sante-queven-2026.html  # Carte Leaflet interactive
│   ├── proteger-peau-seche-hiver-breton-queven.html
│   └── vaccination-adulte-guide-pratique.html
├── fonts/                  # Fonts auto-hébergées (RGPD) - À TÉLÉCHARGER
└── images/                 # Logo et ressources visuelles
```

---

## 🎨 Design & Identité Visuelle

**Design "Wellness Minimal Raffiné"** - moderne, apaisant et accessible

### Palette de Couleurs

```css
:root {
    /* Couleurs principales */
    --sage: #7C9885;          /* Vert naturel principal */
    --sage-light: #9DB3A4;    /* Vert clair */
    --sage-dark: #5F7A68;     /* Vert foncé */
    --teal: #2D5F5D;          /* Teal professionnel */
    --blue: #4A7C8E;          /* Bleu confiance */
    --cream: #F5F1E8;         /* Crème chaleureux */
    --cream-dark: #E8DCC8;    /* Crème foncé */
    --beige: #D9C9B0;         /* Beige naturel */
    --white: #FFFFFF;
    --charcoal: #2C3E50;      /* Texte principal */

    /* Accent Blog "Au Comptoir" */
    --accent: #b4a6d7;        /* Lavande */
    --accent-hover: #9b8bc4;
    --accent-active: #8270b1;
}
```

### Typographie

- **Headings**: Georgia, "Crimson Pro" (fallback), serif
- **Body**: -apple-system, "DM Sans" (fallback), sans-serif
- **Taille de base**: 18px (accessibilité seniors)

**Note**: Les font files (.woff2) ne sont pas encore ajoutés. Le site utilise les polices système en fallback.

### Navigation & UX

**Ordre des Services (Homepage):**
1. Délivrance d'ordonnances
2. **Parapharmacie**
3. Vaccinations
4. Produits naturels
5. Matériel médical
6. **Livraison à domicile** (toujours en dernier)

**Bouton "Au Comptoir":**
- Couleur distinctive: `#b4a6d7` (lavande)
- Se distingue du reste de la navigation

---

## ⏰ Informations Pharmacie

**Adresse**: 32 Place de Toulouse, 56530 Quéven
**Téléphone**: 02 97 05 09 31
**Email**: *(non public sur le site)*

**Horaires**:
- Lundi-Vendredi: 9h-12h30 / 14h-19h15
- Samedi: 9h-12h30
- Dimanche: Fermé

**Réseaux sociaux**:
- Instagram: https://www.instagram.com/pharmaciecharnalqueven/
- Facebook: https://www.facebook.com/pharmaciecharnal/

---

## 🌐 Déploiement GitHub Pages

### Configuration actuelle

- **Repository**: `https://github.com/Marcvrick/Pharmacie-Charnal`
- **Branche unique**: `main` (travail + déploiement automatique)
- **Custom Domain**: `www.pharmaciecharnal.com` (fichier CNAME)
- **GitHub Pages**: Activé sur branche `main`

### Workflow Git

```bash
# Workflow simplifié - une seule branche
git add [fichiers]
git commit -m "Message descriptif"
git push origin main
```

**Note**: Le site se déploie automatiquement à chaque push sur `main`.

---

## 🔒 Conformité RGPD

### État actuel: ~85% conforme

| Élément | Transfert données | Conformité |
|---------|-------------------|------------|
| **Fonts (Google Fonts)** | ✅ Commentées (fallback système) | ✅ Conforme |
| **Google Maps** | ⚠️ Google US | ⚠️ Notice RGPD présente |
| **Liens sociaux** | ✅ Pas de transfert | ✅ Conforme |
| **Analytics** | ✅ Aucun | ✅ Conforme |
| **Cookies** | ✅ Aucun | ✅ Conforme |

**Point d'attention**: Google Maps (page contact) est le seul service externe. Une notice RGPD claire est affichée.

**Fonts auto-hébergées**: Prévues mais pas encore téléchargées. Le site utilise actuellement les polices système (Georgia, San Francisco, Segoe UI).

---

## 🔍 Optimisation SEO & AI Search

### SEO Classique

✅ **Toutes les pages** disposent de:
- Meta descriptions optimisées (150-160 caractères)
- Schema.org markup (Pharmacy, Blog, FAQPage)
- Open Graph (Facebook) et Twitter Cards
- URLs canoniques
- Structure H1 → H2 → H3 propre

### AI Search Optimization (AEO)

✅ **Articles de blog** optimisés pour ChatGPT, Perplexity, Claude:
- Schema.org MedicalWebPage complet
- FAQ Schema intégré (3-5 Q&A par article)
- Citation meta tags (académique)
- JSON Feed (`feed.json`)
- H2/H3 formulés en questions naturelles
- Hyper-localisation (Quéven, Bretagne, climat océanique)

**Crawlers AI autorisés** dans `robots.txt`:
- GPTBot (OpenAI)
- PerplexityBot
- Claude-Web
- Google-Extended (Gemini)

**Voir** `/blog/GUIDE-REDACTION-BLOG.md` pour les règles d'optimisation complètes.

---

## 📝 Articles de Blog Publiés

**6 articles actuellement en ligne:**

1. **Détox après les fêtes** - `detox-apres-fetes-mythe-realite-queven.html`
2. **Humidité et douleurs articulaires** - `humidite-douleurs-articulaires-queven.html`
3. **Prévenir les maux d'hiver** - `prevenir-maux-hiver-queven.html`
4. **Professionnels de santé à Quéven** - `professionnels-sante-queven-2026.html` (carte Leaflet)
5. **Protéger sa peau sèche** - `proteger-peau-seche-hiver-breton-queven.html`
6. **Vaccination adulte** - `vaccination-adulte-guide-pratique.html`

**Stratégie éditoriale**:
- Ton: Voix de Laure (pharmacienne pédagogue, professionnelle accessible)
- SEO local: Quéven, Bretagne, Morbihan, climat océanique
- E-E-A-T médical: Expertise + sources + mécanismes biologiques
- Optimisé pour AI Search (FAQ, questions naturelles)

---

## 🔧 Fonctionnalités Techniques

### Mobile Menu
- Hamburger icon 3 lignes
- JavaScript toggle
- Présent sur toutes les pages
- ARIA attributes (accessibilité)

### Carte Interactive Leaflet.js
**Fichier**: `blog/professionnels-sante-queven-2026.html`

- Leaflet v1.9.4 (CDN sans integrity hash)
- PapaParse v5.4.1 pour CSV
- Données: `professionnels-sante-queven-carte.csv` (15 professionnels)
- Markers: Pharmacie Charnal rouge, autres professionnels bleus

### Animations (animations.js)
- Fade-in au scroll (IntersectionObserver)
- Parallax léger sur hero sections
- Smooth scroll pour ancres
- Stats counter animation

---

## 📋 Checklist Maintenance

### Avant chaque déploiement (main)

- [ ] Toutes les images ont un attribut `alt`
- [ ] Tous les liens internes fonctionnent
- [ ] Mobile menu présent et fonctionnel
- [ ] Informations contact à jour (adresse, tél, horaires)
- [ ] CTAs invitent à venir en pharmacie (pas "contactez-nous")
- [ ] Marques mentionnées sont vendues en pharmacie
- [ ] robots.txt autorise les crawlers AI
- [ ] Tester sur mobile/tablette
- [ ] Tester en local avant push

### Nouvel article de blog

- [ ] Ajouter le bouton "Article précédent" en bas de l'article (voir modèle ci-dessous)
- [ ] Mettre à jour le bouton dans l'article précédent pour pointer vers le nouveau (si applicable)
- [ ] Ajouter l'article dans blog.html (liste des articles)
- [ ] Mettre à jour sitemap.xml et feed.json

**Modèle bouton "Article précédent"** (à placer après les références, avant `</div></article>`) :
```html
<!-- Navigation article précédent -->
<nav style="margin-top: var(--space-3xl); padding-top: var(--space-xl); border-top: 1px solid var(--beige);">
    <a href="NOM-ARTICLE-PRECEDENT.html" style="display: flex; align-items: center; gap: var(--space-md); padding: var(--space-lg); background: linear-gradient(135deg, var(--cream) 0%, #f9f5ed 100%); border-radius: var(--radius-lg); text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.transform='translateX(-4px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='none';">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        <div>
            <span style="display: block; font-size: var(--text-sm); color: var(--gray); margin-bottom: var(--space-xs);">Article précédent</span>
            <span style="display: block; font-size: var(--text-lg); color: var(--charcoal); font-weight: 600;">TITRE DE L'ARTICLE PRÉCÉDENT</span>
        </div>
    </a>
</nav>
```

### Suivi mensuel AI Search (manuel)

**Process simple (15 min/mois)**:

1. Ouvrir ChatGPT, Perplexity, Claude
2. Poser 3-5 questions clés:
   - "Comment protéger sa peau en hiver en Bretagne ?"
   - "Prévenir la grippe à Quéven pharmacie conseils"
   - "Quelle pharmacie à Quéven pour dermatologie ?"
3. Noter si Pharmacie Charnal est citée
4. Ajuster stratégie si nécessaire

---

## 📚 Documentation Connexe

**Pour travailler sur le site, consulter:**

1. **CLAUDE-Pharma.md** (`/Users/mc/Documents/MarcOS/Pharma/CLAUDE-Pharma.md`)
   - Instructions système pour Claude
   - Règles de rédaction et voix de marque
   - Standards qualité contenu
   - Optimisation AI Search (section complète)

2. **GUIDE-REDACTION-BLOG.md** (`blog/GUIDE-REDACTION-BLOG.md`)
   - Voix de Laure (ton comptoir)
   - Paramètres mesurables (formalité, certitude, rythme)
   - Patterns de phrases types
   - E-E-A-T médical

3. **PLANNING-BLOG-PHARMACIE.md** (`blog/PLANNING-BLOG-PHARMACIE.md`)
   - Calendrier éditorial
   - Idées d'articles

---

## 🎯 Prochaines Étapes Suggérées

**Court terme:**
- [ ] Télécharger font files .woff2 (Crimson Pro + DM Sans)
- [ ] Vérifier cohérence domain (.com vs .fr dans canonical URLs)
- [ ] Créer nouveaux articles blog (calendrier éditorial)

**Moyen terme:**
- [ ] Google Search Console (soumettre sitemap)
- [ ] Google My Business (optimiser fiche)
- [ ] Photos réelles pharmacie et équipe

**Long terme:**
- [ ] Système rendez-vous (Doctolib/Maiia)
- [ ] Formulaire contact (Formspree/Netlify Forms)
- [ ] Analytics léger et RGPD-friendly (Plausible, Fathom)

---

## 💡 Différence CLAUDE-Pharma.md vs README.md

**README.md (ce fichier)**:
- Documentation **POUR HUMAINS** (Dany, équipe)
- Décrit **CE QUI EXISTE** (structure, état actuel, config technique)
- Utilisé **POUR COMPRENDRE** le projet
- Format: Documentation technique classique

**CLAUDE-Pharma.md**:
- Instructions **POUR CLAUDE** (système IA)
- Décrit **COMMENT TRAVAILLER** (règles, voix, workflow, best practices)
- Utilisé **POUR GÉNÉRER DU CONTENU** cohérent et conforme
- Format: Règles et standards systématiques

**Exemple concret:**
- README: "Le bouton Au Comptoir utilise la couleur #b4a6d7"
- CLAUDE-Pharma: "Les CTAs doivent TOUJOURS inviter à venir en pharmacie physiquement"

Les deux fichiers sont complémentaires et doivent rester à jour.

---

**Dernière mise à jour**: Janvier 2026
**Version du site**: Production (main branch)
**Statut**: ✅ En ligne sur www.pharmaciecharnal.com
