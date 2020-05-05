import pandas as pd
import pymongo

def getdata_state():
    df_statewise = pd.read_csv('<link hidden>')
    df_statewise['State'] = df_statewise['State'].str.upper()

    ###Saving to db
    dftest= df_statewise
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('DataState')
    records = mydb['DataState']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_state")
    records.insert_many(dftest_json)

    return True
