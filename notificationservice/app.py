from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/notify', methods=['POST'])
def send_notification():
    # In real use, we'd grab request data and send an actual notification
    return jsonify({"message": "Notification sent!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
