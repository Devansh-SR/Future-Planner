from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    with open(DATA_FILE, 'r') as f:
        return jsonify(json.load(f))

@app.route('/save_task', methods=['POST'])
def save_task():
    tasks = []
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)
    
    new_data = request.json
    tasks = [t for t in tasks if not (t['title'] == new_data['title'] and t['start'] == new_data['start'])]
    tasks.append(new_data)
    
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f)
    return jsonify({"status": "success"})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    target = request.json
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)
    
    updated_tasks = [t for t in tasks if not (t['title'] == target['title'] and t['start'] == target['start'])]
    
    with open(DATA_FILE, 'w') as f:
        json.dump(updated_tasks, f)
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    print("🚀 Future Planner Online: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)