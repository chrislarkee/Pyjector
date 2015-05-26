# Pyjector
Limited emulation of a Christie DLP projector's TIPM serial interface, written in Python. Helpful if you're working on an application to control projectors.

Supported commands:
- Ping (PNG?)
- Shutter query (SHU?)
- Shutter open (SHU0)
- Shutter close (SHU1)
- Lamp status query (PWR?)
- Lamp on (PWR1)
- Lamp off (PWR0)
