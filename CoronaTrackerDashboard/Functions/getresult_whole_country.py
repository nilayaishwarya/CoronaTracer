def getresult_whole_country(df_statewise):
    df_temp= df_statewise[df_statewise['State']=='TOTAL']
    return df_temp.to_json(orient='split')