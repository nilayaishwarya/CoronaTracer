import requests
import pandas as pd
import json
import pymongo

def getdata_raw():
    df_raw = pd.read_csv('<link hidden>')
    df_raw = df_raw[df_raw['Date Announced'].notna()]
    #df_raw.str.upper()
    df_raw['Detected State'] = df_raw['Detected State'].str.upper()
    df_raw['Detected City'] = df_raw['Detected City'].str.upper()
    df_raw['Detected District'] = df_raw['Detected District'].str.upper()
    
    ###Saving to db
    dftest= df_raw
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('DataRaw')
    records = mydb['DataRaw']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_raw")
    records.insert_many(dftest_json)
    return True


