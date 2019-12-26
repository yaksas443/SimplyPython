#!/usr/bin/env python

import signal

def ctrlc_handler(signum,frm):
	print "Ha ha! You cannot kill me"


print "Installing signal handler..."
signal.signal(signal.SIGINT, ctrlc_handler)
signal.signal(signal.SIGKILL, ctrlc_handler)
print "Done!"

while True:
	pass


