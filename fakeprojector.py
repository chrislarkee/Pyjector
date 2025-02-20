#!/usr/bin/python

# fakeprojector.py
#
# Pretends to be a Christie Roadster projector, emulating selected behaviors for the purposes of testing the ASCII query/reponse and messaging system

import socket
import sys

lampState = 0      # 0 = off, 1 = on
shutterState = 0   # 0 =  open, 1 = closed
signalState = 0    # 0 = none/bad, 1 = good

lampOnResponse = "(PWR! 001)"
lampOffResponse = "(PWR! 000)"
shutterOpenResponse = "(SHU! 000)"
shutterClosedResponse = "(SHU! 001)"
signalGoodResponse = "(signal good?)"
signalBadResponse = "(signal bad? )"

host = ''       # Will default to the IP of the system it is running on
port = 3002     # Christie default is 3002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

try:
  conn, addr = s.accept()
  print("Connection from " + str(addr))

  while True:
    data = conn.recv(1024).decode()
    if not data: break
    print(data)
    if "PNG?" in data:
        print("Ping received.")
        conn.send("(PNG! 031 001 000)")
    elif "PWR?" in data:
        print("Query received - lamp status.")
        if lampState == 1:
            conn.send(lampOnResponse.encode())
            print("Lamp is on.")
        if lampState == 0:
            conn.send(lampOffResponse.encode())
            print("Lamp is off")
    elif "PWR1" in data:
        print("Command received - lamp on.")
        lampState = 1
    elif "PWR0" in data:
        print("Command received - lamp off.")
        lampState = 0
    elif "SHU?" in data:
        print("Query received - shutter status.")
        if shutterState == 0:
            conn.send(shutterOpenResponse.encode())
            print("Shutter is open.")
        if shutterState == 1:
            conn.send(shutterClosedResponse.encode())
            print("Shutter is closed.")

    elif "SHU0" in data:
         shutterState = 0
         print("Command received - shutter open.")
    elif "SHU1" in data:
         shutterState = 1
         print("Command received - shutter close.")

except KeyboardInterrupt:
  conn.close()
  sys.exit()
