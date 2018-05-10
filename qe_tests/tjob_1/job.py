#!/usr/bin/env python
from openmtc_onem2m.client.http import OneM2MHTTPClient
from openmtc_onem2m.transport import OneM2MRequest


print "setting up http client"
client = OneM2MHTTPClient("http://eds-base:8000", False)
        
print "testing reachability of gateway"
request = OneM2MRequest("retrieve", to="onem2m")
promise = client.send_onem2m_request(request)
response = promise.get()

if response.response_status_code.http_status_code == 200:
    print "onem2m gateway found"
else:
    print "onem2m gateway not found"
    exit -1

print "testing reachability of EDSOrch"
request = OneM2MRequest("retrieve", to="onem2m/EDSOrch")
promise = client.send_onem2m_request(request)
response = promise.get()

if response.response_status_code.http_status_code == 200:
    print "EDSOrch found"
else:
    print "EDSOrch not found"
    exit -1

print "testing reachability of SuT"
request = OneM2MRequest("retrieve", to="onem2m/EDSOrch/testapplication")
promise = client.send_onem2m_request(request)
response = promise.get()

if response.response_status_code.http_status_code == 200:
    print "SuT found"
else:
    print "SuT not found"
    exit -1

print "testing reachability of sensors in SuT"
request = OneM2MRequest("retrieve", to="onem2m/EDSOrch/testapplication/sensors")
promise = client.send_onem2m_request(request)
response = promise.get()

if response.response_status_code.http_status_code == 200:
    print "SuT sensors found"
else:
    print "SuT sensors not found"
    exit -1

print "testing reachability actuators in SuT"
request = OneM2MRequest("retrieve", to="onem2m")
promise = client.send_onem2m_request(request)
response = promise.get()

if response.response_status_code.http_status_code == 200:
    print "SuT actuators found"
else:
    print "SuT actuators not found"
    exit -1

