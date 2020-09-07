import time
import psutil
import platform
import math
from math import floor, log
from cpuWork import main

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


def test():
  prms = [i for i in genprimes(10**3)]

  cpuCases = []

  base = 1
  for prm in prms:
    try:
      base = floor(base * (10**5))  # Change increase per case here
      assert base <= 10**201

      if base % prm == 0:
        base += 1

      cpuCases.append([base, prm])
    except:
      break

  overallStart = time.time()

  tasksDone = 0
  totalTask = len(cpuCases)
  for case in cpuCases:
    main(case[0], case[1])
    tasksDone += 1
    print("\r{}/{} tasks done, {:.1%}".format(tasksDone,
                                              totalTask, tasksDone/totalTask), end="")

  overallEnd = time.time()
  overallDt = overallEnd - overallStart
  global sts
  sts = 4000/abs(log(overallDt))
  print()
  print("Single Thread Score: {:.1f}".format(sts))


if __name__ == "__main__":
  test()