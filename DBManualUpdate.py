from CoronaTrackerDashboard.Functions.data_raw_v2 import getdata_raw
from CoronaTrackerDashboard.Functions.data_statewise_v2 import getdata_state
from CoronaTrackerDashboard.Functions.chartTotal_v2 import getchartTotal
import pymongo
import pandas as pd
from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import lxml.html as lh
import json
import requests
import time

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
    return True


updateDBdata()