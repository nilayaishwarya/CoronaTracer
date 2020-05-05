##chart total

from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import pandas as pd
import lxml.html as lh
import json
from flask import Flask,jsonify
import pymongo

def getchartTotal():
    respond_statewise = requests.get("<link hidden>")
    soup = BeautifulSoup(respond_statewise.text, features="lxml")
    p = soup.find("div", {"id": "387368559"})
    t = p.find_all('tr')
    l=[]
    col_charttotal=[]
    row=0
    for i in t:
        l = i.find_all('td')
        row2=0
        for tdd in l:
            if(row==1 and row!=4):
                name = tdd.get_text()
                col_charttotal.append((name,[]))
            elif(row!=3):  #To remove an empty row
                col_charttotal[row2][1].append(tdd.get_text())
                row2+=1  
        row=row+1

    #print(col_charttotal)
    Dict_charttotal={title:column for (title,column) in col_charttotal}
    df_charttotal=pd.DataFrame(Dict_charttotal)
    
    ###Saving to db
    dftest= df_charttotal
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('ChartTotal')
    records = mydb['ChartTotal']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_chart_total")
    records.insert_many(dftest_json)

    return True