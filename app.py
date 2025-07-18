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
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')


# erstellung einer instanz von Flask app und erstellung einer Haupt route
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'

    
# erstellung einer instanz von Flask app und erstellung einer gemeinsamer topic liste mit get methode von json
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics) 


@app.route('/skills', methods=['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics = data_manager.read_data(TOPICS_FILE)
    topic = next((topic for topic in topics if topic.get('id').lower() == id).lower(), None)
    return jsonify(topic)


@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None)
    return jsonify(skill)

    
# Aufrufen der Haupt funktion
if __name__ == '__main__':
    app.run(debug=True, port=5000)
