#!/usr/bin/env python3
"""Calcule la garde de journée du JOUR MÊME et l'écrit dans un fichier JSON,
destiné à la branche `garde-data` — jamais dans la page HTML de `main`.

Usage :  python3 update-garde-du-jour.py                   aujourd'hui, écrit garde.json
         python3 update-garde-du-jour.py 2026-09-06         une date donnée (test)
         python3 update-garde-du-jour.py --check             n'écrit rien, sort en 1 si le
                                                               JSON existant n'est pas à jour
         python3 update-garde-du-jour.py --out PATH           chemin de sortie (défaut: ./garde.json)

SOURCE des données : le vault iCloud, hors du repo.
  Pharma/GESTION/Plannings de garde/planning-gardes-2026.json
Le repo git local `/Users/mc` n'a aucun remote : le planning ne part jamais en ligne.

RÈGLE (voir CLAUDE.md) : le JSON produit ne contient qu'UNE date, celle du jour, et
uniquement la garde de JOURNÉE (dimanches et jours fériés). Jamais de garde de
nuit, jamais de date future ou passée. Ce script vérifie les valeurs après calcul.

Ce JSON n'est JAMAIS commité sur `main` — il vit sur la branche `garde-data`
(non protégée, non déployée), amendée chaque jour par le workflow. La page
HTML sur `main` ne l'embarque pas : elle le récupère par `fetch()` au chargement
et applique elle-même un filet anti-péremption (date + créneau 9h-19h) avant de
l'afficher. Voir pharmacie-de-garde-queven-hennebont-lorient.html.
"""
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = (Path("/Users/mc/Library/Mobile Documents/com~apple~CloudDocs/MarcOS")
          / "Pharma" / "GESTION" / "Plannings de garde" / "planning-gardes-2026.json")

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

SECTEURS = [
    ("561021", "Quéven, Hennebont, Guidel…"),
    ("561020", "Lorient, Lanester, Ploemeur, Larmor-Plage"),
]

CHECK = "--check" in sys.argv
args = list(sys.argv[1:])
OUT = ROOT / "garde.json"
if "--out" in args:
    i = args.index("--out")
    OUT = Path(args[i + 1])
    del args[i:i + 2]
args = [a for a in args if not a.startswith("--")]
jour = date.fromisoformat(args[0]) if args else date.today()
iso = jour.isoformat()

# Deux sources possibles, jamais le repo :
#  - en local : le fichier du vault (jour ET nuit, usage interne)
#  - en CI    : le secret GitHub PLANNING_GARDES_JOUR, qui ne contient QUE les
#               gardes de journee. Les gardes de nuit ne quittent pas le disque.
brut = os.environ.get("PLANNING_GARDES_JOUR")
if brut:
    planning = json.loads(brut)
    origine = "secret PLANNING_GARDES_JOUR"
elif SOURCE.exists():
    planning = json.loads(SOURCE.read_text(encoding="utf-8"))
    origine = str(SOURCE)
else:
    sys.exit("ECHEC : aucune source de planning\n"
             f"  ni la variable PLANNING_GARDES_JOUR, ni {SOURCE}\n"
             "  (le planning ne vit jamais dans ce repo)")

num = "1er" if jour.day == 1 else str(jour.day)
libelle = f"{JOURS[jour.weekday()]} {num} {MOIS[jour.month - 1]} {jour.year}"

# Quels jours peuvent etre publies, et d'ou vient le nom.
#
# Dimanche et jour ferie : le planning designe une garde de JOURNEE (`jour`).
#   Verifie sur les 63 dates concernees des deux secteurs : la pharmacie de la
#   nuit est LA MEME, sans exception. La publier ne revele donc rien de plus.
# Samedi : le planning n'a pas de categorie samedi, il ne porte qu'une entree
#   `nuit`. C'est pourtant bien la garde du samedi, qui couvre la journee ET la
#   soiree (Dany, 05/09/2026). On la publie donc le samedi.
# Lundi a vendredi : l'entree `nuit` est une garde de nuit pure. JAMAIS publiee.
SAMEDI = 5

cartes = []
for code, communes in SECTEURS:
    e = planning.get(code, {}).get(iso)
    if not e:
        continue
    ferie = e.get("ferie", "")
    if e.get("jour"):
        noms = e["jour"]
        label = f"Garde du {ferie}" if ferie else "Garde du dimanche"
        if jour.weekday() == SAMEDI:
            label = "Garde du samedi"
    elif jour.weekday() == SAMEDI and e.get("nuit"):
        noms = e["nuit"]
        label = "Garde du samedi"
    else:
        continue  # jour ouvrable : rien a publier, le 3237 prend le relais
    for nom in noms:
        # deux formes possibles : "NOM - PHCIE X - VILLE" ou "NOM (Ville)"
        # (pas de nom reel en exemple : ce fichier est dans un repo public)
        m = re.match(r"^(.*?)\s*\(([^)]+)\)$", nom)
        if m:
            pharmacie, ville = m.group(1), m.group(2)
        else:
            morceaux = nom.rsplit(" - ", 1)
            pharmacie = morceaux[0]
            ville = morceaux[1].title() if len(morceaux) > 1 else ""
        cartes.append({
            "pharmacie": pharmacie,
            "ville": ville,
            "label": label,
            "secteur_code": code,
            "secteur_communes": communes,
        })

# ------------------------------------------------- verification par les VALEURS
# Garde-fou dur : un lundi-vendredi non ferie ne porte qu'une garde de NUIT.
# Publier un nom ce jour-la serait exactement la fuite que tout ce dispositif
# existe pour empecher.
fuites = []
ferie_du_jour = any(planning.get(c, {}).get(iso, {}).get("ferie")
                    for c, _ in SECTEURS)
jour_publiable = jour.weekday() in (5, 6) or ferie_du_jour
if cartes and not jour_publiable:
    fuites.append(f"{len(cartes)} carte(s) calculee(s) un "
                  f"{JOURS[jour.weekday()].lower()} non férié : ce serait une garde de nuit")
if fuites:
    for f in fuites:
        print(f"  FUITE : {f}")
    sys.exit(1)

payload = {"date": iso, "libelle": libelle, "cartes": cartes}

if CHECK:
    if not OUT.exists():
        print(f"--check : {OUT} absent")
        sys.exit(1)
    actuel = json.loads(OUT.read_text(encoding="utf-8"))
    if actuel.get("date") != iso:
        print(f"--check : {OUT} date {actuel.get('date')!r}, attendu {iso!r}")
        sys.exit(1)
    if actuel != payload:
        print(f"--check : {OUT} present mais contenu different de la valeur recalculee")
        sys.exit(1)
    print(f"  verification : {OUT.name} a jour ({iso}), {len(cartes)} carte(s), "
          f"une seule date, aucune garde de nuit  OK")
    sys.exit(0)

OUT.parent.mkdir(parents=True, exist_ok=True)
if OUT.exists() and json.loads(OUT.read_text(encoding="utf-8")) == payload:
    print(f"  = {iso} : déjà à jour ({len(cartes)} carte(s))")
else:
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  + {iso} ({libelle}) : {len(cartes)} carte(s) écrite(s) dans {OUT}")
print(f"  source : {origine}")
