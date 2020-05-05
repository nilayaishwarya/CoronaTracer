import pandas as pd
import pymongo

def getchartTotal():
    df_charttotal = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
    ###Saving to db
    dftest= df_charttotal
    client = pymongo.MongoClient("mongodb+srv://dbadmin:dbadmin@coronotrackercluster-ajbco.mongodb.net/test?retryWrites=true&w=majority",connect=False)
    mydb = client.get_database('ChartTotal')
    records = mydb['ChartTotal']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_chart_total")
    records.insert_many(dftest_json)

    return True