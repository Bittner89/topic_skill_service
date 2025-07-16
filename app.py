# Importiere die nötigen module (json, os, flask , jsonify)

import json
import os
from flask import Flask, jsonify

#erstellung einer flask Anwendung

app = Flask(__name__)

# erstellen der Konstanten Variablen
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')

# erstellung einer instanz von Flask app und erstellung einer Haupt route
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'

# erstellen eines try except blocks, indem nach der datei gesucht wird. Wenn nicht existiert dann fehlermeldung ausgeben 

def read_json_file(filepath):
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
        return []
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
        return []
    
# erstellung einer instanz von Flask app und erstellung einer gemeinsamer topic liste mit get methode von json
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = read_json_file(TOPICS_FILE)
    return jsonify(topics) 
   
# Aufrufen der Haupt funktion
if __name__ == '__main__':
    app.run(debug=True, port=5000)
