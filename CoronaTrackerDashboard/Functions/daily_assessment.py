import pymongo
import pandas as pd

def dailyassessment(email):
    client = pymongo.MongoClient("<link hidden>",connect=False)

    mydb = client.get_database('DailyData')
    records = mydb['DailyData']
    if(records.count_documents({'email' : email})==0):
        daily_score = {}
        return daily_score

    #df11 = pd.DataFrame(list(records.find()))
    df_test = pd.DataFrame(list(records.find({'email' : email})))
    
    df_test = df_test.iloc[::-1]
    #df11

    risk_daily_health_score = 0
    daily_prep_score = 0
    ###health
    if (df_test['hasCOVIDcontact'][0]=='Yes'):
        risk_daily_health_score+=100
    elif (df_test['hasCOVIDcontact'][0]=='Maybe not'):
        if (df_test['crowded'][0]=='Yes'):
            risk_daily_health_score+=50

    if (df_test['visitPublic'][0]=='Yes'):
            risk_daily_health_score+=30

    if (df_test['hasHeadache'][0]=='Yes'):
        if(df_test['sevHeadache'][0]=='Low'):
            risk_daily_health_score+=5
        elif(df_test['sevHeadache'][0]=='Medium'):
            risk_daily_health_score+=10
        else:
            risk_daily_health_score+=15

    if (df_test['hasDrycough'][0]=='Yes'):
        if(df_test['sevDrycough'][0]=='Low'):
            risk_daily_health_score+=5
        elif(df_test['sevDrycough'][0]=='Medium'):
            risk_daily_health_score+=10
        else:
            risk_daily_health_score+=15

    if (df_test['hasFever'][0]=='Yes'):
        if(df_test['sevFever'][0]=='Low'):
            risk_daily_health_score+=5
        elif(df_test['sevFever'][0]=='Medium'):
            risk_daily_health_score+=10
        else:
            risk_daily_health_score+=15

    if (df_test['hasDiffbreathing'][0]=='Yes'):
        if(df_test['sevDiffbreathing'][0]=='Low'):
            risk_daily_health_score+=10
        elif(df_test['sevDiffbreathing'][0]=='Medium'):
            risk_daily_health_score+=20
        else:
            risk_daily_health_score+=30

    if (df_test['hasDigestiveIssue'][0]=='Yes'):
        if(df_test['sevDigestiveIssue'][0]=='Low'):
            risk_daily_health_score+=5
        elif(df_test['sevDigestiveIssue'][0]=='Medium'):
            risk_daily_health_score+=10
        else:
            risk_daily_health_score+=15


    if (df_test['hasBodyache'][0]=='Yes'):
        if(df_test['sevBodyache'][0]=='Low'):
            risk_daily_health_score+=5
        elif(df_test['sevBodyache'][0]=='Medium'):
            risk_daily_health_score+=10
        else:
            risk_daily_health_score+=15

    ### risk_daily_prep_score

    if (df_test['hasSanitizer'][0]=='Yes'):
        daily_prep_score += 5

    if (df_test['hasMask'][0]=='Yes'):
        daily_prep_score += 5 


    df_test['risk_daily_health_score'] = (risk_daily_health_score/135)*10
    df_test['daily_prep_score']=daily_prep_score

    risk_daily_health_score_factor = round((risk_daily_health_score/135)*10,2)
    daily_prep_score_factor = daily_prep_score

    ### 235  10
    daily_score = {
        'risk_daily_health_score' : risk_daily_health_score_factor,
        'daily_prep_score' : daily_prep_score_factor
    }
    return daily_score