# Copyright (C) 2017 by Gergo Szabo <szager88@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from __future__ import print_function
import os, sys
from optparse import OptionParser
from pyadl import *

def main():
   devices = ADLManager.getInstance().getDevices()
   for device in devices:
     try:
      print("{0}. {1}".format(device.adapterIndex, device.adapterName))
      if devices is not None:
         try:
           print ("\tTemperature: {0} Celsius".format(device.getCurrentTemperature()))
         except ADLError as err:
           print("Can't get temperature.")
         try:
           print ("\tUsage: {0} %".format(device.getCurrentUsage()))
         except ADLError as err:
           print("Can't get usage.")
         try:
           coreVoltageMin, coreVoltageMax = device.getCoreVoltageRange()
           print ("\tEngine core voltage: {0} mV ({1} mV - {2} mV)".format(device.getCurrentCoreVoltage(), coreVoltageMin, coreVoltageMax))
         except ADLError as err:
           print("Can't get voltage range.")
         try:
           coreFrequencyMin, coreFrequencyMax = device.getEngineClockRange()
           print ("\tEngine clock: {0} MHz ({1} MHz - {2} MHz)".format(device.getCurrentEngineClock(), coreFrequencyMin, coreFrequencyMax))
         except ADLError as err:
           print("Can't get core frequency range.")
         try:
           memoryFrequencyMin, memoryFrequencyMax = device.getMemoryClockRange()
           print ("\tMemory clock: {0} MHz ({1} MHz - {2} MHz)".format(device.getCurrentMemoryClock(), memoryFrequencyMin, memoryFrequencyMax))
         except ADLError as err:
           print("Can't get memory frequency range.")
         try:
           fanSpeedPercentageMin, fanSpeedPercentageMax = device.getFanSpeedRange(ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE)
           print ("\tFan speed: {0} % ({1} % - {2} %)".format(device.getCurrentFanSpeed(ADL_DEVICE_FAN_SPEED_TYPE_PERCENTAGE), fanSpeedPercentageMin, fanSpeedPercentageMax))
         except ADLError as err:
           print("Can't get fan speed percentage range.")
         try:
           print ("\tFan speed: {0} RPM ({1} RPM - {2} RPM)".format(device.getCurrentFanSpeed(ADL_DEVICE_FAN_SPEED_TYPE_RPM), fanSpeedRPMMin, fanSpeedRPMMax))
         except ADLError as err:
           print("Can't get fan speed.")
     except ADLError as err:
       print("Can't get AMD GPU")