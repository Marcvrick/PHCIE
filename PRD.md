# PRD - Site Web Pharmacie Charnal

**Version:** 1.0
**Date:** 2 février 2026
**Statut:** Production
**URL:** www.pharmaciecharnal.com

---

## 1. Vision & Objectifs

### Vision
Créer une présence digitale moderne et accessible pour la Pharmacie Charnal, renforçant sa position de pharmacie de proximité à Quéven tout en optimisant sa visibilité sur les moteurs de recherche classiques et les assistants IA.

### Objectifs Business
| Objectif          | KPI                                | Cible              |
| ----------------- | ---------------------------------- | ------------------ |
| Visibilité locale | Position Google "pharmacie Quéven" | Top 1              |
| Trafic organique  | Visites mensuelles                 | 500+               |
| Engagement blog   | Pages vues articles                | 100+/article       |
| Recrutement       | Candidatures via site              | 2-5/an             |
| AI Search         | Citations ChatGPT/Perplexity       | Présence régulière |

### Objectifs Utilisateur
- Trouver rapidement les horaires et coordonnées
- Découvrir les services proposés
- Accéder aux informations de pharmacies de garde
- Lire des conseils santé fiables et localisés

---

## 2. Personas

### Persona 1: Marie, 68 ans - Patiente régulière
- **Contexte:** Retraitée à Quéven, cliente fidèle depuis 15 ans
- **Besoins:** Vérifier les horaires, trouver la pharmacie de garde le dimanche
- **Comportement digital:** Utilise Google sur tablette, peu à l'aise avec le web
- **Attentes:** Site simple, texte lisible, numéro de téléphone visible

### Persona 2: Thomas, 35 ans - Nouveau résident
- **Contexte:** Vient d'emménager à Quéven avec sa famille
- **Besoins:** Trouver une pharmacie proche, découvrir les services (vaccinations, livraison)
- **Comportement digital:** Recherche Google/Maps, consulte les avis
- **Attentes:** Informations complètes, professionnalisme, modernité

### Persona 3: Sophie, 28 ans - Préparatrice en pharmacie
- **Contexte:** Cherche un emploi dans le secteur Lorient
- **Besoins:** Découvrir l'ambiance de travail, postuler facilement
- **Comportement digital:** Indeed, LinkedIn, sites d'entreprise
- **Attentes:** Page recrutement détaillée, valeurs de l'équipe

---

## 3. Périmètre Fonctionnel

### 3.1 Pages Principales (MVP - Livré)

| Page | URL | Statut | Description |
|------|-----|--------|-------------|
| Accueil | index.html | ✅ Live | Présentation, services, CTA |
| Services | services.html | ✅ Live | Détail des 6 services |
| Notre Histoire | histoire.html | ✅ Live | Timeline 40 ans, équipe |
| Contact | contact.html | ✅ Live | Horaires, carte, téléphone |
| Pharmacies de garde | pharmacie-de-garde-*.html | ✅ Live | Planning gardes secteur |
| Nos Marques | nosmarques.html | ✅ Live | Catalogue marques |
| Blog | blog.html | ✅ Live | Liste des articles |
| Recrutement | recrutement-*.html | ✅ Live | Offre préparatrice |
| Mentions légales | mentions-legales.html | ✅ Live | Conformité |
| Données personnelles | donnees-personnelles.html | ✅ Live | RGPD |

### 3.2 Articles de Blog (6 publiés)

| Article | Thématique | Date |
|---------|------------|------|
| Prévenir les maux d'hiver | Immunité | Déc 2025 |
| Vaccination adulte | Prévention | Déc 2025 |
| Professionnels santé Quéven | Guide local | Déc 2025 |
| Détox après les fêtes | Nutrition | Jan 2026 |
| Humidité et douleurs articulaires | Rhumatologie | Jan 2026 |
| Peau sèche hiver breton | Dermocosmétique | Jan 2026 |

### 3.3 Fonctionnalités Techniques

| Fonctionnalité | Statut | Notes |
|----------------|--------|-------|
| Responsive mobile | ✅ | Breakpoint 767px |
| Menu hamburger | ✅ | JavaScript toggle |
| Animations scroll | ✅ | IntersectionObserver |
| Carte Leaflet | ✅ | Page professionnels santé |
| Schema.org | ✅ | Pharmacy, Blog, JobPosting |
| Open Graph | ✅ | Toutes les pages |
| JSON Feed | ✅ | feed.json pour AI |
| HTTPS | ✅ | GitHub Pages |

---

## 4. Spécifications Techniques

