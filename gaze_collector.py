# coding: utf-8

from psychopy import visual, core
from ctypes import *
import win32api
import datetime
import csv
import os


def waitEnterKey():
	while True:
		i = raw_input()
		if not i:
		    break


def cleanCSV(file, iniTime):
	o = open(file, 'r')
	data = o.read()

	data = data.replace("Gaze Data", "")
	data = data.replace("timestamp", "")
	data = data.replace("ms", "")
	data = data.replace("(", "")
	data = data.replace(")", "")
	data = data.replace(",", "")
	data = data.replace(":", "")
	data = data.replace("  ", " ")
	data = " ".join(data.split(";"))

	m = open(file, 'w')
	m.write(iniTime + "\n" + "x" + "y" + "timestamp(ms)" + "\n" + data)


def main():
	# Loading the DLL
	tobii_dll = CDLL("MinimalGazeDataStream.dll")

	identifier = raw_input("ID: ")
	iniTime = str(datetime.datetime.now())

	# Eye-data tracking
	tobii_dll.tobii_start(True) # True: show data-flow in terminal
	waitEnterKey()
	tobii_dll.tobii_stop()

	# Saving eye-data
	file = "gaze" + str(identifier) + ".csv"
	tobii_dll.tobii_save(file)
	cleanCSV(file, iniTime)

	# Releasing the DLL
	win32api.FreeLibrary(tobii_dll._handle)


if __name__ == '__main__':
    main()
