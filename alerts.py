#!/bin/python

"""
xeroceph - https://github.com/xeroceph/pihole-alerts
GNU General Public License GPL v3.0 - https://www.gnu.org/licenses/gpl-3.0.en.html
"""

from config import *
from mon import searchQueries
from mail import sendMail
import requests

url = piAddr + '/admin/api.php?getAllQueries&auth=' + apiKey

try:
    r = requests.get(url)
    queries = r.json()
except:
    pass
    #print r.status_code

results = searchQueries(queries, blacklist)

for i in results:
    try:
        sendMail(i)
    except:
        pass
