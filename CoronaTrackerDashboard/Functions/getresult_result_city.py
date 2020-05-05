def getresult_result_city(cityName,df_raw):
    #Khordha
    citytemp = cityName.upper().strip()

    ## city fixes
    if(cityName.upper().strip() == "BANGALORE"):
        citytemp = "BENGALURU"
    if(cityName.upper().strip() == "BHUBANESHWAR"):
        citytemp = "BHUBANESWAR"

    df_temp= df_raw[df_raw['Detected District']== citytemp]
    if(df_temp.shape[0]==0):
        df_temp= df_raw[df_raw['Detected City']== citytemp]

    df_temp = df_temp['Current Status'].value_counts()
    return df_temp.to_json(orient='split')