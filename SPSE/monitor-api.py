from pydbg import *
from pydbg.defines import *

def send_bp(dbg):
	print "Send() called!"
	print dbg.dump_context(dbg.context)
	
	return DBG_CONTINUE


dbg = pydbg()


for pid, name in dbg.enumerate_processes() :
	if name == 'vulnserver.exe':
		print "found"
		dbg.attach(pid)
		
send_api_addr = dbg.func_resolve("ws2_32","recv")
dbg.bp_set(send_api_addr,description="Send API breakpoint",handler=send_bp)
dbg.run()
