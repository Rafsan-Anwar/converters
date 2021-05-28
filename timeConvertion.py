

import sys

para1 = sys.argv[1]
inp = float(sys.argv[2])
para2 = sys.argv[3]

"""
		Welcome to python time Conversion Tool
		Developbed by Rafsan Anwar

		Parameters :
		-h : Hours
		-m : Minuts
		-s : Seconds

		--help : tool description
		Example:
			for 1 hour => seconds
			python timeConvertion.py -h 1 -s  [windows]
			./timeConvertion.py -h 1 -s  [linux]
"""

if para1 == "-h" and para2 == "-s":
	res = inp * 3600
	text = "Seconds: "+ str(res)
	print(text)

if para1 == "-m" and para2 == "-s":
	res = inp * 60
	text = "Seconds: "+ str(res)
	print(text)

if para1 == "-s" and para2 == "-m":
	res = inp / 60
	text = "Minutes: "+str(res)
	print(text)

if para1 == "-h" and para2 == "-m":
	res = inp * 60
	text = "Minutes: "+ str(res)
	print(text)

if para1 == "-s" and para2 == "-h":
	res = inp * 3600
	text = "Hours: "+ str(res)
	print(text)

if para1 == "-m" and para2 == "-h":
	res = inp / 60
	text = "Hours: "+ str(res)
	print(text)