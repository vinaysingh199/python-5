from flask import Flask, jsonify
import datetime
import os
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        'hostname': os.uname().nodename,
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'Deployed_on': 'Kubernetes',
        'app_name': 'python-5',
        'env': 'dev'
        })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        "status": "healthy"
        })
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
