import lokiGrabber
import sessionFilter
import webbrowser

lokiGrabber.grabData()
session = input("Please enter session ID as an integer: ")
sessionFilter.filterSession(session)
 
webbrowser.open_new_tab('index.html')