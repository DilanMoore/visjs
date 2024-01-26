import lokiGrabber
import sessionFilter
import webbrowser
import lokiProcesser
import jsonParser
import mapIncidentLifecycle

lokiGrabber.grabData()
lokiProcesser.processRawLokiData()

session = input("Please enter session ID as an integer: ")
sessionFilter.filterSession(session)

jsonParser.parseJSON()
jsonParser.structureJSON()

mapIncidentLifecycle.mapSessionLifecycle()
 
webbrowser.open_new_tab('index.html')