from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
import pandas as pd
import lxml.html as lh
import json
from flask import Flask,jsonify
import io
from io import BytesIO
import requests
import pandas as pd
import lxml.html as lh
import pymongo

def getdata_raw():
    import io
    from io import BytesIO
    import requests
    import pandas as pd
    import lxml.html as lh
    
    url = '<link hidden>'
    page = requests.get(url)

    doc = lh.fromstring(page.content)

    result = doc.xpath('//table[@class="waffle"]')
    #Checking length
    tr_elements = result[1].xpath('//tr')
    # [print(len(T)) for T in tr_elements[:12]]

    col=[]
    i=0
    skip=1
    for t in tr_elements[1]:
        #print(i)
        i+=1
        if(skip==1):
            skip=0
            continue
        if(i>=20): #removed last column
            break
        name=t.text_content()
        #print (" %d : %s " % (i,name))
        col.append((name,[]))

    for j in range(3,len(tr_elements)):
        
        #if (j>=1266):
        #    break
        T=tr_elements[j]
        skip=1
        i=0
        if(T[3].text_content()==""):
            print(T[i])
            break
        for t in T.iterchildren():
            data=t.text_content()
            i=i+1
            if(skip==1):
                skip=0
                continue
            if(i>=20):
                break
            #print(t.text)
            try:
                data=int(data)
            except:
                pass
            col[i-2][1].append(data)


    Dict={title:column for (title,column) in col}
    df_raw=pd.DataFrame(Dict)
    #df_raw.str.upper()
    df_raw['Detected State'] = df_raw['Detected State'].str.upper()
    df_raw['Detected City'] = df_raw['Detected City'].str.upper()
    df_raw['Detected District'] = df_raw['Detected District'].str.upper()
    
    ###Saving to db
    dftest= df_raw
    client = pymongo.MongoClient("<link hidden>",connect=False)
    mydb = client.get_database('DataRaw')
    records = mydb['DataRaw']
    ## if time based data comes into picture
    records.delete_many({})
    dftest_json = dftest.to_dict("record_raw")
    records.insert_many(dftest_json)
    return True


