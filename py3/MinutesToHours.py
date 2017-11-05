#!/usr/bin/env python3
import os
import sys

def quit():
	os._exit(0)

v=0

try:
	if len(sys.argv) <2 :
		raise ValueError("ValueError: Input number cannot be negative")
	v=int(sys.argv[1])
	if v<0 :
		raise ValueError("ValueError: Input number cannot be negative")
except ValueError:
	print("ValueError: Input number cannot be negative")
	quit()

def hour(min):
	hour=int(min/60)
	min=min%60
	print("{} H, {} M".format(hour,min))
	return hour,min

hour(v)

