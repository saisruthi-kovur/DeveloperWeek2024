from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import json
from threading import Lock
from datetime import datetime

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

thread = None
thread_lock = Lock()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(5)  # Sleep for 5 seconds
        count += 1
        timestamp = datetime.now().isoformat()
        # Emit the event along with some mock data
        socketio.emit('update', {'time': timestamp, 'value': random.random(), 'count': count})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@socketio.on('connect')
def on_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

if __name__ == '__main__':
    socketio.run(app, debug=True)