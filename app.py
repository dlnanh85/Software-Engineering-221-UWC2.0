from flask import Flask, render_template, request, session, redirect
from cs50 import SQL
from flask_session import Session
import json
import os

app = Flask(__name__)


#Get data
filename = os.path.join(app.static_folder, 'User.json')
f = open(filename)
users = json.load(f)["User"]
f.close()

filename = os.path.join(app.static_folder, 'Worker.json')
f = open(filename)
workers = json.load(f)["Worker"]
f.close()

filename = os.path.join(app.static_folder, 'Vehicle.json')
f = open(filename)
vehicles = json.load(f)["Vehicle"]
f.close()


# Configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    if not session.get('user'):
        return redirect('/login')
    return render_template('index.html')



# BEGIN: Authentication
def userAuth():
    for user in users:
        if session['user'] == user['username'] and session['pwd'] == user['password']:
            return True
    
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form.get('user')
        session['pwd'] = request.form.get('pwd')
        if userAuth(): 
            return redirect('/')         
        else:
            session['user'] = None
            return render_template('login.html', userAuth=0)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect('/')
# END: Authentication


# BEGIN: WORKER
@app.route('/worker')
def worker():
    return render_template('worker.html', workers=workers)

# END: WORKER

# BEGIN: VEHICLE
@app.route('/vehicle')
def vehicle():
    return render_template('vehicle.html', vehicles=vehicles)
# END: VEHICLE

# BEGIN: MCP
@app.route('/mcp')
def mcp():
    return render_template('mcp.html')
# END: MCP