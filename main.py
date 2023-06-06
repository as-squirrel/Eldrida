import sqlite3
import pygame 
from pygame import mixer

from colorama import init, Fore, Style

init(autoreset=False)

pygame.init()

#Die Musik des Spieles
music = pygame.mixer.music.load('bad.wav')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(.2)



# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('datenbank.db')

# Cursor-Objekt erstellen
c = conn.cursor()

# Tabelle für Benutzer erstellen
c.execute('''CREATE TABLE IF NOT EXISTS benutzer
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT NOT NULL UNIQUE, 
              passwort TEXT NOT NULL)''')

# Tabelle für Inventar erstellen
c.execute('''CREATE TABLE IF NOT EXISTS inventar
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              benutzer_id INTEGER NOT NULL, 
              name TEXT NOT NULL, 
              menge INTEGER NOT NULL)''')

# Benutzer registrieren
def registrieren(name, passwort):
    try:
        c.execute('''INSERT INTO benutzer (name, passwort)
                     VALUES (?, ?)''', (name, passwort))
        conn.commit()
        print("Registrierung erfolgreich!")
    except sqlite3.IntegrityError:
        print("Benutzer existiert bereits!")

# Benutzer anmelden
def anmelden(name, passwort):
    c.execute('''SELECT * FROM benutzer WHERE name = ? AND passwort = ?''', (name, passwort))
    benutzer = c.fetchone()
    if benutzer:
        print("Anmeldung erfolgreich!")
        return benutzer
    else:
        print("Falscher Benutzername oder Passwort!")

# Inventar hinzufügen
def inventar_hinzufügen(benutzer_id, name, menge):
    try:
        c.execute('''INSERT INTO inventar (benutzer_id, name, menge)
                     VALUES (?, ?, ?)''', (benutzer_id, name, menge))
        conn.commit()
        print("Inventar hinzugefügt!")
    except sqlite3.Error as e:
        print("Fehler beim Hinzufügen des Inventars:", e)

# Inventar suchen
def inventar_suchen(benutzer_id, name):
    c.execute('''SELECT * FROM inventar WHERE benutzer_id = ? AND name = ?''', (benutzer_id, name))
    inventar = c.fetchone()
    if inventar:
        print("Inventar gefunden:", inventar)
    else:
        print("Inventar nicht gefunden!")

