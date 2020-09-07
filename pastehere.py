import time
import psutil
import platform
import GPUtil
from tabulate import tabulate
import AMD
import sys

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

  cpufreq = psutil.cpu_freq()
  print("CPU Info:")
  print("Physical cores:", psutil.cpu_count(logical=False))
  print("Total cores:", psutil.cpu_count(logical=True))
  print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
  print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
  print()
  time.sleep(5)

  print("Memory Information:")
  print("Virtual Memory")
  svmem = psutil.virtual_memory()
  print(f"Total: {sys.getsizeof(svmem.total)}")
  print(f"Available: {sys.getsizeof(svmem.available)}")
  print(f"Used: {sys.getsizeof(svmem.used)}")
  print()

  print("Swap Memory")
  swap = psutil.swap_memory()
  print(f"Total: {sys.getsizeof(swap.total)}")
  print(f"Free: {sys.getsizeof(swap.free)}")
  print(f"Used: {sys.getsizeof(swap.used)}")
  print(f"Percentage: {swap.percent}%")
  print()
  time.sleep(5)

  print("Disk Information:")
  partitions = psutil.disk_partitions()
  for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Total Size: {sys.getsizeof(partition_usage.total)}")
    print(f"  Used: {sys.getsizeof(partition_usage.used)}")
    print(f"  Free: {sys.getsizeof(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
    print()
  time.sleep(5)
  print("GPU Details:")
  print("Nvidia GPUs:")
  Ngpus = GPUtil.getGPUs()
  list_Ngpus = []
  for gpu in Ngpus:
    try:
      gpu_name = gpu.name
      gpu_load = f"{gpu.load*100}%"
      gpu_free_memory = f"{gpu.memoryFree}MB"
      gpu_used_memory = f"{gpu.memoryUsed}MB"
      gpu_total_memory = f"{gpu.memoryTotal}MB"
      gpu_temperature = f"{gpu.temperature} °C"
      gpu_uuid = gpu.uuid
      list_Ngpus.append((
         gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature, gpu_uuid
       ))
      print(tabulate(list_Ngpus, headers=("name", "load", "free memory", "used memory", "total memory", "temperature", "uuid")))
      print()
    except list_Ngpus == None:
      print("No GPU detected")
      print()
  print("AMD GPUs:")
  AMD.main()
  print()
  time.sleep(5)




def check_permission():
    euid = os.geteuid()
    if euid != 0:
        print('Script not started as root. Running sudo..')
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        os.execlpe('sudo', *args)

def sh(cmd, in_shell=False, get_str=True):
    output = subprocess.check_output(cmd, shell=in_shell)
    if get_str:
        return str(output, 'utf-8')
    return output

check_permission()