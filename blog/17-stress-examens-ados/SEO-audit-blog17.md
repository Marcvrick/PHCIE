---
title: SEO Audit — Blog 17 Stress Examens Ados
tags: [seo, pharmacie-charnal, blog, audit]
category: SEO
type: audit
created: 2026-05-12
url: https://www.pharmaciecharnal.com/blog/17-stress-examens-ados/stress-examens-ados-queven.html
---

# SEO Audit — Blog 17 / Stress des examens ados

**URL:** https://www.pharmaciecharnal.com/blog/17-stress-examens-ados/stress-examens-ados-queven.html
**Date d'audit:** 2026-05-12

## Score

```
Overall:         79/100  ████████░░

On-Page SEO:     78/100  ████████░░
Content Quality: 85/100  █████████░
Technical:       80/100  ████████░░
Schema:          62/100  ██████░░░░  ← principal levier de progression
Performance:     70/100  ███████░░░
Images:          85/100  █████████░
AI Readiness:    90/100  █████████░
```

---

## Issues par priorité

### CRITICAL

**1. FAQPage schema imbriqué dans MedicalWebPage — bloque les rich results**

La configuration `MedicalWebPage.mainEntity → FAQPage` n'est pas reconnue par Google pour les rich results. Google exige un `FAQPage` de premier niveau (top-level `@type`) dans un `<script type="application/ld+json">` séparé.

**Fix appliqué:** FAQPage extrait en schema indépendant.

---

### HIGH

**2. BlogPosting `author @type: "Person"` incorrect**

"Équipe Pharmacie Charnal" est une Organisation. Utiliser `@type: "Person"` avec un nom générique de team dilue les signaux E-E-A-T pour Google Search et les LLMs parseurs.

**Fix appliqué:** `@type: "Organization"`, `"jobTitle"` supprimé.

**3. Titre trop long (90 caractères)**

Google tronque à ~55–60 chars. La partie affichée s'arrête avant "| Pharmacie Charnal Quéven" — le branding local est coupé en SERP.

Titre actuel (90 chars):
> Stress des examens: comment aider les ados (et les parents) | Pharmacie Charnal Quéven

Suggestion (62 chars):
> Stress des examens ados: que faire vraiment? | Pharmacie Charnal

**Non modifié** — décision éditoriale à valider avant changement. Si tu gardes le titre actuel, le tronquage ne nuit pas au ranking (les mots-clés sont front-loaded) mais réduit le CTR local.

---

### MEDIUM

**4. `og:image:alt` manquant** — recommandé par les guidelines d'accessibilité sociale.
**Fix appliqué.**

**5. `og:site_name` manquant** — améliore l'affichage dans certains previews et parseurs LLM.
**Fix appliqué.**

**6. `article:modified_time` manquant** — signal de fraîcheur pour les agrégateurs.
**Fix appliqué.**

**7. Twitter `og:image` pointe vers le blog photo (1204×803)** — l'image OG générée (1200×630) est déjà disponible et mieux dimensionnée pour Twitter Cards summary_large_image.
**Fix appliqué.**

---

### LOW / Règles site

**8. Espacement avant `:` dans titre/H1/meta/schemas** — ` : ` → `:` per CLAUDE.md règle absolue.
**Fix appliqué:** title, H1, meta description, OG tags, Twitter tags, citation_title, breadcrumb HTML, BreadcrumbList schema, MedicalWebPage schema, BlogPosting schema.

**9. `<meta name="keywords">`** — ignoré par Google depuis 2009. Pas nuisible mais inutile. Non supprimé (inoffensif).

**10. FAQ HTML — balisage non sémantique** — `<p class="faq-question">` au lieu de `<details>/<summary>`. Pas d'impact ranking direct, impact accessibilité. À corriger dans une future itération.

---

## Points forts (ne pas toucher)

| Élément | Statut |
|---------|--------|
| Meta description | ✅ présente, bien rédigée, keyword local |
| Canonical | ✅ URL absolue correcte |
| Meta robots | ✅ index, follow |
| Open Graph complet | ✅ type article, published_time, tags |
| Twitter card summary_large_image | ✅ |
| LLM citation meta tags | ✅ avantage concurrentiel rare (citation_author, citation_institution) |
| Hero image width/height/loading="lazy" | ✅ |
| BreadcrumbList JSON-LD | ✅ 3 niveaux, URLs absolues |
| MedicalWebPage schema | ✅ |
| GA4 (G-2Q64V6B0QE) | ✅ |
| ~2800 mots | ✅ au-dessus du seuil santé |
| 50%+ des H2 en questions | ✅ |
| 9 références bibliographiques sourcées | ✅ (INSERM, HAS, ANSES, JAMA, EMA) |
| robots.txt — PerplexityBot, GPTBot, Claude-Web | À vérifier |

---

## Fixes appliqués dans `stress-examens-ados-queven.html`

- [x] FAQPage extrait en schema `<script>` top-level séparé
- [x] BlogPosting author `Person` → `Organization`, `jobTitle` supprimé
- [x] `og:image:alt` ajouté
- [x] `og:site_name` ajouté
- [x] `article:modified_time` ajouté
- [x] Twitter image → OG image (1200×630)
- [x] Espacement `:` corrigé dans tous les tags SEO et schemas

## Non modifié

- Longueur du titre (décision éditoriale)
- `<meta name="keywords">` (inoffensif)
- FAQ HTML markup (travaux futures)
- Corps de l'article (colons dans le texte courant — hors scope SEO)
