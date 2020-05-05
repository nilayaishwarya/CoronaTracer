def getresult_result_stateALL(df_statewise):
    df_temp = df_statewise
    return df_temp.to_json(orient='split')