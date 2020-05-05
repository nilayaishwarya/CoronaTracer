import pymongo
import pandas as pd

def fetchDBraw():
    client = pymongo.MongoClient("<link hidden>",connect=False)

    mydb = client.get_database('DataRaw')
    records = mydb['DataRaw']

    df_test = pd.DataFrame(list(records.find({})))
    df_delid = df_test.drop(['_id'], axis=1)
    return df_delid


