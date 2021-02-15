from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
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

login_id=[]
@app.route('/login')
def login():
    username = request.args.get('user_name') #GET method
    
    if username == 'Grace':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    return render_template('login.html')

@app.route('/server_info_sc') 
def server_json_sc():
    return make_response(jsonify({'success':True}), 200)

@app.route('/server_info_fl') 
def server_json_fl():
    return make_response(jsonify({'success':False}), 500)

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
    return "<h1>404 Error가 발생했습니다ㅠ</h1>", 404

if __name__=="__main__":
    app.run(host='127.0.0.1', port='5000', debug=1)