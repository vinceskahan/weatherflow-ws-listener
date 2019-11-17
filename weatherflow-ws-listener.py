#!/usr/bin/env python
#
# this is a quickie WF websocket client mainly to test how it works
#

import json
import time
from websocket import create_connection

# ws endpoint and test key
uri = "ws://ws.weatherflow.com/swd/data?api_key=20c70eae-e62f-4d3b-b3a4-8586e90f3ac8"

# some messages we might send
#    TO DO: edit in your device and station id in below
Air_ListenStart    = '{ "type":"listen_start",        "device_id":12965,  "id": myId}'
Sky1_ListenStart   = '{ "type":"listen_start",        "device_id":12969,  "id": myId}'
Sky1_RapidStart    = '{ "type":"listen_rapid_start",  "device_id":12969,  "id": myId}'
Sky2_ListenStart   = '{ "type":"listen_start",        "device_id":29167,  "id": myId}'
Sky2_RapidStart    = '{ "type":"listen_rapid_start",  "device_id":29167,  "id": myId}'
Events_ListenStart = '{ "type":"listen_start_events", "station_id":29167, "id": myId}'

# try to have a unique id
timestamp=int(time.time() + 0.5)
myId = "random-id-" + str(timestamp)
print("randomId = '%s'" % myId)

print("------ create connection ------")
print("creating connection to '%s'" % uri)
ws = create_connection(uri)
result =  ws.recv()
print(result)

print()
print("------ sky1 listenStart ------------")
print("sending '%s'" % Sky1_ListenStart)
ws.send(Sky1_ListenStart)
result =  ws.recv()
print(result)

print()
print("------ sky1 rapidStart -------------")
print("sending '%s'" % Sky1_RapidStart)
ws.send(Sky1_RapidStart)
result =  ws.recv()
print(result)

print()
print("------ sky2 listenStart ------------")
print("sending '%s'" % Sky2_ListenStart)
ws.send(Sky2_ListenStart)
result =  ws.recv()
print(result)

print()
print("------ sky2 rapidStart -------------")
print("sending '%s'" % Sky2_RapidStart)
ws.send(Sky2_RapidStart)
result =  ws.recv()
print(result)

print()
print("------ air  listenStart ------------")
print("sending '%s'" % Air_ListenStart)
ws.send(Air_ListenStart)
result =  ws.recv()
print(result)

print()
print("------ events listenStart ----------")
print("sending '%s'" % Events_ListenStart)
ws.send(Events_ListenStart)
result =  ws.recv()
print(result)

# at this point we should be just listening....
print("\n entering loop\n")

while True:

    result =  ws.recv()

    # json object to pick the pieces out as needed
    r = json.loads(result)
    print(r['type'])
    print("   '%s'" % result)

    # a little whitespace for the poor human
    print()

    # sleep for a fraction of a second so we don't eat the cpu :-)    
    time.sleep(0.1)

# you don't reach here unless they disconnect us
ws.close()

