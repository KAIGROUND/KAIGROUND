import firebase_admin
from flask import Flask, request
from flask_cors import CORS
from firebase_admin import credentials, db
from threading import Thread, Timer
import sys
import time

app=Flask(__name__)
CORS(app)
cred = credentials.Certificate("./kaist-freshman-game-firebase-adminsdk-8xps2-5c0970a8f2.json")
admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://kai-ground-default-rtdb.firebaseio.com'})
game_thread = None


status = db.reference('status')

time_idx=None
T=[120,5,300,5]


def set_value(ref, child, val):
    db.reference(ref).child(child).set(val)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = Timer(sec, func_wrapper)
    t.start()
    return t

def every_second():
    global time_idx

    #mode 0 : move, 1: bg, 2: wait

    #2분 시작할 때
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == 0:
        turn = time_idx // (T[0] + T[1] + T[2] + T[3]) + 1
        if turn > 15:
            sys.exit()
        set_value("status", "turn", turn)
        set_value("status", "mode", 0)

    #2분 끝나고 4초
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + 4):
        pass

    #5분 시작할 때
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + T[1]):
        set_value("status", "mode", 1)

    #5분 끝나고 4초
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + T[1] + T[2] + 4):
        pass


    # Update
    time_idx += 1
    set_value("status", "time_idx", time_idx)

def run_game():
    global time_idx
    set_value("status", "mode", 2)
    time.sleep(1)
    time_idx = status.child('time_idx').get()

    #initialization from time_idx (For exeption)
    set_value("status", "turn", time_idx // (T[0] + T[1] + T[2] + T[3]) + 1)
    if time_idx % (T[0] + T[1] + T[2] + T[3]) < T[0]:
        set_value("status", "mode", 0)
    elif (T[0] + T[1]) < time_idx % (T[0] + T[1] + T[2] + T[3]) < (T[0] + T[1] + T[2]):
        set_value("status", "mode", 1)

    set_interval(every_second, 1)

@app.route('/admin_init')
def admin_init():
    idx = request.args.get('time_idx')

    if idx is not None:
        set_value("status", "time_idx", int(idx))
    else:
        set_value("status", "time_idx", 0)

    game_thread = Thread(target=run_game)
    game_thread.start()
    return 'Start to run'

@app.route('/test')
def test():
    return 'Hello'


if __name__ == "__main__":
    app.run()