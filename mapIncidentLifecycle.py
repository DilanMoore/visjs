import pandas as pd
import json
import emoji
import matplotlib.pyplot as plt

#"session_restructured.js"

def mapSessionLifecycle():
    with open('nonVar_session_restructured.js', 'r') as f:
        sessionData = json.load(f)

    starHintLabels = pd.read_csv("starHintLifecycleLabels.csv", header = None).drop(0, axis = 0).drop(0, axis = 1)

    keys = starHintLabels[1].apply(lambda x: emoji.emojize(x, language='alias'))
    labels = starHintLabels[2]

    labelDict = dict(zip(keys, labels))
    sessionMessages = sessionData[0]['messages']

    flagList = []
    for message in sessionMessages:
        messageText = message['message']
        if messageText in labelDict.keys():
            message['lifecycleStage'] = labelDict[messageText]
        else: message['lifecycleStage'] = "None"

    for message in sessionMessages:
        if message["lifecycleStage"] != "None":
            plt.scatter(y = message['lifecycleStage'], x = message["datetime"][-8:])

    plt.title("Session "  + str(sessionData[0]['session_id']))
    plt.savefig('sessionLifecycle.png')
