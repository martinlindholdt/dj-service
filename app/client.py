from urlparse import urlparse
from threading import Thread
from time import sleep, time
import httplib, sys


concurrent = 20

if (len(sys.argv)>1 and sys.argv[1]):
    url=sys.argv[1].strip
else: 
    url="http://dj.liquid.int.tdk.dk"

active = True 

def doWork():
    while active: 

        status, content, elapsed_time, iurl = getStatus(url)
        doSomethingWithResult(status, content, elapsed_time, iurl)

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)   
        start_time = time()
        #conn.request("HEAD", url.path)
        conn.request("GET", url.path)
        res = conn.getresponse()
        #print res.msg 
        #print res.getheaders()
        #print "read: "
        #print res.read()
        elapsed_time = time() - start_time
        return res.status, res.read(), elapsed_time, ourl
    except Exception as e: 
        print e
        return "error", "None", 0, ourl

def doSomethingWithResult(status, content, elapsed_time, iurl):
    print status, content, elapsed_time

for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    while active:
        pass
except KeyboardInterrupt:
    print "Exit"
    active = False
    sleep(5)
    sys.exit(1)