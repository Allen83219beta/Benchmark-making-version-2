import platform
import cpuinfo
import GPUtil
import psutil
import shutil
from pyadl import *
from __future__ import print_function
import os, sys
from optparse import OptionParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials

Ngpus = GPUtil.getGPUs()
list_Ngpus = []
for gpu in Ngpus:
  try:
    gpu_name = gpu.name
  except list_Ngpus == None:
    gpu_name = str("No Nvidia GPU detected")

devices = ADLManager.getInstance().getDevices()
for device in devices:
  try:
    agpus = device.adapterName
  except ADLError as err:
    agpus =  str("Can't detect AMD GPU")


uname = platform.uname()

CPU = info['brand_raw']

auth_json_path = 'Computer Scores.json'

mem = psutil.virtual_memory()
RAM = float(mem.total/(2**30))
total, used, free = shutil.disk_usage("/")
def main():
  from Disktest import speed
  from RAMTest import rtsc
  from singleThreadTest import sts
  from multiThreadTest import mts
  from fullTest import fullscore

  credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
  gss_client = gspread.authorize(credentials)
  spreadsheet_key = "2PACX-1vTkFY9dkanWcWwsv614X7ONJ5TSZqxQ7AP7d-AIQeT56wnkIb13X8Tv-X6D_0LXm3nCVwym3yDBYFUv"
  insert_row()
  values = [uname.system , CPU , gpu_name , agpus , RAM , (total / (2**30)) , sts , mts , rtsc , speed , fullscore]
  sheet.insert_row(values, )