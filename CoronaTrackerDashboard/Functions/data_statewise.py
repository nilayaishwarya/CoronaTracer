from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import pandas as pd
import lxml.html as lh
import json
from flask import Flask,jsonify
import pymongo

def getdata_state():
    respond_statewise = requests.get("<link hidden>")
    soup = BeautifulSoup(respond_statewise.text, features="lxml")
    p = soup.find("div", {"id": "1896310216"})
    t = p.find_all('tr')
    l=[]
    col_statewise=[]
    row=0
    for i in t:
        l = i.find_all('td')
        p=0
        row2=0
        for tdd in l:
            if(row==1 and p!=1):
                name = tdd.get_text()
                col_statewise.append((name,[]))
            elif( p!=1 and row!=3):  #To remove an empty row
                col_statewise[row2][1].append(tdd.get_text())
                row2+=1  
            p=p+1
        row=row+1

    #print(col_statewise)
    Dict_statewise={title:column for (title,column) in col_statewise}
    df_statewise=pd.DataFrame(Dict_statewise)
    #df_statewise['State'].apply(lambda x: x.upper())
    df_statewise['State'] = df_statewise['State'].str.upper()

    ###Saving to db
    dftest= df_statewise
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('DataState')
    records = mydb['DataState']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_state")
    records.insert_many(dftest_json)

    return True
