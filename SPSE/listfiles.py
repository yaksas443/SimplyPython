#!/usr/bin/env python

# Program to recursively list files and directories from a given path


import os
import sys

path =  sys.argv[1]

def lsfile(dir,path,level):
	dr = ''
	if level==0:
		print "-"*level + dir
		dr = dir
	else:
		dr = path+'/'+dir
	for item in os.listdir(dr):
		print "--" * (level+1) + " " + item
		if os.path.isdir(dr+'/'+item):
			lsfile(item,dr,level+1)

lsfile(path,path,0)
