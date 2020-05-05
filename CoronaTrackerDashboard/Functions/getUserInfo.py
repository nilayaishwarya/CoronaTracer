import pymongo
import pandas as pd

def getUserInfo(email):
    import pymongo
    import pandas as pd
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('BasicInfo')
    records = mydb['BasicInfo']
    if(records.count_documents({'email' : email})==0):
        data=[]
        nodata = pd.DataFrame(data, columns = ['Empty'])
        return nodata

    df_temp = pd.DataFrame(list(records.find({ 'email' : email })))
    risk_basic_health_score = 0
    ###health
    if (df_temp['Diabetic']=='true').any() :
        risk_basic_health_score+=10
    if (df_temp['PastCardio']=='true').any():
        risk_basic_health_score+=10
    if (df_temp['PastResp']=='true').any():
        risk_basic_health_score+=10
    if (df_temp['travelled']=='true').any():
        risk_basic_health_score+=20

    df_temp['risk_basic_health_score']= (risk_basic_health_score/50)*10

    return df_temp
 
# x = getUserInfo(omeone@somewhere.com)
# print(x)