import json
import pandas as pd
import numpy as np

import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
hv.extension('bokeh')
hv.output(size=200)

def generateChordPlot():
    with open('nonVar_session_restructured.js', 'r') as f:
        sessionData = json.load(f)

    playerList = []
    for message in sessionData[0]['messages']:
        player = message['player']
        if player not in playerList:
            playerList.append(player)

    mentionDict = dict.fromkeys(playerList)
    for player in playerList:
        mentionDict[player] = []

    for message in sessionData[0]['messages']:
        if len(message['mentions']) != 0:
            newMentions = message['mentions']
            player = message['player']
            
            if mentionDict[player] == None:
                mentionDict[player] = newMentions
            else:
                existingMentions = mentionDict[player]
                mentionDict[player] = existingMentions + newMentions#

    sourceList = []
    targetList = []
    valueList = []
    for key in mentionDict.keys():
        for item in mentionDict[key]:
            sourceList.append(key)
            targetList.append(item)
            valueList.append(1)
        
    mentionsDF = pd.DataFrame({"source" : sourceList, "target" : targetList, "value" : valueList, "name" : sourceList})

    try:
        chord = hv.Chord(mentionsDF)
        chord.opts(
        opts.Chord(cmap='Category20', edge_cmap='Category20', edge_color=dim('source').str(), 
                labels='name', node_color=dim('index').str()))
        hv.save(chord, "chordPlot.html")
# Dump as a JSON for easy embedding??
       # item_text = json.dumps(json_item(chord, "myplot"))
       # with open('data.json', 'w') as f:
       #     json.dump(data, f)

    except Exception:
        pass

    

    #hv.show(chord)