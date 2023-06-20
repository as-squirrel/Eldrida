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
def errate_hauptstadt(land, korrekte_hauptstadt):
    print("Errate die Hauptstadt!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == korrekte_hauptstadt.lower():
        print("Richtig! Das ist die Hauptstadt von", land)
    else:
        print("Falsch! Die richtige Hauptstadt von", land, "ist", korrekte_hauptstadt)

def errate_kontinent(land, korrekter_kontinent):
    print("Errate den Kontinent!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == korrekter_kontinent.lower():
        print("Richtig! Das Land", land, "befindet sich auf dem Kontinent", korrekter_kontinent)
        return True
    else:
        print("Falsch! Das Land", land, "befindet sich auf dem Kontinent", korrekter_kontinent)
        return False


def errate_hoechste_erhebung(land, korrekte_hoechste_erhebung):
    print("Errate die höchste Erhebung!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == korrekte_hoechste_erhebung.lower():
        print("Richtig! Die höchste Erhebung von", land, "ist", korrekte_hoechste_erhebung)
    else:
        print("Falsch! Die höchste Erhebung von", land, "ist", korrekte_hoechste_erhebung)

def errate_laengster_fluss(land, korrekter_laengster_fluss):
    print("Errate den längsten Fluss!")
    print("Land:", land)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == korrekter_laengster_fluss.lower():
        print("Richtig! Der längste Fluss von", land, "ist", korrekter_laengster_fluss)
    else:
        print("Falsch! Der längste Fluss von", land, "ist", korrekter_laengster_fluss)

def errate_bundesland(land, korrektes_bundesland):
    print("Errate das Land!")
    print("Bundesland:", korrektes_bundesland)

    eingabe = input("Deine Antwort: ")

    if eingabe.lower() == korrektes_bundesland.lower():
        print("Richtig! Das Land", land, "hat das Bundesland", korrektes_bundesland)
    else:
        print("Falsch! Das Land", land, "hat das Bundesland", korrektes_bundesland)



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
                            print("Du betrittst den Tempel und findest eine wundersame alte Truhe.")
                            print("Du schaust sie dir genau an und merkst, sie kann nur durch ein Rätsel geöffnet werden.")
                            print("1 - Das Rätsel lösen")
                            print("2 - Die Truhe ignorieren")

                            auswahl = input("Auswahl: ")

                            if auswahl == "1":
                                # Das Rätsel lösen
                                print("Eine mystische Stimme erklingt und stellt dir ein Rätsel.")
                                korrekter_kontinent = kontinente["Deutschland"]
                                lösung_richtig = errate_kontinent("Deutschland", korrekter_kontinent)

                                if lösung_richtig:

                                    print("Wie von Zauberhand öffnet sich die Truhe und du findest einen alten magischen Talisman darin")
                                    print("1 - Talisman nehmen")
                                    print("2 - Talisman ignorieren")

                                    auswahl = input("Auswahl: ")

                                    if auswahl == "1":
                                        # Den Talisman mitnehmen
                                        print("Du nimmst den magischen Talisman an dich und spürst seine Macht.")
                                        inventar_hinzufügen(benutzer[0], "Talisman", 1)
                                        
                                        # Hier kannst du das neue Rätsel hinzufügen
                                        print("Als du den Talisman in deinem Inventar verstaut hast, entdeckst du eine geheimnisvolle Tür im Tempel.")
                                        print("Neben der Tür befindet sich eine Inschrift mit den Worten:")
                                        print("Errate die höchste Erhebung von Deutschland, um die Tür zu öffnen.")

                                        errate_hoechste_erhebung("Deutschland", hoechste_erhebungen["Deutschland"])

                                        # Fortsetzung der Geschichte nach dem Rätsel zur höchsten Erhebung
                                        print("Die Tür öffnet sich mit einem lauten Knarren und enthüllt einen dunklen Gang, der tiefer in den Tempel führt.")
                                        print("Du entscheidest dich, den Gang zu erkunden und gehst vorsichtig weiter.")
                                        print("Nach einigen Minuten erreichst du eine große Kammer, in der ein leuchtender Kristall auf einem Sockel thront.")
                                        print("Du spürst eine starke Energie, die von dem Kristall ausgeht.")
                                        print("1 - Den Kristall berühren")
                                        print("2 - Den Kristall ignorieren und weitergehen")

                                        auswahl = input("Auswahl: ")

                                        if auswahl == "1":
                                            # Den Kristall berühren
                                            print("Als du den Kristall berührst, strömt eine magische Energie durch deinen Körper.")
                                            print("Du fühlst dich gestärkt und erhältst neue Fähigkeiten.")
                                            print("1 - Feuerzauber")
                                            print("2 - Heilzauber")

                                            auswahl = input("Auswahl: ")

                                            if auswahl == "1":
                                                # Feuerzauber
                                                print("Du beherrschst nun den mächtigen Feuerzauber. Flammen entfachen sich um deine Hände.")
                                                inventar_hinzufügen(benutzer[0], "Feuerzauber", 1)
                                                print("Du nimmst den Feuerzauber in dein Inventar auf und fühlst dich bereit für kommende Herausforderungen.")
                                            elif auswahl == "2":
                                                # Heilzauber
                                                print("Du hast nun die heilende Macht in deinen Händen. Du kannst Wunden schließen und Gesundheit wiederherstellen.")
                                                inventar_hinzufügen(benutzer[0], "Heilzauber", 1)
                                                print("Du nimmst den Heilzauber in dein Inventar auf und fühlst dich bereit für kommende Herausforderungen.")
                                        
                                        elif auswahl == "2":
                                            # Den Kristall ignorieren
                                            print("Du entscheidest dich, den Kristall zu ignorieren und gehst weiter durch den Tempel.")
                                            print("Du bist gespannt, was dich noch erwartet.")

                                    elif auswahl == "2":
                                        # Den Talisman ignorieren
                                        print("Du entscheidest dich, den magischen Talisman liegen zu lassen und gehst wieder aus dem Tempel.")

                                else:
                                    print("Du hast das Rätsel nicht gelöst und die Truhe bleibt verschlossen")
                                    print("Du verlässt den Tempel und machst dich auf den Weg zu neuen Abenteuern.")

                        elif auswahl == "2":
                                # Die Truhe ignorieren
                                print("Du ignorierst die Truhe und gehst aus dem Tempel.")

                    elif auswahl == "2":
                            # Den Tempel umgehen und weiterziehen
                            print("Du entscheidest dich, den geheimnisvollen Tempel zu umgehen und weiterzuziehen.")
                            print("Wer weiß, was dich noch auf deinem Weg erwartet.")



                elif auswahl == "2":
                    # Ablehnen
                    print("Du setzt dein Abenteuer fort und gelangst zu einer tiefen Schlucht.")
                    print("1 - Über die Schlucht springen")
                    print("2 - Einen anderen Weg suchen")

                    auswahl = input("Auswahl: ")

    if auswahl == "1":
        # Über die Schlucht springen
        print("Du nimmst Anlauf und springst über die Schlucht.")
        print("Es ist ein gewagter Sprung, aber du schaffst es sicher auf die andere Seite.")
        print("Du bist erleichtert und stolz auf deine Geschicklichkeit.")

    elif auswahl == "2":
        # Einen anderen Weg suchen
        print("Du entscheidest dich, einen anderen Weg um die Schlucht herum zu suchen.")
        print("Nach einiger Zeit entdeckst du eine schmale Brücke, die über die Schlucht führt.")
        print("Du gehst vorsichtig über die Brücke und erreichst sicher die andere Seite.")

    print("Während deines Abenteuers kommst du an einem verlassenen Dorf vorbei.")
    print("1 - Das Dorf erkunden")
    print("2 - Am Dorf vorbeiziehen")

    auswahl = input("Auswahl: ")
    
    
    print("Neugierig entscheidest du dich, das verlassene Dorf zu erkunden.")
print("Du betrittst die engen Gassen des Dorfes und siehst, dass die Häuser verfallen sind und von der Natur zurückerobert werden.")
print("Es herrscht eine unheimliche Stille, die nur vom leisen Rascheln des Windes durchbrochen wird.")
print("Während du dich durch die verlassenen Straßen bewegst, bemerkst du, dass viele der Häuser geplündert wurden und persönliche Gegenstände verstreut sind.")

print("Plötzlich hörst du ein leises Weinen aus der Ferne.")
print("Du folgst dem Klang und gelangst zu einem kleinen Haus am Ende des Dorfes.")
print("Die Tür steht halb offen, und du hörst das Schluchzen immer lauter werden.")
print("Du betrittst das Haus und findest eine junge Frau, die verzweifelt in einer Ecke sitzt.")

print("1 - Die Frau ansprechen")
print("2 - Das Haus verlassen")

auswahl = input("Auswahl: ")

if auswahl == "1":
    # Die Frau ansprechen
    print("Du gehst langsam auf die Frau zu und sprichst sie sanft an.")
    print("Sie schaut auf, Tränen rinnen über ihr Gesicht.")
    print("Sie erzählt dir, dass das Dorf von einer dunklen Macht heimgesucht wurde, die die Bewohner vertrieben hat.")
    print("Ihre Familie wurde getrennt, und sie ist die einzige, die zurückgeblieben ist.")

    print("1 - Die Frau trösten und Hilfe anbieten")
    print("2 - Das Dorf verlassen und das Abenteuer fortsetzen")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        # Die Frau trösten und Hilfe anbieten
        print("Du setzt dich zu der Frau und nimmst ihre Hand.")
        print("Du versicherst ihr, dass du ihr helfen wirst, ihre Familie wiederzufinden und das Dorf von der dunklen Macht zu befreien.")
        print("Ihr Gesicht hellt sich etwas auf, und sie bedankt sich für deine Unterstützung.")

        print("Gemeinsam macht ihr euch auf den Weg, das Dorf zu erkunden und Hinweise auf die vermissten Familienmitglieder zu finden.")
        print("Ihr durchsucht die Häuser, sprecht mit den wenigen verbliebenen Dorfbewohnern und stoßt auf immer mehr Anzeichen für die Präsenz der dunklen Macht.")

        print("Nach einiger Zeit entdeckt ihr einen alten, versteckten Eingang zu einer geheimen Höhle unter dem Dorf.")
        print("Ihr entscheidet euch, hineinzugehen, in der Hoffnung, dort Antworten und vielleicht sogar eine Möglichkeit zur Befreiung des Dorfes zu finden.")
        
        print("Die Höhle ist düster und voller Gefahren. Ihr müsst euch an giftigen Spinnenweben vorbeischlängeln, über instabile Brücken balancieren und rätselhafte Mechanismen entschlüsseln, um weiterzukommen. Doch ihr gebt nicht auf und kämpft euch tapfer durch die Herausforderungen.")

print("Schließlich erreicht ihr den tiefsten Teil der Höhle, wo ihr auf eine finstere Gestalt trefft – den Anführer der dunklen Macht, der das Dorf terrorisiert. Es kommt zu einem epischen Kampf, bei dem ihr eure neugewonnene Waffe und Fähigkeiten einsetzt, um gegen den Anführer anzutreten. Ihr kämpft verbissen, während die Höhle von eurem Kampf widerhallt.")

print("Dank deiner geschärften Sinne und der mächtigen Waffe gelingt es dir, den Anführer der dunklen Macht zu bezwingen. Er verschwindet in einem dunklen Nebel, der sich langsam auflöst und die Höhle in ein warmes Licht taucht.")

print("Als der Nebel verzieht, erscheint ein geheimnisvolles Portal vor euch. Es scheint eine Verbindung zu einer anderen Dimension zu sein. Du spürst eine starke Präsenz und eine unerklärliche Anziehungskraft von jenseits des Portals.")

print("1 - Das Portal betreten")
print("2 - Das Portal ignorieren und zum Dorf zurückkehren")

auswahl = input("Auswahl: ")

if auswahl == "1":
    print("Du und die gerettete Frau treten gemeinsam durch das Portal und findet euch plötzlich in einer faszinierenden, aber fremden Welt wieder. Die Landschaft ist atemberaubend, mit schimmernden Wasserfällen, leuchtenden Pflanzen und exotischen Kreaturen.")
    
    print("Ihr erkundet diese neue Welt voller Abenteuer und Geheimnisse. Gemeinsam begebt ihr euch auf die Suche nach den vermissten Familienmitgliedern der Frau und stellt euch den Herausforderungen, die euch hier erwarten.")
    
    print("Im Laufe eurer Reise begegnet ihr faszinierenden Wesen und freundet euch mit einigen von ihnen an. Ihr entdeckt verborgene Schätze, die euch noch mächtiger machen, und gewinnt an Erfahrung und Weisheit.")
    
    print("Nach vielen aufregenden Abenteuern und harten Kämpfen gelingt es euch, die vermissten Familienmitglieder der Frau aufzuspüren und sie sicher zurückzubringen. Ihr habt euer Versprechen gehalten und das Dorf von der dunklen Macht befreit.")
    
    print("Das Dorf erblüht wieder in alter Pracht, und die Bewohner kehren zurück. Ihr werdet als Helden gefeiert und als Dank für euren Mut und eure Tapferkeit beschenkt. Die gerettete Frau ist dankbar für eure Hilfe und schließt sich euch an, um an eurer Seite weiter Abenteuer zu erleben.")
    
    print("Gemeinsam erkundet ihr die neue Welt")
    
    print("Die Frau fragt dich ob du mit ihr Im dorf bleiben willst oder dir ein neues Arbenteuer suchst")

        

        
        
    
  
