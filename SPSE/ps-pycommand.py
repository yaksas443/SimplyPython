#!/usr/bin/env python

import immlib

DESC = 'Sample SPSE Demo Pycommand'

def main(args):
	imm = immlib.Debugger()
	imm.log("Writting to my Log Window")
	
	td = imm.createTable("SPSE Demo",['PID','Name','Path','Services'])
	psList = imm.ps()
	for process in psList:
		td.add(0,[str(process[0]),process[1],process[2],str(process[3])])
	
	return "[+] Success"
