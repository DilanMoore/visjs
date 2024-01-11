import pandas as pd
import json


def parseJSON():

    with open('sessions.json', 'r') as f:
        input_json = json.load(f)

    # Serializing json
    json_object = json.dumps(input_json)
    
    # Writing to sample.json
    with open("session.js", "w") as outfile:
        outfile.write(json_object)
