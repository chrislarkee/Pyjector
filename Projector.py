#!/usr/bin/python

import os
import sys
import time
import socket

class Projector:
  'projectors!'

  def __init__(self, id, label, ipAddress):
    self.id = id
    self.label = label
    self.ipAddress = ipAddress

  def info(self):
    print("ID: Projector" , self.id, '\n', "Label:", self.label, '\n', "IP Address:", self.ipAddress)

  def test(self):
    print("Test of Projector class seems to work.")

  def ping(self):
    print("Pinging", self.label, "(" + self.ipAddress + ")","...")
    global pingResult
    pingResult = os.system("ping -c 5 -i 1 -t 3 " + self.ipAddress + " > /dev/null 2>&1")
    if pingResult == 0:
      print("Projector", self.label, "is up.")
    else:
      print("Projector", self.label, "ping failed.")
    return pingResult

  def hasBrain(self):
    global brain # indicates that the projector's brain is working, not just that the network interface is up
    self.ping()
    if pingResult == 0:
      print("Ping was good, let's try to connect...")
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      host = self.ipAddress
      port = 3002
      print("connecting to " + self.label + " on port " + str(port))
      try :
        s.connect((host, port))
      except Exception as e:
        print(('something\'s wrong with %s:%d. Exception type is %s' % (host, port, repr(e))))
      s.send("(PNG?)".encode())
      data = s.recv(1024).decode()
      if data == "(PNG! 031 001 000)":
        brain = 1
      else:
        brain = 0
      #s.close()
      print(data)


      brain = 1 # if connect is successful, and query (PNG?) returns something useful
    else:
      print("Braindead!")
      brain = 0
    return brain


  def lamp(self):
    global lamp
    if brain == 1:
      print("Has a brain, how's the lamp?")

      lamp = 1 # if (PWR?) query returns (PWR! 001) or whatever
    else:
      print("Braindead, so not checking lamp.")
      lamp = 0
    return lamp

  def shutter(self):
    global shutter
    if brain == 1 and lamp == 1:
      print("Has a brain, how's the shutter?")
      shutter = 1 # if (SHU?) query returns (SHU! 001)
    else:
      print("Braindead, so can't check shutter and STOP ASKING.")
      shutter = 0
    return shutter

  def signal(self):
    global signal
    if brain == 1:
      print("Has a brain, how's the signal?")
      signal = 1 # find way to check signal status. There's an FYI message? An SST query?
    else:
      print("Braindead, so can't check signal.")
      signal = 0
    return signal
