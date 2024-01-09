import pandas as pd
#from pandasql import sqldf


#session = input("Please enter session ID as an integer")

def filterSession(session):

    data = pd.read_csv("raw_loki_data_new_prod.csv")
    sessionData = data.query("session_id == " + str(session))
    sessionData.to_csv("session_" + str(session) + ".csv", index=False)


