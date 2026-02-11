# CLAUDE.md - Site Web Pharmacie Charnal

> Instructions spécifiques pour le développement et la maintenance du site web.
> Pour les règles de contenu, ton de voix et pédagogie, voir `/Pharma/CLAUDE-Pharma.md`

---

## Configuration GitHub Pages

**Repository:** `https://github.com/Marcvrick/Pharmacie-Charnal`
- **Branche principale:** `main` (déploiement automatique)
- **Branche de travail:** `pharmacie-charnal`
- **GitHub Pages:** Activé sur `main`

**Custom Domain:**
- **URL:** `www.pharmaciecharnal.com`
- **Fichier CNAME:** Contient `www.pharmaciecharnal.com`
- **DNS:** CNAME → `marcvrick.github.io`
- **HTTPS:** Activé

**Workflow Git:**
```bash
git checkout pharmacie-charnal
git add . && git commit -m "Message" && git push origin pharmacie-charnal
# Déployer: merge sur main
git checkout main && git merge pharmacie-charnal && git push origin main
git checkout pharmacie-charnal
```

---

## Charte Graphique

### Palette de Couleurs

```css
:root {
    --sage: #7C9885;           /* Vert naturel principal */
    --sage-light: #9DB3A4;
    --sage-dark: #5F7A68;
    --teal: #2D5F5D;           /* Teal professionnel */
    --teal-dark: #1E4644;
    --blue: #4A7C8E;           /* Bleu confiance */
    --cream: #F5F1E8;          /* Crème chaleureux */
    --white: #FFFFFF;
    --black: #1A1A1A;
    --accent: #b4a6d7;         /* Lavande "Au Comptoir" */
    --accent-hover: #9b8bc4;
}
```

**Dashboard Ventes (palette spécifique):**
- Fond: `#FAF8F5` | Cartes: `#FFFFFF` | Bordures: `#E8E3DA`
- Titres: `#2D5F5D` | Secondaire: `#7C9885` | Complémentaire: `#4A7C8E`
- Positif: `#50A686` | Warning: `#FF9F5A` | Alerte: `#C0392B`

### Typographie

- **Headings:** Georgia, Crimson Pro, serif
- **Body:** -apple-system, San Francisco, DM Sans, sans-serif

---

## Structure des Fichiers

**Pages principales:**
```
index.html, histoire.html, services.html, blog.html, contact.html
mentions-legales.html, donnees-personnelles.html
```

**Blog:** `blog/*.html`
**Marques:** `Nos-marques/*.html`
**Quiz:** `Quizzes/*.html`
**Assets:** `images/`, `style.css`, `style-v2.css`, `animations.js`

---

## Règles de Contenu Web

### Marques Approuvées

**RÈGLE:** Seules les marques réellement vendues peuvent être mentionnées.

**Cosmétiques:** Bioderma, La Roche-Posay, Avène, Nuxe, La Rosée, Mustela, Klorane
**Compléments:** PiLeJe, Arkopharma, Boiron, Aragan, Nat&Form, Bion 3, Biogaran

**❌ Ne JAMAIS inventer de marques**

### CTAs (Calls-to-Action)

**✅ Autorisé:** "Passez nous voir", "Venez en pharmacie", "N'hésitez pas à venir"
**❌ Interdit:** "Contactez-nous", "Appelez-nous", "Prenez rendez-vous"

### Formulations Naturelles

**✅** "Chez nous", "Notre pharmacie", "Nous proposons"
**❌** "À la Pharmacie Charnal", "La Pharmacie Charnal propose..."

### Informations Pharmacie

- **Adresse:** 32 Place de Toulouse, 56530 Quéven
- **Téléphone:** 02 97 05 09 31
- **Horaires:** Lun-Ven 9h-12h30/14h-19h15 | Sam 9h-12h30 | Dim fermé
- **Instagram:** `@pharmaciecharnalqueven`
- **Facebook:** `/pharmaciecharnal`