### 4.1 Stack Technique
- **Type:** Site statique (HTML/CSS/JS)
- **Hébergement:** GitHub Pages
- **Repository:** github.com/Marcvrick/Pharmacie-Charnal
- **Domaine:** www.pharmaciecharnal.com
- **Déploiement:** Push sur main = déploiement auto

### 4.2 Performance Cibles
| Métrique | Cible | Actuel |
|----------|-------|--------|
| Lighthouse Performance | >90 | À mesurer |
| First Contentful Paint | <1.5s | À mesurer |
| Largest Contentful Paint | <2.5s | À mesurer |
| Time to Interactive | <3s | À mesurer |

### 4.3 Compatibilité Navigateurs
- Chrome (2 dernières versions)
- Safari (2 dernières versions)
- Firefox (2 dernières versions)
- Edge (2 dernières versions)
- Safari iOS
- Chrome Android

### 4.4 Conformité RGPD
| Élément | Statut | Action |
|---------|--------|--------|
| Cookies | ✅ Aucun | - |
| Analytics | ✅ Aucun | - |
| Fonts | ✅ Système | Fallback actif |
| Google Maps | ⚠️ Notice | Notice RGPD affichée |
| Formulaire | ❌ Absent | Pas de collecte |

---

## 5. Design System

### 5.1 Identité Visuelle
**Style:** "Wellness Minimal Raffiné"

### 5.2 Palette de Couleurs
```
Principale:
- Sage: #7C9885 (vert naturel)
- Sage Light: #9DB3A4
- Sage Dark: #5F7A68
- Teal: #2D5F5D (professionnel)
- Blue: #4A7C8E (confiance)

Neutres:
- Cream: #F5F1E8
- Cream Dark: #E8DCC8
- Beige: #D9C9B0
- Charcoal: #2C3E50 (texte)

Accent:
- Lavande: #b4a6d7 (blog)
```

### 5.3 Typographie
- **Titres:** Georgia, Crimson Pro (fallback), serif
- **Corps:** -apple-system, DM Sans (fallback), sans-serif
- **Taille base:** 18px (accessibilité seniors)

---

## 6. Roadmap

### Phase 1: Fondations (Terminé)
- [x] Structure site 10 pages
- [x] Design responsive
- [x] SEO on-page
- [x] Déploiement GitHub Pages
- [x] Domaine custom

### Phase 2: Contenu (En cours)
- [x] 6 articles blog publiés
- [ ] Photos réelles pharmacie/équipe
- [ ] Télécharger fonts .woff2
- [ ] 6 articles supplémentaires (calendrier éditorial)

### Phase 3: Visibilité (Planifié)
- [ ] Google Search Console
- [ ] Google My Business optimisé
- [ ] Suivi positions SEO
- [ ] Monitoring AI Search mensuel

### Phase 4: Fonctionnalités (Futur)
- [ ] Formulaire contact (Formspree)
- [ ] Système RDV (Doctolib widget)
- [ ] Analytics RGPD-friendly (Plausible)
- [ ] Newsletter (optionnel)

---

## 7. Métriques de Succès

### 7.1 Métriques Quantitatives
| Métrique | Baseline | Cible 6 mois | Cible 12 mois |
|----------|----------|--------------|---------------|
| Visites/mois | 0 | 300 | 600 |
| Pages/session | - | 2.5 | 3.0 |
| Taux rebond | - | <60% | <50% |
| Position "pharmacie Quéven" | ? | Top 5 | Top 3 |

### 7.2 Métriques Qualitatives
- Citations dans réponses ChatGPT/Perplexity (suivi manuel mensuel)
- Retours clients en pharmacie ("j'ai vu sur votre site...")
- Candidatures reçues via page recrutement

---

## 8. Risques & Mitigations

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Google Maps non RGPD | Moyen | Faible | Notice claire affichée |
| Contenu obsolète | Moyen | Moyen | Planning éditorial |
| Temps de maintenance | Faible | Moyen | Documentation complète |
| Changement algo Google | Moyen | Moyen | Diversification AI Search |

---

## 9. Annexes

### Documents connexes
- `README.md` - Documentation technique
- `CLAUDE-Pharma.md` - Instructions rédactionnelles
- `blog/GUIDE-REDACTION-BLOG.md` - Guide voix de marque
- `blog/PLANNING-BLOG-PHARMACIE.md` - Calendrier éditorial

### Contacts
- **Pharmacie:** Laure Charnal - 02 97 05 09 31
- **Technique:** Repository GitHub

---

*Dernière mise à jour: 6 février 2026*
