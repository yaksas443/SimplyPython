#!/usr/bin/env python

import os

def child_process():
	print "I am the child process and my PID is: %d" %os.getpid()
	print "The child is exiting"

def parent_process():
	print "I am the parent process with PID: %d"%os.getpid()

	childpid = os.fork()
	if childpid == 0:
		# we are inside child
		child_process()
	else:
		# we are inside the parent process
		print "We are inside the parent process\n"
		print "Our child has PID: %d"%childpid 
	while True:
		pass

parent_process()
