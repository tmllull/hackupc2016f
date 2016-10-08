
import serial
import time
import sys

if len(sys.argv) != 0:
  a = serial.Serial('/dev/ttyACM0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, None, False, False, None, False)
  time.sleep(1)
  print(sys.argv[1])
  a.write(sys.argv[1])
  a.close()
