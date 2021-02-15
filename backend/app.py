from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
from . import config
import logging
from logging.handlers import RotatingFileHandler 
from flask_login import UserMixin

app = Flask(__name__)
CORS(app)

'''
if not app.debug:
    file_handler = RotatingFileHandler('server.log', maxBytes=20000, backupCount=10)
    file_handler.setLevel(logging.WARNING)  
    app.logger.addHandler(file_handler)
'''
n_team = config.n_team
login_id=config.login_id
passwd=config.passwd
sv_ip=[]

@app.route('/login')
def login_html():
    return render_template('login.html')

@app.route('/login_post', methods=['POST'])
def login():
    data = request.get_json()
    if data['id'] in login_id and data['pass']==passwd:
        sv_ip.append(request.remote_addr)
        return render_template('game.html')
    return render_template("login.html")

@app.route('/game')
def game():
    if request.remote_addr not in sv_ip:
        return make_response("<h1>Access Denied</h1>", 404)
    return render_template('game.html')

@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()  #data is dict
        print(data)
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)
    return make_response(jsonify({'status': True}), 200)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Wrong Access</h1>", 404

if __name__=="__main__":
    app.run(host='127.0.0.1', port='5000', debug=1)