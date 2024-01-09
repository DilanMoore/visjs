import lokiGrabber
import sessionFilter

lokiGrabber.grabData()
session = input("Please enter session ID as an integer: ")
sessionFilter.filterSession()