#!/usr/bin/env python3
"""Garde-fou de confidentialite des gardes, page pharmacie de garde.

Usage :  python3 check-garde-privacy.py          applique et verifie
         python3 check-garde-privacy.py --check  n'ecrit rien, sort en 1 si fuite

REGLE (Dany, 05/09/2026)
------------------------
Le site ne publie JAMAIS de calendrier de gardes, meme limite aux gardes de
journee. Le dimanche, la pharmacie de garde de journee est aussi celle de la
nuit suivante : un calendrier permet donc de savoir des aujourd'hui quel
pharmacien sera seul dans son officine tel soir, et de le planifier.

Publiable  : qui est de garde AUJOURD'HUI, en journee (samedi, dimanche, ferie).
Interdit   : toute date future ou passee, tout planning, toute garde de nuit,
             y compris en donnees brutes non affichees a l'ecran.
La nuit passe par le 3237, qui enregistre l'identite de l'appelant.

Ce script retire du fichier public tout ce qui constitue un calendrier, puis
verifie par les VALEURS qu'il n'en reste rien.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "pharmacie-de-garde-queven-hennebont-lorient.html"
CHECK = "--check" in sys.argv

src = PAGE.read_text(encoding="utf-8")
orig = src
actions = []

# ------------------------------------------------- 1. tableau statique + CSS + JS
BLOCS = [
    ("tableau statique",
     r"[ \t]*<!-- PLANNING-STATIQUE:DEBUT -->.*?<!-- PLANNING-STATIQUE:FIN -->\n"),
    ("CSS du planning",
     r"[ \t]*<!-- PLANNING-STATIQUE:CSS -->\s*<style>.*?</style>\n"),
    ("JS du planning",
     r"[ \t]*<!-- PLANNING-STATIQUE:JS -->\s*<script>.*?</script>\n"),
]
for nom, motif in BLOCS:
    src, n = re.subn(motif, "", src, flags=re.S)
    actions.append(f"{'+' if n else '='} {nom} : {'retire' if n else 'deja absent'}")

# ------------------------------------- 2. donnees de planning embarquees dans le JS
VIDE = """        // Aucun planning n'est embarque dans la page. Publier un calendrier,
        // meme reduit aux gardes de journee, revient a annoncer a l'avance quel
        // pharmacien sera seul dans son officine tel soir : le dimanche, la garde
        // de journee et la garde de nuit sont assurees par la meme pharmacie.
        // Seule la garde du JOUR MEME peut etre affichee, et elle doit alors etre
        // injectee au moment de la construction de la page, jamais stockee ici.
        // Voir CLAUDE.md, section "Regle de securite".
        const gardesData = {};
        const gardesData561020 = {};"""

bloc_donnees = re.compile(
    r"[ \t]*// === DONNÉES DES GARDES.*?"
    r"const gardesData561020 = \{.*?\n        \};", re.S)
# Depuis la mise en place de `update-garde-du-jour.py`, la page n'embarque plus
# aucun objet de planning : la garde du jour est ecrite en dur, une seule date.
# L'absence totale du bloc est donc l'etat NORMAL, pas une erreur.
if "const gardesData" not in src:
    actions.append("= donnees de planning : aucun objet embarque (etat attendu)")
elif VIDE in src:
    actions.append("= donnees de planning : deja vidées")
else:
    src, n = bloc_donnees.subn(VIDE, src, count=1)
    if not n:
        sys.exit("ECHEC : bloc `const gardesData` present mais non reconnu, "
                 "verifier manuellement ce qu'il contient")
    actions.append("+ donnees de planning : vidées")

# ------------------------------------------------------- 3. meta : ne rien promettre
ANCIENNES = [
    '<meta name="description" content="Quelle pharmacie de garde ce dimanche à Lorient, Quéven, '
    'Hennebont? Nom et commune de la garde de jour, planning 2026 des dimanches et jours fériés.">',
    '<meta name="description" content="Quelle pharmacie de garde ce soir et ce dimanche à '
    'Lorient, Quéven, Hennebont? Nom et commune de la pharmacie de garde du jour, planning 2026 '
    'complet.">',
]
NOUVELLE = ('<meta name="description" content="Trouver la pharmacie de garde aujourd\'hui à '
            'Lorient, Quéven et Hennebont: garde de journée le week-end, 3237 pour la nuit, '
            '15 ou 112 en urgence vitale.">')
if NOUVELLE in src:
    actions.append("= meta description : deja a jour")
else:
    for a in ANCIENNES:
        if a in src:
            src = src.replace(a, NOUVELLE, 1)
            actions.append("+ meta description : reecrite")
            break
    else:
        actions.append("! meta description : etat inattendu, non touchee")

OG = ('<meta property="og:description" content="Nom et commune de la pharmacie de garde du jour, '
      'plus le planning complet des dimanches et jours fériés, secteurs 561021 et 561020.">')
OG_NEW = ('<meta property="og:description" content="La pharmacie de garde de journée du week-end '
          'à Lorient, Quéven et Hennebont. Pour la nuit, le 3237.">')
if OG_NEW in src:
    actions.append("= og:description : deja a jour")
elif OG in src:
    src = src.replace(OG, OG_NEW, 1)
    actions.append("+ og:description : reecrite")

for a in actions:
    print("  " + a)

if src != orig:
    if CHECK:
        print("\n--check : la page contient encore un calendrier")
        sys.exit(1)
    PAGE.write_text(src, encoding="utf-8")
    print(f"\necrit : {PAGE.name}")
else:
    print("\naucun changement")

# ------------------------------------------------- 4. verification par les VALEURS
final = PAGE.read_text(encoding="utf-8")
fuites = []
for motif, libelle in [
    (r'type: "Nuit"', "ligne de garde de nuit"),
    (r'type: "Jour"', "ligne de garde de jour"),
    (r'type: "Férié"', "ligne de garde de jour férié"),
    (r"type === 'Nuit'", "reference JS a la garde de nuit"),
    (r"<tr data-date=", "ligne de tableau de planning"),
    (r'"\d{4}-\d{2}": \[', "mois de planning embarque"),
    (r"renderTodayGuard", "reste de l'ancien moteur JS"),
]:
    n = len(re.findall(motif, final))
    if n:
        fuites.append(f"{n} x {libelle}")

# Au plus UNE date de garde dans la page. Deux dates = un calendrier.
# On ne regarde que les dates de GARDE : la page contient des dates editoriales
# legitimes (« Depuis le 1er janvier 2025, ces honoraires... ») qu'il ne faut pas
# confondre avec un planning. Que la date presente soit bien celle du jour est
# verifie par `update-garde-du-jour.py`, pas ici.
dates_garde = set(re.findall(r'data-garde-date="(\d{4}-\d{2}-\d{2})"', final))
libelles = set(re.findall(r'class="today-guard-date">([^<]+)<', final))
if len(dates_garde) > 1:
    fuites.append(f"{len(dates_garde)} dates de garde dans la page (calendrier) : "
                  f"{sorted(dates_garde)}")
if len(libelles) > 1:
    fuites.append(f"{len(libelles)} dates affichees dans les cartes : {sorted(libelles)}")

print("\n--- verification ---")
if fuites:
    for f in fuites:
        print(f"  FUITE : {f}")
    sys.exit(1)
print("  aucun calendrier, aucune garde de nuit, aucune date future dans la page  OK")
