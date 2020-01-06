#!/usr/bin/env python

from pydbg import *
from pydbg.defines import *
import sys


def detect_overflow(dbg):
	
	if dbg.dbg.u.Exception.dwFirstChange:
		return DBG_EXCEPTION_NOT_HANDLED
		
	print "Access Violation Happened"

dbg = pydbg()
dbg.attach(int(sys.argv[1]))

dbg.set_callback(EXCEPTION_ACCESS_VIOLATION,detect_overflow)
dbg.run()
