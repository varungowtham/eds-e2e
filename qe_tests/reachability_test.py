#!/usr/bin/env python2

from openmtc_onem2m.model import AE, Container, ContentInstance
from openmtc_onem2m.client.http import OneM2MHTTPClient
from openmtc_onem2m.transport import OneM2MRequest


client = OneM2MHTTPClient("http://eds-base:8000", False)
applications = []

verdict = True
# check reachability of the gateway
onem2m_request = OneM2MRequest("retrieve", to="onem2m/EDSOrch")
promise = client.send_onem2m_request(onem2m_request)
onem2m_response = promise.get()

if onem2m_response.response_status_code.http_status_code  == 200:
  print "EDSOrch path found"
else:
  print "EDSOrch path not found"
  verdict = False

print "scanning AEs"

children = onem2m_response.content.childResource
base_path = "onem2m/EDSOrch"
for child in children:
  print "Found AE: " + child.path
  if "testapplication" in child.path:
    applications.append(child.path)
    print "Scanning internal sensor path"
    sensor_path = base_path + "/" + child.path + "/" + "sensors"
    onem2m_request = OneM2MRequest("retrieve", to=sensor_path)
    promise = client.send_onem2m_request(onem2m_request)
    onem2m_response = promise.get()
    sensor = onem2m_response.content.childResource
    print "    found sensor: " + sensor[0].path

    print "Scanning internal actuator path"
    actuator_path = base_path + "/" + child.path + "/" + "actuators"
    onem2m_request = OneM2MRequest("retrieve", to=actuator_path)
    promise = client.send_onem2m_request(onem2m_request)
    onem2m_response = promise.get()
    actuator = onem2m_response.content.childResource
    print "    found actuator: " + actuator[0].path


