#!/usr/bin/env python3
"""Injecte dans la page la garde de journée du JOUR MÊME, et rien d'autre.

Usage :  python3 update-garde-du-jour.py            aujourd'hui
         python3 update-garde-du-jour.py 2026-09-06 une date donnée (test)
         python3 update-garde-du-jour.py --check    n'écrit rien, sort en 1 si dérive

SOURCE des données : le vault iCloud, hors du repo.
  Pharma/GESTION/Plannings de garde/planning-gardes-2026.json
Le repo git local `/Users/mc` n'a aucun remote : le planning ne part jamais en ligne.

RÈGLE (voir CLAUDE.md) : la page ne contient qu'UNE date, celle du jour, et
uniquement la garde de JOURNÉE (dimanches et jours fériés). Jamais de garde de
nuit, jamais de date future ou passée. Le script vérifie les deux après écriture.

Un filet côté client masque le bloc si la date affichée n'est pas celle du
visiteur, ou hors du créneau 9h-19h : si la mise à jour quotidienne saute, la
page n'affiche rien plutôt qu'une information périmée.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "pharmacie-de-garde-queven-hennebont-lorient.html"
SOURCE = (Path("/Users/mc/Library/Mobile Documents/com~apple~CloudDocs/MarcOS")
          / "Pharma" / "GESTION" / "Plannings de garde" / "planning-gardes-2026.json")

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

SECTEURS = [
    ("561021", "Quéven, Hennebont, Guidel&hellip;"),
    ("561020", "Lorient, Lanester, Ploemeur, Larmor-Plage"),
]

DEBUT = "<!-- GARDE-DU-JOUR:DEBUT -->"
FIN = "<!-- GARDE-DU-JOUR:FIN -->"

CHECK = "--check" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
jour = date.fromisoformat(args[0]) if args else date.today()
iso = jour.isoformat()

if not SOURCE.exists():
    sys.exit(f"ECHEC : source introuvable\n  {SOURCE}\n"
             "  (le planning vit dans le vault, jamais dans ce repo)")
planning = json.loads(SOURCE.read_text(encoding="utf-8"))

num = "1er" if jour.day == 1 else str(jour.day)
libelle = f"{JOURS[jour.weekday()]} {num} {MOIS[jour.month - 1]} {jour.year}"

cartes = []
for code, communes in SECTEURS:
    e = planning.get(code, {}).get(iso)
    if not e or not e.get("jour"):
        continue  # jour ouvrable : aucune garde de journée désignée
    ferie = e.get("ferie", "")
    label = f"Garde {ferie}, 9h&ndash;19h" if ferie else "Garde de journée, 9h&ndash;19h"
    for nom in e["jour"]:
        # deux formes possibles : "NOM - PHCIE X - VILLE" ou "NOM (Ville)"
        # (pas de nom reel en exemple : ce fichier est dans un repo public)
        m = re.match(r"^(.*?)\s*\(([^)]+)\)$", nom)
        if m:
            pharmacie, ville = m.group(1), m.group(2)
        else:
            morceaux = nom.rsplit(" - ", 1)
            pharmacie = morceaux[0]
            ville = morceaux[1].title() if len(morceaux) > 1 else ""
        cartes.append(
            f'                    <div class="today-guard-card" data-garde-date="{iso}">\n'
            f'                        <div class="today-guard-date">{libelle}</div>\n'
            f'                        <div class="today-guard-pharmacie">Pharmacie {pharmacie}</div>\n'
            f'                        <div class="today-guard-ville">{ville}</div>\n'
            f'                        <div class="today-guard-type">{label}</div>\n'
            f'                        <div class="today-guard-secteur">Secteur de garde '
            f'N&deg;{code} ({communes})</div>\n'
            f'                    </div>')

if cartes:
    corps = "\n\n".join(cartes)
else:
    corps = (f'                    <!-- {libelle} : aucune garde de journée désignée, '
             f'les pharmacies du secteur sont ouvertes normalement -->')

bloc = f"                    {DEBUT}\n{corps}\n                    {FIN}"

src = PAGE.read_text(encoding="utf-8")
orig = src

i, j = src.find(DEBUT), src.find(FIN)
if i != -1 and j != -1:
    deb = src.rfind("\n", 0, i) + 1
    src = src[:deb] + bloc + src[j + len(FIN):]
else:
    # première pose : remplace les deux anciennes cartes pilotées par JS
    anciennes = re.compile(
        r'[ \t]*<div id="todayGuardSection".*?</div>\s*'
        r'<div id="todayGuardSection561020".*?\n[ \t]*</div>\n', re.S)
    src, n = anciennes.subn(bloc + "\n", src, count=1)
    if not n:
        sys.exit("ECHEC : point d'insertion des cartes introuvable")

# --- le JS de rendu est remplacé par un simple filet anti-péremption ---
FILET = """        // La garde du jour est écrite en dur dans le HTML par
        // update-garde-du-jour.py, une seule date. Ce filet la masque si la mise à
        // jour quotidienne a sauté, ou hors du créneau 9h-19h : mieux vaut ne rien
        // afficher qu'une information périmée. La nuit passe par le 3237.
        (function () {
            var n = new Date();
            var today = n.getFullYear() + '-'
                + String(n.getMonth() + 1).padStart(2, '0') + '-'
                + String(n.getDate()).padStart(2, '0');
            var ouvert = n.getHours() >= 9 && n.getHours() < 19;
            document.querySelectorAll('[data-garde-date]').forEach(function (el) {
                if (el.dataset.gardeDate !== today || !ouvert) {
                    el.style.display = 'none';
                }
            });
        })();"""

# L'ancien moteur pilotait les cartes par JS et référence des `id` qui n'existent
# plus. Laissé en place, il lève une TypeError qui interrompt le script AVANT le
# filet, et une garde périmée reste affichée. Le retirer n'est donc pas cosmétique.
# On ancre sur `const gardesData`, stable, et non sur un commentaire qui a déjà
# changé une fois.
if FILET not in src:
    ancien_js = re.compile(
        r"[ \t]*(?://[^\n]*\n[ \t]*)*const gardesData = .*?"
        r"document\.addEventListener\('DOMContentLoaded', \(\) => \{\s*"
        r"renderTodayGuard\(\);\s*\}\);", re.S)
    src, n = ancien_js.subn(FILET, src, count=1)
    if not n:
        sys.exit("ECHEC : ancien moteur JS des gardes introuvable, "
                 "impossible d'installer le filet anti-péremption")
    print("  + ancien moteur JS remplacé par le filet anti-péremption")

if src != orig:
    if CHECK:
        print("--check : la page n'est pas à jour")
        sys.exit(1)
    PAGE.write_text(src, encoding="utf-8")
    print(f"  + {iso} ({libelle}) : {len(cartes)} carte(s) écrite(s)")
else:
    print(f"  = {iso} : déjà à jour ({len(cartes)} carte(s))")

# ------------------------------------------------- vérification par les VALEURS
final = PAGE.read_text(encoding="utf-8")
fuites = []
dates = set(re.findall(r'data-garde-date="(\d{4}-\d{2}-\d{2})"', final))
if dates - {iso}:
    fuites.append(f"date(s) autre(s) que {iso} : {sorted(dates - {iso})}")
for motif, libel in [(r'type: "Nuit"', "ligne de garde de nuit"),
                     (r'type: "Jour"', "ligne de garde de jour"),
                     (r'type: "Férié"', "ligne de garde de jour férié"),
                     (r"<tr data-date=", "ligne de tableau de planning"),
                     (r'"\d{4}-\d{2}": \[', "mois de planning embarqué")]:
    n = len(re.findall(motif, final))
    if n:
        fuites.append(f"{n} x {libel}")
# Ne contrôler que les dates de GARDE, pas les dates éditoriales de la page
# (« Depuis le 1er janvier 2025, ces honoraires... » n'est pas une garde).
zone = final[final.find(DEBUT):final.find(FIN)] if DEBUT in final else ""
affichees = set(re.findall(r'class="today-guard-date">([^<]+)<', zone))
autres = affichees - ({libelle} if cartes else set())
if autres:
    fuites.append(f"date(s) de garde autre(s) qu'aujourd'hui : {sorted(autres)}")
hors_zone = re.findall(r'class="today-guard-date">([^<]+)<',
                       final.replace(zone, "") if zone else final)
if hors_zone:
    fuites.append(f"carte de garde hors du bloc balisé : {hors_zone}")

for reste in ("renderTodayGuard", "todayGuardSection", "renderTodayGuardZone",
              "gardesData"):
    if reste in final:
        fuites.append(f"reste de l'ancien moteur JS : {reste}")
if FILET not in final:
    fuites.append("filet anti-péremption absent")

if fuites:
    for f in fuites:
        print(f"  FUITE : {f}")
    sys.exit(1)
print(f"  verification : une seule date dans la page ({iso}), aucune garde de nuit  OK")
