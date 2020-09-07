import GPUtil
from tabulate import tabulate

def main():
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
         gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature
       ))
      print(tabulate(list_Ngpus, headers=("name", "load", "free memory", "used memory", "total memory", "temperature", "uuid")))
      print()
    except list_Ngpus is None:
      print("No NVidia GPU detected")
      print()