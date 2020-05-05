import pymongo

def SymptomSaveBasic(email,locality, city, state, scorebasic,scoredaily, prepscore):
    locality = locality.upper().strip()
    city = city.upper().strip()
    state = state.upper().strip()
    scorebasic = float(scorebasic)
    scoredaily = float(scoredaily)
    prepscore = float(prepscore)

    client = pymongo.MongoClient("<link hidden>",connect=False)

    mydb = client.get_database('SocietySymptom')
    records = mydb['SocietySymptom']
    if(records.count_documents({'email' : email})==0):
        records.insert_one({
           "email": email,
           "locality": locality,
           "city":city,
           "state":state,
           "scorebasic": scorebasic,
           "scoredaily": scoredaily,
           "prepscore": prepscore
        })
    else:
        records.update_one({"email":email},{ "$set" : {
           "scoredaily": scoredaily,
           "prepscore": prepscore
        }})

    return True


