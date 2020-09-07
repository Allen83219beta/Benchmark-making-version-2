import time
import psutil
import platform
import cpuinfo
import AMD
import sys
import os
import shutil
import Ngpus

def main():
  print("System Information:")
  uname = platform.uname()
  print(f"System: {uname.system}")
  print(f"Node Name: {uname.node}")
  print(f"Release: {uname.release}")
  print(f"Version: {uname.version}")
  print(f"Machine: {uname.machine}")
  print(f"Processor: {uname.processor}")
  print()
  time.sleep(5)

  print("CPU Info:")
  info = cpuinfo.get_cpu_info()
  HzM = info['hz_advertised_friendly']
  Vendor = info['vendor_id_raw']
  CPU = info['brand_raw']
  print(Vendor)
  print(CPU)
  print(HzM)
  print()
  time.sleep(5)

  print("RAM Information(GB):")
  mem = psutil.virtual_memory()
  RAM = float(mem.total/(2**30))
  print(RAM, "GB")
  print()
  time.sleep(5)

  print("Disk Information(GB):")
  total, used, free = shutil.disk_usage("/")
  print("Total: %d GB" % (total / (2**30)))
  print("Used: %d GB" % (used / (2**30)))
  print("Free: %d GB" % (free / (2**30)))
  print()
  time.sleep(5)
  
  print("GPU Details:")
  print("NVidia GPUs:")
  Ngpus.main()
  
  print("AMD GPUs:")
  AMD.main()
  print()
  time.sleep(5)

if __name__ == "__main__":
  main()