from CoronaTrackerDashboard.Functions.data_raw_v2 import getdata_raw
from CoronaTrackerDashboard.Functions.data_statewise_v2 import getdata_state
from CoronaTrackerDashboard.Functions.chartTotal_v2 import getchartTotal
import pymongo
import pandas as pd
import requests
import time
from apscheduler.schedulers.background import BlockingScheduler

def updateDBdata():
    x = getdata_raw()
    print("PASS_RAW")
    print(x)
    y = getdata_state()
    print("PASS_STATE")
    print(y)
    z = getchartTotal()
    print("PASS_CHART")
    print(z)
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

scheduler = BlockingScheduler()
scheduler.add_job(func=updateDBdata, trigger="interval", seconds=900)
scheduler.start()