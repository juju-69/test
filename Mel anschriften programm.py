import streamlit as st

# =========================================================
# HIER KANNST DU DEINE STÄDTE UND TEXTE ANPASSEN
# =========================================================

laender_daten = {
    "1": {
        "name": "Deutschland",
        "staedte": {
            "Jübek": "Tabitha Marr, Parkweg 5, 24855 Jübek",
            "Norden": "Kim Kampe-Diekmann, Dornkaatstr. 13 - 15, 26506 Norden",
            "Verden": "Alexandra Schelcher, Am Hufeisen 15, 27283 Verden",
            "Stade": "Michaela Woller, Moorchausee 128, 21683 Stade",
            "Bielefeld": "Bahar Durgunsu, Kamener Str. 11, 33647 Bielefeld", 
            "Köln": "Sara Pavo, Merowinger Str. 35, 50677 Köln", 
            "Bad Münstereifel": " Christiane Maserke, Sittardweg 24, 53902 Bad Münstereifel", 
            "Heuchelheim": "Nicoletta Gora, Schillerstr. 5a, 35452 Heuchelheim", 
            "Leipzig": "Wencke Haubold, Markt 11, 04109 Leipzig ", 
            "Frankfurt": "Samira Jawadi, Schillerstr. 31, 60313 Frankfurt am Main",
            "Frankfurt 2": "Jenny Hertel, 60596 Frankfurt am Main",
            "Würzburg": "",
            "Oststeinbek": "Miriam Felice, 22113 Oststeinbek",
            "Amberg": "", 
            "Mannheim": "", 
            "Geislingen": "", 
            "Mühldorf": "Yvonne Werner, 84453 Mühldorf am Inn", 
            "München": "", 
            "Friedrichshafen": "Joana Pfeiderer, 88045 Friedrichshafen",
            "Bad Homburg": "Julia Dittrich, Haingasse 5, 61348 Bad Homburg",
            "Wusterwitz": "Antje Benecke Hautaesthetik, 14789 Wusterwitz",
            "Berlin": "Kosmetik Heike Dossmann, 12159 Berlin",
            "Lutherstadt Wittenberg": "Sophia Kreutzer, 06886 Lutherstadt Wittenberg",
            "Bonn": "Julia Petker, 53121 Bonn",
            "Esslingen": "Julia Schwicker, 73732 Esslingen",
            "Groß Köris": "Julia Starke, 15746 Groß Köris",
            "Geislingen": "Alexandra Lauer, 73312 Geislingen",
            "Dammbach": "Sarah Seibert, 63874 Dammbach",
        }
    },
    "2": {
        "name": "Österreich",
        "staedte": {
            "Wien": "Zuzanna Lach, Mariahilferstr. 126/21, 1070Wien AT", 
            "Neuzeug": "Denise Bramberger, Burgstallstr. 11, 4523 Neuzeug AT", 
            "Kötschach - Mauthen": "Petra Oberauner, Mauthen 215, 9640 Kötschach - Mauthen AT",
            "Bad Ischl": "Christine Mörschbacher, 4820 Bad Ischl AT",
            "Saalfelden": "Karin Schnelzer, 5760 Saalfelden AT",
        }
    },
    "3": {
        "name": "Niederlande",
        "staedte": {
            "Didam": "Madelon Bänziger, 6942 Didam (Klammer offen weil auf rechnung steht Deutschland)",
        }
    },
    "4": {
        "name": "Liechtenstein",
        "staedte": {
            "Schaan": "Rachel Tino-Jehle, 9494 Schaan LI",
        }
    }
}

# =========================================================
# AB HIER STARTET DAS EIGENTLICHE PROGRAMM (NIX MEHR ÄNDERN)
# =========================================================

# Titel der App auf der Webseite
st.title("Welche Daten möchtest du Wissen?")

# 1. Länder-Auswahl als Dropdown
land_namen = [daten["name"] for daten in laender_daten.values()]
gewaehltes_land = st.selectbox("Bitte wähle ein Land aus:", land_namen)

# 2. Den passenden Schlüssel (1, 2, 3 oder 4) für das gewählte Land finden
land_schluessel = None
for schluessel, daten in laender_daten.items():
    if daten["name"] == gewaehltes_land:
        land_schluessel = schluessel
        break

# 3. Städte-Auswahl basierend auf dem gewählten Land anzeigen
if land_schluessel:
    # Holt alle Städtenamen als Liste für das Dropdown
    staedte_dict = laender_daten[land_schluessel]["staedte"]
    gewaehlte_stadt = st.selectbox("Bitte wähle eine Stadt deiner Wahl aus:", list(staedte_dict.keys()))
    
    # Bestätigungs-Button auf der Webseite
    if st.button("Auswahl bestätigen"):
        # Das Ergebnis schön anzeigen
        st.success("Auswahl erfolgreich!")
        st.write(f"**Gewähltes Land:** {gewaehltes_land}")
        st.write(f"**Gewählte Stadt:** {gewaehlte_stadt}")
        
        # Holt den spezifischen Text der ausgewählten Stadt
        stadt_spezifischer_text = staedte_dict[gewaehlte_stadt]
        
        # Zeigt den individuellen Text in der Infobox an
        st.info(stadt_spezifischer_text)
