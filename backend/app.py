from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from utility import get_data
import json

get_data('trip')

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def home(path):
    if path == '':
        return send_from_directory(app.template_folder, 'index.html')
    else:
        return send_from_directory(app.template_folder, path)

@app.route('/data/<type>')
def trip_json(type):
    with open(f'json/{type}.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")