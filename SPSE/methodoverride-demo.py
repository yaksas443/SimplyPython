#!/usr/bin/python

class parent:
	def __init__(self,ina):
		self.a = ina

	def printA(self):
		print str(self.a)


class child(parent):
	def printA(self):
		print str(self.a+1)


p = parent(5)
p.printA()
c = child(5)	
c.printA()
