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
src = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

with request.urlopen(src) as response:
    data = json.load(response)

import os.path

BASE_DIR = os.path.dirname(os.path.abspath("/Users/ct/Desktop/youbike.db"))
db_path = os.path.join(BASE_DIR, 'youbike.db')
conn = sqlite3.connect(db_path)
print ('opened database successfully')

cursor = conn.cursor()

for i in range(len(data)):
    sql = "INSERT INTO youbike_tp20_table(sno, sna, tot, sbi, sarea, mday, lat, lng, ar, sareaen, snaen, aren, bemp, act) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(data[i]['sno'], data[i]['sna'], data[i]['tot'], data[i]['sbi'], data[i]['sarea'], data[i]['mday'], data[i]['lat'], data[i]['lng'], data[i]['ar'], data[i]['sareaen'], data[i]['snaen'], data[i]['aren'], data[i]['bemp'], data[i]['act'])

    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    else:
        conn.commit()

conn.close()
print('closed database successfully')