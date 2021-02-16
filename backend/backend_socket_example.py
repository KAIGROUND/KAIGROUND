from flask import Flask
from flask_socketio import SocketIO, emit
import time
import schedule

app=Flask(__name__)
socketIo = SocketIO(app,cors_allowed_origins="*")
status={
    "running_time": 0
}
@socketIo.on("connect")
def handleMessage_connect():
    print("connected")

    return None

@socketIo.on("req_time")
def handleMessage_req_time(json):
    print(json)
    for i in range(250):
        time.sleep(0.25)
        emit("LEFT_TIME", i)


def connect_socket():
    socketIo.run(app, host='0.0.0.0', port=3001)

if __name__ == '__main__':
    connect_socket()
