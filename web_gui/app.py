from flask import Flask, render_template, request, jsonify
from modules.reconnaissance import whois_lookup, scan_ports

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whois', methods=['POST'])
def whois_lookup_api():
    domain = request.form['domain']
    result = whois_lookup(domain)
    return jsonify(result)

@app.route('/scan_ports', methods=['POST'])
def scan_ports_api():
    ip = request.form['ip']
    result = scan_ports(ip)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
