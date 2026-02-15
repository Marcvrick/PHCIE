# APP Planning - Pharmacie Charnal

## Description

Application web de gestion du planning, des absences et des vacances pour la Pharmacie Charnal (Queven). Single-page app en HTML/CSS/JS vanilla avec backend Firebase Firestore pour synchronisation temps reel entre appareils.

## URL en ligne

**https://www.pharmaciecharnal.com/planning.html**

## Mots de passe

- **Equipe** (pour entrer dans l'app) : `pharma2026`
- **Manager** (dashboard admin) : `Hutchence23@`

## Equipe actuelle (Fevrier 2026)

- **Laure** — Boss, manager (recoit les notifications, n'apparait pas dans le dropdown employe)
- **Stephanie** — 22h30/semaine (Lun/Mar/Jeu, 9h-18h)
- **Claire** — 35h/semaine
- **Sandrine** — 35h/semaine
- **Titia** — 35h/semaine
- **Melanie Le Bihan** — 35h/semaine (remplace Leila)
- **Mathilde** — 28h/semaine (Lun/Mar/Jeu/Ven)
- **Chloe** — Absente (arret maladie) - retiree du planning jusqu'a nouvel ordre, mais presente dans le dropdown pour acceder a ses vacances
- **Emilie** — Absente (arret maladie) - presente dans le dropdown pour acceder a ses vacances
- **Pascal** — Freelance, disponible a la demande (remplacements ponctuels)

Tous les employes ont acces au module vacances.

## Fonctionnalites

- Planning bi-hebdomadaire (semaine paire/impaire) en lecture seule
- Demandes d'absence (depart anticipe, maladie, conge, echange horaires, autre)
- Analyse d'impact automatique sur l'effectif par tranche horaire
- Systeme de recuperation avec suggestions de creneaux prioritaires
- Recuperation partielle acceptee (solde du affiche, pas de blocage)
- **Recuperation d'heures** : type de demande disponible dans le formulaire d'absence si l'employe a des heures dues. Permet de selectionner des creneaux de recuperation independamment d'une absence.
- **Echange d'heures avec validation pharmacien** : systeme d'echange d'heures entre deux employes avec validation automatique :
  - Laure n'est pas disponible pour les echanges normaux (role de manager/bouche-trou)
  - Verification disponibilite : l'autre employe DOIT etre disponible (pas programmé a cette periode)
  - Blocage si l'autre employe travaille deja → aucun interet a l'echange
  - Verification automatique : il doit toujours y avoir au minimum 1 pharmacien en boutique
  - Alerte si Laure sera la seule pharmacienne en boutique pendant l'echange
  - Blocage automatique si l'echange mettrait la boutique sans pharmacien
- Tableau de bord manager (protege par mot de passe)
- Solde d'heures dues/recuperees par employe (hors Laure)
- Export/import JSON pour sauvegardes
- Notification email via lien Gmail (destinataire: laure.charnal@gmail.com)
- **Synchronisation temps reel** — Toutes les modifications sont visibles instantanement sur tous les appareils
- **Planning des vacances** (tous les employes) :
  - Onglet "Vacances" visible pour tous les employes
  - Calcul automatique des jours acquis selon la loi (2.5 jours ouvrables/mois)
  - Bonus anciennete +2 jours apres 6 ans (convention pharmacie)
  - Formulaire de demande avec calcul automatique des jours ouvrables (weekends + jours feries exclus)
  - Jours feries francais integres pour 2026, 2027, 2028
  - Verification du solde suffisant avant soumission
  - **Limite de chevauchement : maximum 2 personnes en vacances simultanement**
  - Analyse d'impact sur l'effectif (meme logique que les absences)
  - Calendrier mensuel de l'equipe (vacances color-codees par employe, jours feries affiches)
  - Navigation calendrier bloquee pour les mois passes (uniquement mois courant et futurs)
  - Validation manager dans le dashboard (approbation = deduction automatique du solde)
  - Ajustement manuel du solde par le manager
  - Historique des demandes de vacances par employe
  - Notification Gmail dediee pour les demandes de vacances
- **Gestion des contrats** (dashboard manager) :
  - Type de contrat par employe : CDI, CDD, Periode d'essai
  - Date d'embauche (pour calcul d'anciennete)
  - Date de debut et fin de contrat
  - Calcul automatique des vacances selon la periode de reference (1er juin - 31 mai)
  - Alertes visuelles pour les fins de contrat proches (<30 jours)
  - Synchronisation automatique des soldes vacances avec les contrats

## Architecture technique

### Firebase

- **Projet** : `planning-pharmacie`
- **Base de donnees** : Firestore (europe-west1)
- **Collections** :
  - `demandes` — toutes les demandes d'absence et vacances
  - `config/vacances_solde` — soldes vacances par employe
  - `config/staff_contracts` — contrats et anciennete par employe

### Hebergement

- **GitHub Pages** sur le repo `Marcvrick/Pharmacie-Charnal`
- **Fichier** : `planning.html`
- **Deploiement** : automatique a chaque push sur `main`

## Seuils d'effectif

- **>=4 personnes** — OK (vert)
- **3 personnes** — Critique (rouge)
- **<=2 personnes** — Critique (rouge)

### Tranches horaires de controle

- **Matin** : 9h, 10h30, 12h
- **Apres-midi** : 14h, 15h15, 16h, 16h30, 17h30, 18h, 18h30
- **19h exclue** — derniere 15min de fermeture, pas significatif

### Logique de recuperation

- **Detection des creneaux** : recherche sur 30 jours, verifie matin et apres-midi separement
- **Matin (9h-12h30)** : 3h30 de recuperation
- **Apres-midi (14h-19h)** : 5h de recuperation
- **PRIORITAIRE** (rouge) : effectif <= 3 personnes (critique)
- **RECOMMANDE** (orange) : effectif = 4 personnes (au seuil optimal)
- **Condition** : l'employe ne doit pas etre programme sur le creneau propose

## Modifications effectuees (Janvier 2026)

1. **Mise a jour du planning** — Nouveau planning TEAM avec 6 employes (Laure, Stephanie, Claire, Sandrine, Titia, Leila). Retrait de Chloe.
2. **Laure retiree du dropdown** — Elle reste dans les donnees STAFF pour le calcul d'effectifs mais ne peut pas soumettre de demandes.
3. **Affichage effectif** — Badges affichent "5pers" au lieu de "5".
4. **Tranche 19h retiree** — Les dernieres 15min de fermeture ne comptent plus dans les calculs.
5. **Laure retiree du solde d'heures** — N'apparait plus dans le tableau de balance.
6. **Seuil critique a 3** — 3 personnes = critique (rouge), minimum 4 requis.
7. **Recuperation differenciee** — Heures coeur (14h-17h30) vs fin de journee (17h30+) avec seuils differents.
8. **Recuperation partielle** — L'employe peut soumettre meme si la recuperation ne couvre pas 100% des heures. Le solde du est affiche en orange.
9. **Planning des vacances** — Nouvel onglet "Vacances" pour Chloe, Claire et Sandrine. Solde de 25 jours/an, formulaire avec calcul jours ouvrables, calendrier equipe, analyse d'impact, validation manager avec deduction automatique.
10. **Chloe ajoutee au dropdown** — Presente dans le selecteur employe pour acceder a ses vacances, mais absente du planning (arret maladie).
11. **Bouton "Demande Absence"** — Renomme depuis "Nouvelle demande" pour plus de clarte.
12. **Dates alignees** — Date debut et Date fin sur la meme ligne dans le formulaire d'absence.
13. **Migration Firebase** — Remplacement de localStorage par Firebase Firestore pour synchronisation temps reel entre appareils.
14. **Ecran de login** — Mot de passe equipe requis pour acceder a l'app.
15. **Deploiement en ligne** — App deployee sur GitHub Pages a www.pharmaciecharnal.com/planning.html
16. **Responsive mobile** — Badges solde d'heures reduits sur mobile pour meilleur affichage.
17. **Recuperation d'heures** — Nouveau type de demande dans le formulaire d'absence (visible uniquement si l'employe a des heures dues). Permet de selectionner des creneaux de recuperation sur 30 jours. Detection amelioree : verifie matin/apres-midi separement, propose les creneaux ou l'effectif est <= 4 (PRIORITAIRE si <=3, RECOMMANDE si =4). Validation manager avec credit automatique des heures.
18. **Gestion des contrats** — Nouvelle section dans le dashboard manager permettant de definir le type de contrat (CDI/CDD/Periode d'essai), les dates de debut/fin, et la date d'embauche originale pour le calcul d'anciennete.
19. **Calcul automatique des vacances** — Les jours de vacances sont maintenant calcules automatiquement selon la loi francaise : 2.5 jours ouvrables par mois travaille (periode de reference 1er juin - 31 mai), avec bonus de +2 jours apres 6 ans d'anciennete (convention pharmacie).
20. **Acces vacances etendu** — Tous les employes (Stephanie, Claire, Sandrine, Titia, Melanie, Chloe, Mathilde, Emilie, Pascal) ont maintenant acces au module vacances.
21. **Alertes fin de contrat** — Affichage d'alertes visuelles dans le dashboard manager lorsqu'un contrat CDD ou periode d'essai arrive a echeance (orange si <30 jours, rouge si <7 jours ou termine).
22. **Exclusion des creneaux deja utilises** — Les creneaux de recuperation deja approuves ou en attente ne sont plus proposes a nouveau. Evite les doublons de recuperation.
23. **Limite de chevauchement vacances** — Maximum 2 personnes peuvent etre en vacances en meme temps. Si une demande de vacances chevauche avec 2+ autres personnes, elle est bloquee avec un message d'erreur explicite.

## Modifications effectuees (Fevrier 2026)

24. **Remplacement Leila par Melanie Le Bihan** — Melanie (35h) remplace Leila dans le STAFF et le planning.
25. **Ajout Mathilde au STAFF** — Mathilde (28h, Lun/Mar/Jeu/Ven) ajoutee dans les donnees STAFF avec ses horaires. Comptee dans les calculs de couverture.
26. **Melanie ajoutee aux vacances** — Acces au module vacances pour Melanie.
27. **Ajout Emilie et Pascal** — Emilie (arret maladie) et Pascal (freelance) ajoutes au dropdown et vacances.
28. **Roles employes definis** — Definition des roles (pharmacien vs preparatrice) pour chaque employe :
    - Pharmaciens : Laure, Stephanie, Claire, Pascal
    - Preparatrices : Sandrine, Titia, Melanie, Mathilde, Chloe, Emilie
29. **Laure exclue des echanges normaux** — Laure n'est pas disponible pour les demandes d'echange (role de manager/bouche-trou).
30. **Validation disponibilite pour echanges** — L'autre employe DOIT etre disponible (pas deja programmé a cette periode), sinon pas d'interet
31. **Validation pharmacien pour echanges** — Verification automatique qu'il y aura toujours au minimum 1 pharmacien en boutique lors d'un echange :
    - Blocage automatique si l'echange mettrait la boutique sans pharmacien
    - Alerte si Laure sera la SEULE pharmacienne en boutique
    - Fonctionne pour echanges pharmacien ↔ pharmacien ET pharmacien ↔ preparatrice

## Modifications effectuees (Fevrier 2026 - Phase 2)

32. **Fix: Demandes en attente** — Correction du filtre "Demandes en attente" pour inclure les echanges (statuts 'attente' ET 'echange_attente'). Affichage correct des demandes d'echange en attente validation.

33. **Reorganisation dashboard manager** — Restructuration des sections :
    - "Gestion des plannings" deplacee plus haut (avant contrats)
    - "Historique complet" repositionne entre contrats et export/backup
    - Section export/backup a la fin

34. **Consolidation onglets "Solde des vacances"** — Trois onglets (tabs) pour une meilleure organisation :
    - **Onglet 1 : Solde vacances** — Affichage classique avec jours annuels, pris, restants
    - **Onglet 2 : Heures dues** — Nouvelles heures (non-vacances) avec affichage:
      * Grand nombre des heures dues (vert/orange/rouge selon criticite)
      * Creneaux de recuperation avec dates/horaires
      * Details expandibles (toggle)
    - **Onglet 3 : Heures mensuelles par employe** — Vue manager montrant heures dues par employe

35. **System "Solde d'heures"** (heures dues vs recuperation) — Amelioration interface :
    - Affichage par employe avec card layout
    - Couleur-coding dynamique : vert (>5h), orange (3-5h), rouge (<=2h)
    - Chaque employe : heures dues + creneaux de recuperation avec dates/horaires
    - Toggle "Details" pour affichage expanded
    - Suivi des heures recuperees vs dues restantes

36. **Ameliorations visuelles UI** :
    - Bordures des cartes vacances plus foncees (#6B7280 au lieu de #E5E7EB)
    - Bouton "Modifier" (contrats) change en `btn-outline` (transparent, bordure 2px)
    - Backgrounds des champs input 30% plus foncés (#F3F4F6)
    - Design global plus coherent avec meilleure hierarchie visuelle

37. **Editeur de planning compact** — Redesign du formulaire d'edition :
    - Largeur limitee a 550px (centré) au lieu de pleine largeur
    - AM/PM bien serres vertically
    - Champs texte horaires fixes (100px) et compacts
    - Layout grid responsif : `100px auto auto` pour jours
    - Labels AM/PM reduits en taille

38. **Interface vacances simplifiee** — Redesign du solde vacances :
    - Grand nombre (jours restants) en vedette avec couleur (vert/orange/rouge)
    - Barre de progression avec code couleur
    - Infos detaillees au clic (toggle "Détails")
    - Formulaire modification au clic (toggle "Modifier")
    - Progressive disclosure : info critique toujours visible, details a la demande

39. **Mode "Creer un planning vide (avancé)"** — Nouvel interface pour creation de planning :
    - Choix de template ou mode vide
    - Selection du template depuis cards visuelles
    - Edition avec horaires par defaut
    - Checkboxes AM/PM + heures modifiables
    - Calcul automatique total heures/semaine
    - Validation nom + role
    - Creation stockée dans Firebase

40. **Auto-backup system** — Sauvegarde automatique chaque samedi a 14h :
    - Telechargement automatique JSON vers Downloads folder
    - Tracker Firebase pour prevenir doublons meme jour
    - Affichage timestamp du dernier backup dans Export/Backup
    - Check toutes les 5 minutes (fonction setInterval)
    - Contient : demandes, vacances solde, contrats, staff schedules, timestamp
    - Fichier : `planning-backup-YYYY-MM-DD.json`

41. **Enlever tableau Solde d'heures de la page Planning** — Le tableau "Solde d'heures" n'apparait plus sur la page Planning (qui affichait les heures dues par employe avec courbes). Les heures dues restent accessibles dans "Mes demandes" pour les employes qui en ont besoin.

## Fichiers

### Fichiers principaux
- `app.html` — Version locale de developpement
- `planning.html` — Version deployee (dans le repo website-pharmacie-charnal)

### Documentation UI/UX
- `SCHEDULE_EDITOR_COMPACT.md` — Guide du redesign editeur planning (compact, 550px max)
- `VACANCES_UI_SIMPLIFIED.md` — Guide du redesign interface vacances (progressive disclosure)
- `BLANK_SCHEDULE_GUIDE.md` — Guide mode "Creer un planning vide" (template selection)

## Lancer l'app en local

```bash
cd "/Users/mc/Documents/MarcOS/Pharma/APP planning"
python3 -m http.server 8080
# Ouvrir http://localhost:8080/app.html
```

## Source du planning

Le planning de reference est dans : `Planning creation/Planning TEAM.md`

---

## Console Firebase

https://console.firebase.google.com/project/planning-pharmacie

---

---

## Code Standards: DRY + SOLID

**Every implementation must pass DRY/SOLID audit:**
- No code duplication (extract to functions/modules)
- No large centralized const files (keep constants near usage)
- Single Responsibility: each function/component has one job
- Open/Closed: open for extension, closed for modification
- Liskov Substitution: predictable behavior contracts
- Interface Segregation: focused, minimal interfaces
- Dependency Inversion: depend on abstractions, not concrete implementations

**Before submitting code:** Run mental audit—if logic appears twice, extract it. If a file >200 lines, break it down.

---

## TODO

### Fait

- [x] Migrer vers Firebase pour partage des donnees entre appareils
- [x] Deployer sur GitHub Pages
- [x] Planning des vacances
- [x] Recuperation d'heures (integree au formulaire d'absence)
- [x] Gestion des contrats (CDI/CDD/Periode d'essai)
- [x] Calcul automatique des vacances selon la loi francaise
- [x] Acces vacances pour tous les employes
- [x] Alertes fin de contrat

### A faire (optionnel)

- [ ] Securiser les regles Firestore (actuellement ouvertes)
- [ ] Ajouter authentification Firebase Auth si besoin de securite renforcee
- [ ] Masquer automatiquement les employes du planning apres fin de contrat
