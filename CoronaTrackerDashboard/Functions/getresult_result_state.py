def getresult_result_state(stateName,df_statewise):
    statetemp = stateName.upper().strip()
    ## state fixes
    if(stateName.upper().strip() == "ORISSA"):
        statetemp = "ODISHA"
    df_temp= df_statewise[df_statewise['State']== statetemp]
    return df_temp.to_json(orient='split')