import os, sys, random 
from bottle.bottle import route, run, template
from time import sleep 


rndwait = False 

def setWait(): 
    if rndwait: 
        return random.randint(0, 5)
    else: 
        return 0


@route('/hello/<name>')
def index(name):
    return template('<b>Hello, {{name}}!</b>', name=name)

@route('/')
def index():
    waittime = setWait()
    sleep(waittime)
    host = os.getenv('HOSTNAME', 'unknown host')
    version = os.getenv('VERSION', 'unknown version')
    return template('{{host}} running {{version}} waiting {{wait}} seconds', host=host, version= version, wait=waittime)

@route('/random/<state>')
def doRandom(state):
    global rndwait
    if state == "on" or state == "true": 
        rndwait = True 
    else: 
        rndwait = False
    return template('Random repsonsetime 0-5 seconds now {{rndwait}}</b>', rndwait=rndwait)

@route('/crash') 
def crachApp(): 
    sys.stderr.close() # rather ugly hack but there are no exit function 
    return "<h1>Goodbye cruel world...</h2>"


@route('/health')
def alive():
    return "true"

run(host='0.0.0.0', port=8080, reloader=True)
