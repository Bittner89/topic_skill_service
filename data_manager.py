import json
import os

class JsonDataManager:  #Eine Klasse zum Verwalten von JSON-Daten, die das Lesen aus und Schreiben in JSON-Dateien vereinfacht und Fehlerbehandlung integriert.

    def __init__(self):
        #Der Konstruktor der Klasse. Aktuell ist er leer, da für diese Funktionalität keine Initialisierungsparameter oder Instanzvariablen benötigt werden.
        pass



    def read_data(self, filepath):          #Liest Daten aus einer JSON-Datei.
        if not os.path.exists(filepath):
            return []
        
        # Überprüft, ob die angegebene Datei existiert.
        # Wenn nicht, gibt die Methode eine leere Liste zurück, da es nichts zu lesen gibt.
    
        try:                                                            #Erstellung eines try und except blocks. Um Fehler abzufangen.
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
            return []
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
            return []


    def write_data(self, filepath, data):       #Schreibt Daten in eine JSON-Datei.
                                                #Erstellt bei Bedarf die Verzeichnisse im Dateipfad.

        os.makedirs(os.path.dirname(filepath), exist_ok=True)       # Erstellt alle notwendigen Verzeichnisse im Pfad zur Datei, falls sie noch nicht existieren.
                                                                    # 'exist_ok=True' verhindert einen Fehler, wenn die Verzeichnisse bereits vorhanden sind.

        try:                                                        #Erstellung eines try und except blocks. Um Fehler abzufangen.
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                return True
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")
            return False       