# Spiel-Loop
def errate_hauptstadt(land, hauptstadt):
    print("Errate die Hauptstadt!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == hauptstadt.lower():
        print("Richtig! Das ist die Hauptstadt von", land)
    else:
        print("Falsch! Die richtige Hauptstadt von", land, "ist", hauptstadt)

def errate_kontinent(land, kontinent):
    print("Errate den Kontinent!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == kontinent.lower():
        print("Richtig! Das Land", land, "befindet sich auf dem Kontinent", kontinent)
    else:
        print("Falsch! Das Land", land, "befindet sich auf dem Kontinent", kontinent)

def errate_hoechste_erhebung(land, hoechste_erhebung):
    print("Errate die höchste Erhebung!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == hoechste_erhebung.lower():
        print("Richtig! Die höchste Erhebung von", land, "ist", hoechste_erhebung)
    else:
        print("Falsch! Die höchste Erhebung von", land, "ist", hoechste_erhebung)

def errate_laengster_fluss(land, laengster_fluss):
    print("Errate den längsten Fluss!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == laengster_fluss.lower():
        print("Richtig! Der längste Fluss von", land, "ist", laengster_fluss)
    else:
        print("Falsch! Der längste Fluss von", land, "ist", laengster_fluss)

def errate_bundesland(land, bundesland):
    print("Errate das Land!")
    print("Bundesland:", bundesland)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == bundesland.lower():
        print("Richtig! Das Land", land, "hat das Bundesland", bundesland)
    else:
        print("Falsch! Das Land", land, "hat das Bundesland", bundesland)



# Beispiel-Daten
hauptstaedte = {
    "Deutschland": "Berlin",
    "Frankreich": "Paris",
    "Spanien": "Madrid",
    "Italien": "Rom",
    "Kanada": "Ottawa",
    "Australien": "Canberra",
    "Südafrika": "Pretoria",
    "Indonesien": "Jakarta",
    "Estland": "Tallinn",
    "Uruguay": "Montevideo",
    "Bangladesch": "Dhaka",
    "Kirgisistan": "Bischkek"
}

kontinente = {
    "Deutschland": "Europa",
    "Frankreich": "Europa",
    "Spanien": "Europa",
    "Italien": "Europa",
    "Kanada": "Nordamerika",
    "Australien": "Australien",
    "Südafrika": "Afrika",
    "Indonesien": "Asien",
    "Estland": "Europa",
    "Uruguay": "Südamerika",
    "Bangladesch": "Asien",
    "Kirgisistan": "Asien"
}

hoechste_erhebungen = {
    "Deutschland": "Zugspitze",
    "Frankreich": "Mont Blanc",
    "Spanien": "Teide",
    "Italien": "Monte Bianco",
    "Kanada": "Mount Logan",
    "Australien": "Mount Kosciuszko",
    "Südafrika": "Tafelberg",
    "Indonesien": "Puncak Jaya",
    "Estland": "Suur Munamägi",
    "Uruguay": "Cerro Catedral",
    "Bangladesch": "Keokradong",
    "Kirgisistan": "Pik Pobedy"
}

laengste_fluesse = {
    "Deutschland": "Rhein",
    "Frankreich": "Seine",
    "Spanien": "Ebro",
    "Italien": "Po",
    "Kanada": "Mackenzie River",
    "Australien": "Murray River",
    "Südafrika": "Orange River",
    "Indonesien": "Kapuas River",
    "Estland": "Pärnu River",
    "Uruguay": "Uruguay River",
    "Bangladesch": "Jamuna River",
    "Kirgisistan": "Naryn River"
}

bundeslaender = {
    "Deutschland": "Bayern",
    "Frankreich": "Île-de-France",
    "Spanien": "Madrid",
    "Italien": "Latium",
    "Kanada": "Ontario",
    "Australien": "New South Wales",
    "Südafrika": "Gauteng",
    "Indonesien": "Java",
    "Estland": "Harju",
    "Uruguay": "Montevideo",
    "Bangladesch": "Dhaka",
    "Kirgisistan": "Tschüi"
}


eingeloggt = False

def inventar_leeren():
    # Das Inventar der aktuellen Benutzer-ID aus der Datenbank löschen
    c.execute('''DELETE FROM inventar WHERE benutzer_id = ?''', (benutzer[0],))
    conn.commit()

while True:
    # Hauptmenü anzeigen
    print(Fore.YELLOW + "Willkommen zum Textadventure!" + Style.RESET_ALL)
    print("1 - Registrieren")
    print("2 - Anmelden")
    print("3 - Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        # Registrierungsprozess starten
        name = input("Benutzername: ")
        passwort = input("Passwort: ")
        registrieren(name, passwort)

    elif auswahl == "2":
        # Anmeldeprozess starten
        name = input("Benutzername: ")
        passwort = input("Passwort: ")
        benutzer = anmelden(name, passwort)
        if benutzer:
            eingeloggt = True

    elif auswahl == "3":
        # Programm beenden
        break

    else:
        print(Fore.RED + "Ungültige Auswahl!" + Style.RESET_ALL)

    while eingeloggt:
        # Spiel-Loop
        print(Fore.GREEN + "Du bist eingeloggt!" + Style.RESET_ALL)
        print("1 - Inventar anzeigen")
        print("2 - Abenteuer beginnen")
        print("3 - Ausloggen")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            # Inventar anzeigen
            c.execute('''SELECT * FROM inventar WHERE benutzer_id = ?''', (benutzer[0],))
            inventar = c.fetchall()
            if inventar:
                print(Fore.CYAN + "Dein Inventar:" + Style.RESET_ALL)
                for item in inventar:
                    print(item[2], "x", item[3])

                print(">---------------------------------------<")
            else:
                print(Fore.CYAN + "Dein Inventar ist leer." + Style.RESET_ALL)
                print(">---------------------------------------<")

        elif auswahl == "2":
            # Abenteuer beginnen
            print("Du betrittst einen dunklen Wald...")
            print("Du findest einen Schatz!")
            print("1 - Schatz öffnen")
            print("2 - Schatz ignorieren")

            auswahl = input("Auswahl: ")

            if auswahl == "1":
                # Schatz öffnen
                print("Im Schatz findest du eine mächtige Waffe!")
                print("1 - Waffe nehmen")
                print("2 - Waffe liegen lassen")

                auswahl = input("Auswahl: ")

                if auswahl == "1":
                    # Waffe nehmen
                    print("Du nimmst die Waffe und fühlst ihre Macht!")
                    print("Du hast das Abenteuer erfolgreich bestanden!")
                    # Inventar hinzufügen
                    inventar_hinzufügen(benutzer[0], "Waffe", 1)

                elif auswahl == "2":
                    # Waffe liegen lassen
                    print("Du entscheidest dich, die Waffe liegen zu lassen...")
                    print("Das Abenteuer geht weiter!")

            elif auswahl == "2":
                # Schatz ignorieren
                print("Du entscheidest dich, den Schatz zu ignorieren...")
                print("Das Abenteuer geht weiter!")

            print("Plötzlich wirst du von einem Ork angegriffen!")
            print("1 - Kämpfen")
            print("2 - Fliehen")

            auswahl = input("Auswahl: ")

            if auswahl == "1":
                # Kämpfen
                print("Der Ork verpasst dir einen Hieb mit seiner Keule und du stirbst...")
                print(Fore.RED + "Game Over!" + Style.RESET_ALL)
                inventar_leeren()
                break

            elif auswahl == "2":
                # Fliehen
                print("In der Ferne siehst du eine Burg!")
                print("Du gehst hinein und bist sicher.")
                print("-----------------------------------------")
                print("Du triffst einen Priester, der dich segnen möchte.")
                print("1 - du lässt dich segnen")
                print("2 - du lehnst ab")

                auswahl = input("Auswahl: ")

                if auswahl == "1":
                    # Segnen lassen
                    print("Du wirst gesegnet und spürst die Kraft Gottes!")
                    print("Das Abenteuer geht weiter!")

                    print("Plötzlich taucht ein mächtiger Drache vor dir auf!")
                    print("1 - Mit der gesegneten Waffe kämpfen")
                    print("2 - Den Drachen um Gnade bitten")
                    print("3 - Versuchen, davonzulaufen")

                    auswahl = input("Auswahl: ")

                    if auswahl == "1":
                        # Mit der gesegneten Waffe kämpfen
                        if "gesegnete Waffe" in inventar:
                            print("Mit deiner gesegneten Waffe wagst du den Kampf gegen den Drachen.")
                            # Hier kannst du den Kampf gegen den Drachen implementieren
                        else:
                            print("Du hast keine geeignete Waffe, um gegen den Drachen anzutreten. Du stirbst...")
                            print(Fore.RED + "Game Over!" + Style.RESET_ALL)
                            inventar_leeren()
                            break

                    elif auswahl == "2":
                        # Den Drachen um Gnade bitten
                        print("Du kniest nieder und bittest den Drachen um Gnade.")
                        print("Der Drache scheint mitfühlend zu sein und lässt dich unversehrt weiterziehen.")

                    elif auswahl == "3":
                        # Versuchen, davonzulaufen
                        print("Du versuchst, vor dem Drachen zu fliehen.")
                        # Hier kannst du die Fluchtmechanik implementieren

                    print("Du setzt dein Abenteuer fort und gelangst zu einem geheimnisvollen Tempel.")
                    print("1 - Den Tempel betreten")
                    print("2 - Den Tempel umgehen und weiterziehen")

                    auswahl = input("Auswahl: ")

                    if auswahl == "1":
                        # Den Tempel betreten
                        print("Du betrittst den Tempel und findest einen alten magischen Talisman.")
                        print("1 - Den Talisman mitnehmen")
                        print("2 - Den Talisman ignorieren")

                        auswahl = input("Auswahl: ")

                        if auswahl == "1":
                            # Den Talisman mitnehmen
                            print("Du nimmst den magischen Talisman an dich und spürst seine Macht.")
                            inventar_hinzufügen(benutzer[0], "Talisman", 1)

                        elif auswahl == "2":
                            # Den Talisman ignorieren
                            print("Du entscheidest dich, den magischen Talisman liegen zu lassen.")

                    elif auswahl == "2":
                        # Den Tempel umgehen und weiterziehen
                        print("Du entscheidest dich, den geheimnisvollen Tempel zu umgehen und weiterzuziehen.")

                elif auswahl == "2":
                    # ablehnen
                    print("Der Priester wird wütend und ersticht dich mit einem Dolch...")
                    print(Fore.RED + "Game Over!" + Style.RESET_ALL)
                    inventar_leeren()
                    break
