#!/usr/bin/env python

import immlib

def main(args):
	imm = immlib.Debugger()
	
	#imm.openProcess('C:\Documents and Settings\MA LabMachine_1\Desktop\Vulnserver\\vulnserver\\vulnserver.exe')
	
	#imm.Attach(int(args[0]))
	
	td = imm.createTable("Module Information",['Name','Base','Entry','Size','Version'])
	
	moduleList = imm.getAllModules()
	
	for entity in moduleList.values():
		td.add(0, [entity.getName(),
		'%08X'%entity.getBaseAddress(),
		'%08X'%entity.getEntry(),
		'%08X'%entity.getSize(),
		entity.getVersion()
		])
		
		
	imm.log(str(imm.getRegs()))
	
	return "[+] Success!"
