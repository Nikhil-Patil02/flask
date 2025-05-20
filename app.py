from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

devices = {}

@app.route('/register', methods=['POST'])
def register_device():
    data = request.get_json()
    device_id = data.get('device_id')
    ip = data.get('ip')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    devices[device_id] = {"ip": ip, "last_seen": timestamp}
    return jsonify({"status": "ok", "device_id": device_id}), 200

@app.route('/')
def index():
    return jsonify(devices)

if __name__ == '__main__':
    app.run(debug=True)
