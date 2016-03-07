import requests
import time
import telepot as tp
import json
from datetime import datetime
import os

def messageMe(message):
    bot = tp.Bot('155578772:AAGngKO2rPtjzC2_P3CM7FSsL-FIAfzRk8A')
    bot.sendMessage(33612976, str(message))


def getData():
    res = requests.get('http://nanopool.org/api/user/0xa47cd1e0e031de09622b6ada5f80a291f302e711')
    data = json.loads(res.text)['data']
    return data

if __name__ == "__main__":
    while True:
        data=getData()
        print '>>>>>>>>>', str(datetime.now())
        print '>>>>>>>>>', 'Current Hashrate', data['hashrate']
        print 
        for j in [worker['hashrate'] for worker in data['workers']]:
            if j == '0.0':
                message = str(j)+"th worker is dead!!!"
                messageMe(message)
        for i in data['workers']:
            print i['id'], i['hashrate'], i['avg_h6']
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        time.sleep(60)

