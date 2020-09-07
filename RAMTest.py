import time
import math
from math import log

def main():
  rts = time.time()
  for rep in range(10):
    test = []
    for i in range(10**7):
      test.append(0)
  rte = time.time()
  rdt = rte-rts
  print (rdt ,end='seconds')
  print()
  global rtsc
  rtsc = 4096/abs(log(rdt))
  print("RAM Test Score:" ,end = " ")
  print(rtsc)
if __name__ == "__main__":
	main()