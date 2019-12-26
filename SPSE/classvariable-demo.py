#!/usr/bin/python

class mainClass:
	instanceCount = 0
	def __init__(self,ina):
		pass
	
	def printInstanceCount(self):
		mainClass.instanceCount +=1
		print "This is instance number: " + str(mainClass.instanceCount)

in1 = mainClass(2)
in1.printInstanceCount()
in2 = mainClass(3)
in2.printInstanceCount()
in3 = mainClass(4)
in3.printInstanceCount()