---

## Optimisation IA (Blog)

### Règles Obligatoires

1. **Questions en H2/H3:** Au moins 50% doivent être des questions explicites
   - ✅ "Comment protéger sa peau du froid breton ?"
   - ❌ "Protection peau hiver"

2. **FAQ Schema:** Chaque article doit inclure un markup FAQ (3-5 Q&A)
   ```html
   <script type="application/ld+json">
   {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [...]}
   </script>
   ```

3. **Hyper-localisation:** Mentionner Quéven, Bretagne, Morbihan, climat océanique

4. **Crédibilité:** Mécanismes biologiques, dosages précis, noms scientifiques

### robots.txt

Autoriser: GPTBot, PerplexityBot, Claude-Web, Google-Extended

---

## Spécifications Techniques

### Google Analytics

**ID:** `G-2Q64V6B0QE`

Code à insérer dans `<head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2Q64V6B0QE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-2Q64V6B0QE');
</script>
```

### Carte Leaflet

- **Leaflet:** v1.9.4 (sans integrity hash)
- **PapaParse:** v5.4.1
- **Données:** `professionnels-sante-queven-carte.csv`
- **Markers:** Pharmacie en rouge, autres en bleu

### CSS - Règles Critiques

**Footer Navigation (mobile):**
```css
@media (max-width: 767px) {
    .footer-col:nth-child(2) { display: none; }
}
```

**Copyright visible:** `color: var(--white); opacity: 0.8;`

**Boutons navigation:** `background: linear-gradient(135deg, var(--cream-dark), var(--beige));`

### Fichiers CSS

- `style-v2.css`: Pages principales, pages marques
- `style.css`: Blog, pages secondaires

---

## Accents Français (CRITIQUE)

Vérifier systématiquement:
- ✅ **Quéven** (pas "Queven")
- ✅ **Découvrez**, **française**, **expérience**

Emplacements prioritaires: `<meta description>`, header, footer

---

## Synchronisation Titres Blog

Quand on modifie un titre d'article, mettre à jour:
1. Dans l'article: `<title>`, meta tags, Schema.org, `<h1>`
2. Dans `blog.html`: carte article
3. Dans autres articles: navigation "Article précédent/suivant"

---

## Ordre Services (Homepage)

1. Délivrance d'ordonnances
2. Parapharmacie
3. Vaccinations
4. Produits naturels
5. Matériel médical
6. **Livraison à domicile** (toujours en dernier)

---

## Quiz

**Design (HIMS-inspired):**
- Fonts: Fraunces (display) + DM Sans (body)
- Boutons: fond teal-pro, radius 8px
- Variables CSS pastels + spacing 8pt

**Disponibles:** quiz-soin-peau.html ✅
**En préparation:** Produits naturels, Compléments, Automédication

---

## Checklist Avant Déploiement

- [ ] Google Analytics (G-2Q64V6B0QE) dans `<head>`
- [ ] Images avec attribut `alt`
- [ ] Liens internes relatifs
- [ ] Mobile menu présent
- [ ] Marques vérifiées (pas d'invention)
- [ ] CTAs → venir en pharmacie
- [ ] Footer complet avec mentions légales
- [ ] Footer navigation masquée sur mobile
- [ ] Copyright visible (blanc)
- [ ] Accents français corrects
- [ ] Tester en local avant push

---

## Commandes Rapides

```bash
# Test local
python3 -m http.server 8000

# Déployer
git checkout pharmacie-charnal
git add . && git commit -m "Message" && git push origin pharmacie-charnal
git checkout main && git merge pharmacie-charnal && git push origin main
git checkout pharmacie-charnal
```

---

## Ressources

- **Leaflet.js:** https://leafletjs.com/reference.html
- **GitHub Pages:** https://docs.github.com/pages
- **Parent instructions:** `/Pharma/CLAUDE-Pharma.md`

---

*Dernière mise à jour: Février 2026*
