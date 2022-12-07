from flask import Flask, render_template, request, session, redirect
from cs50 import SQL
from flask_session import Session
import json

app = Flask(__name__)


# Configure database
seDB = SQL('mysql://root:158502@localhost:3306/SE')


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
    users = seDB.execute('SELECT * FROM User')
    
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
    workers = seDB.execute('SELECT * FROM Worker')
    return render_template('worker.html', workers=workers)

# END: WORKER

# BEGIN: VEHICLE
@app.route('/vehicle')
def vehicle():
    vehicles = seDB.execute('SELECT * FROM Vehicle')
    return render_template('vehicle.html', vehicles=vehicles)
# END: VEHICLE

# BEGIN: MCP
@app.route('/mcp')
def mcp():
    return render_template('mcp.html')
# END: MCP