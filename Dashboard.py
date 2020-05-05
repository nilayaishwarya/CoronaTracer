from CoronaTrackerDashboard.Functions.daily_assessment import dailyassessment
from CoronaTrackerDashboard.Functions.data_raw import getdata_raw
from CoronaTrackerDashboard.Functions.data_statewise import getdata_state
from CoronaTrackerDashboard.Functions.getresult_result_city import getresult_result_city
from CoronaTrackerDashboard.Functions.getresult_result_state import getresult_result_state
from CoronaTrackerDashboard.Functions.getresult_result_stateALL import getresult_result_stateALL
from CoronaTrackerDashboard.Functions.getresult_whole_country import getresult_whole_country
from CoronaTrackerDashboard.Functions.getUserInfo import getUserInfo
from CoronaTrackerDashboard.Functions.fetchDBraw import fetchDBraw
from CoronaTrackerDashboard.Functions.fetchDBstate import fetchDBstate
from CoronaTrackerDashboard.Functions.fetchDBChartTotal import fetchDBChartTotal
from CoronaTrackerDashboard.Functions.SymptomSave import SymptomSaveBasic
from CoronaTrackerDashboard.Functions.symptomfetch import SymptomCompute

import pymongo
import pandas as pd
from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import lxml.html as lh
import json
from flask import Flask,jsonify



def DashboardLoad(emailid):
    ##intializing None
        result_state = {}
        result_city = {}
        infoUserjson = {}
        info_basic_health = {}
        scoreneighborhood = {}
    # fetching data
        # df_raw1= getdata_raw()
        # df_statewise1 = getdata_state()
    # fetching data DB
        df_raw1= fetchDBraw()
        df_statewise1 = fetchDBstate()
        
    # get user data scarape from google sheets
        infoUser1 = getUserInfo(emailid) #"test_all@ty.com"
    # Whole country result
        result_whole_country = json.loads(getresult_whole_country(df_statewise1))
        if (len(infoUser1) != 0):
            result_state= json.loads(getresult_result_state(infoUser1.state[0],df_statewise1))
        result_stateALL = json.loads(getresult_result_stateALL(df_statewise1))
        if (len(infoUser1) != 0):
            result_city = json.loads(getresult_result_city(infoUser1.city[0],df_raw1))
            result_city.update( {'city' : infoUser1.city[0].upper()} )
            infoUserjson = json.loads(infoUser1.drop(['_id'], axis=1).to_json(orient='split'))
            info_basic_health = json.loads(infoUser1['risk_basic_health_score'].to_json(orient='split'))
        dailyassess = dailyassessment(emailid)
        if (len(infoUser1) != 0 and dailyassess != {}):
            x = SymptomSaveBasic(emailid,infoUser1.locality[0],infoUser1.city[0],infoUser1.state[0],info_basic_health['data'][0],dailyassess['risk_daily_health_score'],dailyassess['daily_prep_score'])
            scoreneighborhood = SymptomCompute(emailid,infoUser1.locality[0],infoUser1.city[0],infoUser1.state[0],info_basic_health['data'][0],dailyassess['risk_daily_health_score'],dailyassess['daily_prep_score'])
            

        response= {
            'result_country' : result_whole_country,
            'res_state' : result_state,
            'result_stateALL' : result_stateALL,
            'result_city':result_city,
            'infoUserjson' : info_basic_health,
            'dailyassess': dailyassess,
            'scoreneighborhood':scoreneighborhood
        }#
        #print(response)
        return response
#px= onse)

# x = DashboardLoad("nikita0808gupta@gmail.com") nikita0808gupta@gmail.com
# print(x)