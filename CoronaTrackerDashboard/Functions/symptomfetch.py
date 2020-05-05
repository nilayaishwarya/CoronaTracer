import pymongo

def SymptomCompute(email,locality, city, state, scorebasic,scoredaily, prepscore):
    ##Just locality match for now
    locality = locality.upper().strip()
    city = city.upper().strip()
    state = state.upper().strip()
    scorebasic = float(scorebasic)
    scoredaily = float(scoredaily)
    prepscore = float(prepscore)

    scorebasicsoc = 0
    scoredailysoc = 0
    prepscoresoc = 0

    client = pymongo.MongoClient("<link hidden>",connect=False)

    mydb = client.get_database('SocietySymptom')
    records = mydb['SocietySymptom']
    recno = records.count_documents({'locality' : locality})
    totrec = records.find({'locality' : locality})
    for i in totrec:
        scorebasicsoc += i['scorebasic']
        scoredailysoc += i['scoredaily']
        prepscoresoc += i['prepscore']

    scorebasicsoc = round(scorebasicsoc/recno,2)
    scoredailysoc = round(scoredailysoc/recno,2)
    prepscoresoc = round(prepscoresoc/recno,2)
    locality = locality + " (Users: "+ str(recno) +")"
    scoreneighborhood = {
        'locality' : locality,
        'scorebasicsoc' : scorebasicsoc,
        'scoredailysoc' : scoredailysoc,
        'prepscoresoc' : prepscoresoc
    }

    return scoreneighborhood