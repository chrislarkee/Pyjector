#!/usr/bin/python

import time
from Projector import Projector


projector1 = Projector(1, "USRP-1", "172.16.20.101")
projector2 = Projector(2, "USRP-2", "172.16.20.102")
projector3 = Projector(3, "NewFakeProjector", "192.168.2.201")




while True:
  projector3.info()
  time.sleep(1.5)
  projector3.ping()
  time.sleep(1)
  projector3.hasBrain()
  time.sleep(1)
  projector3.lamp()
  time.sleep(1)
  projector3.shutter()