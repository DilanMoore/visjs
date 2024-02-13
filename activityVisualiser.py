import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px


def generateActivityPlots():

    # Import session data from the JSON

    with open('nonVar_session_restructured.js', 'r') as f:
        sessionData = json.load(f)


    # Retrieve specific message data from the dataframe

    messageData = pd.DataFrame(sessionData[0]['messages'])


    # Create holders for each summary statistic

    messageData["messageCount"] = 1
    messageData["charCount"] = messageData["message"].str.len()

    messageData["rawCharCount"] = messageData["message"].str.len()


    # Generate and populate with summary statistics

    messageData["totalActivity"] = messageData.rolling(10).mean()["charCount"]

    messageData["messageCount"] = messageData.groupby(by = "player").cumsum()["messageCount"]

    messageData["charCount"] = messageData.groupby(by = "player").cumsum()["charCount"]


    # Generate individual player character activity plot

    p = so.Plot(messageData, "datetime", "charCount", color = "player")#.facet("player")
    p = p.add(so.Area())
    p.save("snsPlot.png")


    # Generate total activity summary plot for 

    fig = px.area(messageData, x="datetime", y="totalActivity")
    fig.show()
    fig.write_html("totalActivity.html")


    # Generate player activity plot (interactive)

    p = px.line(messageData, "datetime", "charCount", color = "player")#.facet("player")
    p.show()
    p.write_html("playerCharActivity.html")

