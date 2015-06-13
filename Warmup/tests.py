import signal
import urllib
import requests

try:
    r = requests.get("http://github.com", timeout = 0.001)
    
except requests.exceptions.Timeout as e:
    error = e[0][1]
    if error: print error
    else: print "connection timed out"
