import time
import sys
import os
import math
import platform
from singleThreadTest import sts
from multiprocessing import Pool
from math import floor, log, abs
from cpuWork import main


tasksDone = 0
totalTask = 0


def _getThreads():
    """ Returns the number of available threads on a posix/win based system """
    if sys.platform == 'win32':
        return (int)(os.environ['NUMBER_OF_PROCESSORS'])
    else:
        return (int)(os.popen('grep -c cores /proc/cpuinfo').read())


def genprimes(limit):  # derived from
  # Code by David Eppstein, UC Irvine, 28 Feb 2002
  D = {}            # http://code.activestate.com/recipes/117119/
  q = 2

  while q <= limit:
    if q not in D:
      yield q
      D[q * q] = [q]
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]
    q += 1


def taskDone(result):
  global tasksDone, totalTask
  tasksDone += 1
  print("\r{}/{} tasks done, {:.1%}".format(tasksDone,
                                            totalTask, tasksDone/totalTask), end="")


def test():

  prms = [i for i in genprimes(10**4)]

  cpuCases = []

  base = 1
  for prm in prms:
    try:
      base = floor(base * 10)  # Change increase per case here
      assert base <= 10**201

      if base % prm == 0:
        base += 1

      cpuCases.append([base, prm])
    except:
      break

  global totalTask
  totalTask = len(cpuCases)

  overallStartm = time.time()

  with Pool(_getThreads()) as p:
    for task in cpuCases:
      p.apply_async(main, task, callback=taskDone)
    p.close()
    p.join()

  overallEndm = time.time()
  overallDtm = overallEndm - overallStartm
  global mts
  mts = (0.8*abs(1/log(overallDtm))*int((pow(5,0.5)+1)*8000))+0.2*sts
  print()
  print("Multi Thread Score: {:.1f}".format(mts))


if __name__ == "__main__":
  test()
