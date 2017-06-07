# pyfwr

pywfr provides a simple but powerful way to access the flightaware FlightXML api.

simply call pyfwr.get() and pass it a map structure with the following three elements:
* a credentials map that encapsulates the username/apikey for your flightaware account 
* a string of the FlightXML operation you wish to call (see http://flightxml.flightaware.com/soap/FlightXML2/doc) 
* a map with the inputs required for the operation

pyfwr makes a REST api call and parses the JSON response such that it can be accessed programmatically

Refer to the examples.py file to see how it works
