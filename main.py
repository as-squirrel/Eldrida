import sqlite3
import pygame 
from pygame import mixer

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
eingeloggt = False
while True:
    # Hauptmenü anzeigen
    print("Willkommen zum Textadventure!")
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
        print("Ungültige Auswahl!")

    while eingeloggt:
        # Spiel-Loop
        print("Du bist eingeloggt!")
        print("1 - Inventar anzeigen")
        print("2 - Abenteuer beginnen")
        print("3 - Ausloggen")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            # Inventar anzeigen
            c.execute('''SELECT * FROM inventar WHERE benutzer_id = ?''', (benutzer[0],))
            inventar = c.fetchall()
            if inventar:
                print("Dein Inventar:")
                for item in inventar:
                    print(item[2], "x", item[3])
            else:
                print("Dein Inventar ist leer.")

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


            elif auswahl == "2":
            if auswahl == "1":
                # Kämpfen
                print("Der Ork verpasst dir einen Hieb mit seiner Keule und du stirbst...")
                print("Game Over!")
                break

            elif auswahl == "2":
                # Fliehen
                print("In der Ferne siehst du eine Burg!")
                print("Du gehst hinein und bist sicher.")
            
            print("Du triffst einen Priester, der dich segnen möchte.")
            print("1 - du lässt dich segnen")
            print("2 - du lehnst ab")
            
            auswahl = input("Auswahl: ")
            
            if auswahl == "1":
                # segnen lassen
                print("Du wirst gesegnet und spührst die Kraft Gottes!")
                print("Das Abenteuer geht weiter!")
                
            elif auswahl == "2":
                # ablehnen
                print("Der Priester wird wütend und ersticht dich mit einem Dolch...")
                print("Game Over!")
                break