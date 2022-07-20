import urllib.request as request
import json
import sqlite3
import ssl
import time
from datetime import datetime

ts = time.time() + 28800
dt = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
filename = "{}.txt".format(dt)
with open('/Users/ct/Documents/Resume/Full-time/{}'.format(filename), 'w', encoding='UTF-8') as file:
    file.write('Created at {}'.format(dt))

ssl._create_default_https_context = ssl._create_unverified_context
src = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

with request.urlopen(src) as response:
    data = json.load(response)

blist = data['retVal']

import os.path

BASE_DIR = os.path.dirname(os.path.abspath("/Users/ct/Desktop/youbike.db"))
db_path = os.path.join(BASE_DIR, 'youbike.db')
conn = sqlite3.connect(db_path)
print ('opened database successfully')

cursor = conn.cursor()

for i in blist:
    sql = "INSERT INTO youbike_tp_table(sno, sna, tot, sbi, sarea, mday, lat, lng, ar, sareaen, snaen, aren, bemp, act) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(blist[i]['sno'], blist[i]['sna'], blist[i]['tot'], blist[i]['sbi'], blist[i]['sarea'], blist[i]['mday'], blist[i]['lat'], blist[i]['lng'], blist[i]['ar'], blist[i]['sareaen'], blist[i]['snaen'], blist[i]['aren'], blist[i]['bemp'], blist[i]['act'])

    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    else:
        conn.commit()

conn.close()
print("closed database successfully")