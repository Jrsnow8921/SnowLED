import sys
import time
from ctypes import cdll
lib = cdll.LoadLibrary('./snowled.so')

class Led(object):
    
    def __init__(self):
        self.obj = lib.Led_new()

    def snowled(self):
        lib.Led_snowled(self.obj)

    def sleeper(self):
      num = float(1)
      time.sleep(num)

    def main(self):
      light = Led()
      light.snowled()

    def stop_running(self):
      try:
        sys.exit()
      except:
        print(sys.exc_info()[0])

if __name__=='__main__':
   Led().main()
