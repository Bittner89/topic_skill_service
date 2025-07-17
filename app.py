# Importiere die nötigen module (json, os, flask , jsonify)

import os
from flask import Flask, jsonify
from data_manager import JsonDataManager
#erstellung einer flask Anwendung

app = Flask(__name__)
data_manager = JsonDataManager()
# erstellen der Konstanten Variablen
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')

# erstellung einer instanz von Flask app und erstellung einer Haupt route
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'

    
# erstellung einer instanz von Flask app und erstellung einer gemeinsamer topic liste mit get methode von json
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics) 
   
# Aufrufen der Haupt funktion
if __name__ == '__main__':
    app.run(debug=True, port=5000)
