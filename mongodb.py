import redis
import pandas as pd
from pymongo import MongoClient
import time as t


def GetRedis():
    red = redis.Redis(host='test',port=6379, db=0)
    redi = red.get('scraperdf')
    redii = pd.read_json(redi)
    rediii = redii.sort_values(by = ['US Dollar'], ascending = False).head(1)
    rediiii = rediii.to_dict('records') #waardes en titles
    red.flushdb
    return rediiii

def MainMongo():
    try:
        connection = MongoClient('localhost', 27017)
        print("Connected")
    except:
        print("Could not connect to MongoDB")

    db = connection.scraper
    collect = db.scrapery

    scrapero = GetRedis()
    collect.insert_many(scrapero)

MainMongo()
        
while True:
    
    MainMongo()
    t.sleep(60)

