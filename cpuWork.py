import random
import time
from math import floor
DEFAULT = object()


def i(x, y):
  last = 1
  iteration = 1

  while True:
    iterBeforeMod = min(x - iteration, floor((iteration - last) / abs(y)))

    if (iterBeforeMod > 1):  # Multi Tick
      last += abs(y) * iterBeforeMod
      iteration += iterBeforeMod

    if (iteration >= x):
      break

    last = (last + abs(y)) % (iteration+1)
    iteration += 1

  return last


def n(x, y):
  return max(1, i(x, y))


def main(x=DEFAULT, m=DEFAULT):
  if x is DEFAULT or isinstance(x, type(None)):
    x = 1
  if m is DEFAULT or isinstance(m, type(None)):
    m = random.randrange(-25, 25)

  if min(m, 0) == m:
    y = m-1
  else:
    y = m+1

  if x > 0:
    if y > 0:
      result = i(x, y)
      if result == 0:
        ret = x
      else:
        ret = result
    if y < 0:
     ret = n(x, y)

  return ret