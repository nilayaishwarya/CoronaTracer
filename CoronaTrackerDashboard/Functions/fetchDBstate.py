import pymongo
import pandas as pd

def fetchDBstate():
    client = pymongo.MongoClient("<link hidden>",connect=False)

    mydb = client.get_database('DataState')
    records = mydb['DataState']

    df_test = pd.DataFrame(list(records.find({})))
    df_delid = df_test.drop(['_id'], axis=1)
    return df_delid


