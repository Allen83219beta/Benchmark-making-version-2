import singleThreadTest
import time
import sys
import os
import math
from math import log
import RAMTest
import System
import platform
import export


def main():
  
  System.main()

  print("Starting Single Thread Test")
  singleThreadTest.test()
  from singleThreadTest import sts
  print()
  time.sleep(5)

  print("Starting Multi Thread Test")
  import multiThreadTest
  multiThreadTest.test()
  from multiThreadTest import mts
  print()
  time.sleep(5)

  print('Starting Disk Test')
  import Disktest
  from Disktest import speed
  print()
  time.sleep(5)

  print('Starting RAM Test')
  RAMTest.main()
  from RAMTest import rtsc
  print()
  time.sleep(5)
  
  print('Starting GPU Test')
  import gputest
  gputest.main()
  from gputest import results
  print(results)
  
  global fullscore
  fullscore = (1.3*sts + 1.1*mts + 0.75*speed + 0.85*rtsc)
  print("Total Test Score:  ",end = "")
  print(fullscore)
  time.sleep(5)

  
  
  

  time.sleep(15)
  print("Test finished...")
  time.sleep(30)
  sys.exit(0)


if __name__ == "__main__":
  main()