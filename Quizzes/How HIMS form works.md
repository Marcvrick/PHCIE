

# [https://www.hims.com/g/i/sh/intro-transition-step](https://www.hims.com/g/i/sh/intro-transition-step)

Hims create forms to assess the client's need online. can you describe how they do it, what is their intent?  how it can be dusplicated for a pharmacy who want to propose offers to clients... and anything that could help me replicate the concept

Hims uses short, guided “quizzes” as medical intake forms to qualify people for specific offers (e.g., hair loss treatments), collect legally required data for telehealth, and nudge users toward a recommended, subscription product path.[^1][^2][^3][^4][^5]

## How Hims’ forms work

Typical flow (hair loss example):

- Entry via “Start my hair quiz” or “Free hair quiz” CTA that promises a clear benefit (regrow hair, personalized plan, etc.), not “medical form.”[^2][^4][^6]
- Step 1: Define goals and current situation: what your hair looks like now, what you want it to look like, where you’re losing hair.[^5][^1]
- Step 2: Treatment preference: choose if you want FDA‑approved prescription options or non‑Rx, but they explain you’re not locked in; it’s to help them recommend the right product.[^1]
- Step 3: Structured medical questionnaire:
    - Sex and gender, medical and mental health history, current meds/supplements, allergies, prior hospitalizations/surgeries.
    - Specific symptom questions: location of hair loss, scalp issues, previous topical treatments, sexual side effects, etc.[^1]
- Step 4: Safety/compliance checks: they gather enough history for a licensed prescriber to evaluate and legally issue (or refuse) a prescription.[^1]
- Step 5: Preference \& matching: user can choose “what the platform recommends,” “what’s popular,” or ask for more guidance, which lets Hims steer toward a specific product bundle and subscription.[^3][^1]
- Result: asynchronous teleconsultation (doctor reviews the answers, may ask questions), then discreet shipment of treatment and ongoing follow‑ups/check‑ins.[^7][^3]

Key characteristics:

- Multi‑step, low‑friction, visually simple, with only a few questions per screen.[^5][^1]
- Starts with goals and visuals (how your hair looks / should look), then only later goes into “boring” medical details.[^5][^1]
- Strong framing around “quick quiz” and “personalized plan,” not “medical questionnaire,” to keep conversion high.[^4][^6][^2]


## Their business and clinical intent

What they’re trying to achieve with these forms:

- Qualify and segment quickly
    - Identify who is likely to benefit from treatment vs. who should be excluded or referred (contraindications, severe conditions, red flags).[^1]
    - Segment by goal (exploring vs. ready to start ASAP; slowing receding hairline vs. regrowing density) to tailor messaging and offers.[^5][^1]
- Generate personalized offers that feel “doctor‑recommended”
    - Use answers to auto‑suggest a specific regimen: finasteride, minoxidil, combo products, hybrids, etc., often as a subscription.[^6][^2][^3]
    - Give the impression of a bespoke plan while routing most people into a small number of standardized protocols.[^3][^1]
- Satisfy telehealth and legal requirements
    - Collect validated anamnesis so a prescriber can safely decide and document their decision.[^1]
    - Standardize the intake so every patient is evaluated with the same checklist, reducing risk and increasing efficiency.[^1]
- Create a conversion funnel and retention loop
    - Turn anonymous visitors into identified leads with structured data attached (symptoms, concerns, budget level, etc.).[^2][^4]
    - Build lifecycle communications: progress tracking, check‑ins at 3–6 months, and reminders to stay consistent with treatment.[^7][^3]


## How a pharmacy could duplicate the concept

You can repurpose the same logic for a French officine (especially for para‑pharmacie and “protocoles” around chronic topics).

1) Choose 2–3 “flagship” topics
Start where you already have margin + clear protocols:

- Hair loss (chute de cheveux / alopécie légère).
- Acne / peau grasse.
- Sleep / stress.
- Intimate health (cystite récidivante, sécheresse vaginale).

For each topic, your quiz is both:

- A structured clinical/needs intake.
- A product recommendation engine that ends in a clear offer (pack, routine, or RDV pharmacien).

2) Copy the funnel structure

For each topic, design a flow with 4–5 steps:

- Step 1: Goals \& self‑image (very light, aspirational)
    - “What is your main goal?” (Ex: “Stop hair shedding,” “Regrow density,” “Strengthen fragile hair.”)
    - “When did you first notice the problem?”
This mimics Hims’ “what your hair looks like now vs. what you want.”[^5][^1]
- Step 2: Severity \& pattern
    - Small visual scale (1–4 pictures or descriptions) for severity.
    - Localisation (temples, vertex, diffuse; T‑zone vs. cheeks for acne, etc.).
    - “Have you already tried something? If yes, what and for how long?”[^1]
- Step 3: Health/safety questions (simpler than telehealth, but still robust)
Adapted to officine context and HAS/ANSM guidance; e.g.:
    - Age, sex, known conditions (thyroid disease, recent childbirth, chemo, etc.).
    - Current medications, allergies.[^1]
    - “Red flag” questions that trigger “please see a doctor” rather than self‑medication (sudden hair loss patches, severe weight loss, fever, suicidal ideation for sleep, etc.).
