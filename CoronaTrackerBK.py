from Dashboard import DashboardLoad
from CoronaTrackerDashboard.Functions.daily_assessment import dailyassessment
from CoronaTrackerDashboard.Functions.data_raw_v2 import getdata_raw
from CoronaTrackerDashboard.Functions.data_statewise_v2 import getdata_state
from CoronaTrackerDashboard.Functions.getresult_result_city import getresult_result_city
from CoronaTrackerDashboard.Functions.getresult_result_state import getresult_result_state
from CoronaTrackerDashboard.Functions.getresult_result_stateALL import getresult_result_stateALL
from CoronaTrackerDashboard.Functions.getresult_whole_country import getresult_whole_country
from CoronaTrackerDashboard.Functions.getUserInfo import getUserInfo
from CoronaTrackerDashboard.Functions.fetchDBraw import fetchDBraw
from CoronaTrackerDashboard.Functions.fetchDBstate import fetchDBstate
from CoronaTrackerDashboard.Functions.fetchDBChartTotal import fetchDBChartTotal
from CoronaTrackerDashboard.Functions.chartTotal_v2 import getchartTotal
from DBManualUpdate import updateDBdata
import pymongo
import pandas as pd
from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import lxml.html as lh
import json
from flask import Flask,jsonify,request
from flask import render_template
import requests
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS

app =  Flask(__name__)
CORS(app)
# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

# def updateDBdata():
#     x = getdata_raw()
#     print("PASS_RAW")
#     print(x)
#     y = getdata_state()
#     print("PASS_STATE")
#     print(y)
#     z = getchartTotal()
#     print("PASS_CHART")
#     print(z)
#     #print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=updateDBdata, trigger="interval", seconds=900)
# scheduler.start()

# Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return "Success"

@app.route('/Dashboard', methods=['POST'])
def Dashboard():
    if request.method == 'POST':
        email = request.json['email']
        response = DashboardLoad(email)
        return response

@app.route('/CountryLoad', methods=['GET'])
def CountryLoad():
    if request.method == 'GET':
        df_statewise1 = fetchDBstate()
        result_stateALL = json.loads(getresult_result_stateALL(df_statewise1))
        df_chartTotal = fetchDBChartTotal()
        chartTotal = json.loads(df_chartTotal.to_json(orient='split'))
        result_stateALL.update({ 'chartTotal' : chartTotal})
        return result_stateALL
        
@app.route('/DBMANUAL', methods=['GET'])
def DBMANUAL():
    if request.method == 'GET':
        ret = updateDBdata()
        return True

if __name__ == '__main__':
    app.run()