- Step 4: Preferences \& constraints
    - “What is most important to you?” (Natural, quick results, minimal side effects, budget).
    - Form factor (tablets, topicals, shampoos, gummies), time willingness (complete routine vs. minimum viable effort).[^1]
- Step 5: Outcome and CTA
    - Display 1–2 recommended “protocols” (e.g., “Routine Essentielle 3 mois” + “Routine Premium 3 mois”).
    - Clear next step:
        - “Réserver un RDV conseil de 15 min à la pharmacie.”
        - “Recevoir votre ordonnance de produits par email avec un code promo / click-and-collect.”
        - “Télécharger votre plan personnalisé (PDF) et venir en parler en officine.”

3) Technical implementation options

You do not need a full SaaS:

- No‑code form builders
    - Typeform, Tally, Jotform etc. can reproduce the multi‑step visual style of Hims quizzes.[^8]
    - Logic rules let you branch questions based on red flags and end with different recommendation screens.
- Simple stack for you
    - Web page (WordPress / Webflow / simple landing) per topic with “Commencer le quiz gratuit” CTA.
    - Embedded Typeform/Tally for the quiz.
    - On submission:
        - Show dynamic “result page” with your curated pack.
        - Send answers and segmentation tags into a CRM (Brevo, MailerLite, etc.) for follow‑up emails and reminders.
- Data usage
    - Use quiz data to tag people (e.g., “HairLoss_Mild,” “Budget_Low,” “Prefers_Natural”) and send tailored sequences: content + offers + reminder to re‑do the quiz at 3 months, mirroring Hims’ check‑in logic.[^7][^3]


## Practical adaptation to a French pharmacy

Some concrete ways to make this compliant and credible in your officine context:

- Medical vs. commercial boundaries
    - Make it explicit: “Ce questionnaire ne remplace pas un avis médical. En cas de doute, nous vous orienterons vers un médecin.”
    - Build a decision tree where certain answers end with “Arrêt du parcours + conseil de consulter.”
- Professional positioning
    - Present it as “Bilan personnalisé” (Bilan chute de cheveux, Bilan peau) prepared by your pharmacy.
    - At the end, propose either:
        - Pack parapharmacie + conseils hygiène de vie.
        - Option “RDV pharmacien” for more complex cases.
- Offer design
    - For each segment, pre‑define:
        - 1–2 product bundles (shampoo + lotion + complément, etc.).
        - 2–3 key conseils (nutrition, fréquence lavage, etc.).
        - A recommended follow‑up time (e.g., “Refaire le bilan dans 8–12 semaines”).[^7]
- Follow‑up loop
    - After 2–3 months, send a short “check‑in” mini‑quiz: “Avez‑vous noté une amélioration ?” + “Souhaitez‑vous ajuster votre routine ?”
    - This mirrors Hims’ hair “check‑in” that encourages persistence and retention.[^7]


## Steps for you to start this week

1) Pick one topic (hair loss is ideal) and map 10–15 key questions in the four blocks: goals, severity, health, preferences.[^5][^1]
2) Turn them into a Typeform/Tally with logic jumps and 4–5 steps maximum.[^8]
3) Define 3–4 standard recommendation “profiles” and link each to a specific response combination.
4) Build a simple landing page “Bilan chute de cheveux gratuit en 3 minutes” with a clear benefit‑oriented headline, similar to “Start my hair quiz.”[^4][^2]
5) Test in‑pharmacy (QR code on the comptoir, flyers near dermocosmetics) and online (website, Instagram bio link), then refine based on response rates and sales.

If you tell me which first theme you want to launch (hair, acne, sommeil, etc.), I can draft a ready‑to‑paste full questionnaire plus 2–3 product/routine archetypes tailored to your officine.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^9]</span>

<div align="center">⁂</div>

[^1]: https://stylegirlfriend.com/hair-loss-treatment-online/

[^2]: https://www.facebook.com/wearehims/videos/start-my-hair-quiz-/1644383586911022/

[^3]: https://www.hims.com/blog/how-to-take-hair-growth-progress-photos

[^4]: https://www.hims.com/c/hl/goals

[^5]: https://www.youtube.com/watch?v=VWJyMD6Jsko

[^6]: https://www.facebook.com/wearehims/videos/start-my-hair-quiz-/906115051795972/

[^7]: https://www.hims.com/hair-loss/check-in

[^8]: https://www.jotform.com/blog/patient-onboarding/

[^9]: https://downloads.asam.org/sitefinity-production-blobs/docs/default-source/guidelines/the-asam-appropriate-use-of-drug-testing-in-clinical-addiction-medicine-full-document.pdf

[^10]: https://www.sec.gov/Archives/edgar/data/1357671/000121390020008255/0001213900-20-008255.txt

[^11]: https://www.facebook.com/groups/babelistas/posts/5437569756262032/

[^12]: https://www.hims.com/blog/everything-you-need-to-know-about-the-hair-growth-process-regrowing-hair

[^13]: https://hangzonecare.com/flawless-client-onboarding-process/

[^14]: https://www.hims.com/blog/pull-test-hair

[^15]: https://www.scribd.com/document/983377168/HIMS-Functionalities-List

