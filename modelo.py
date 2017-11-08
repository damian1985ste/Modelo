#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('churrinche.db')
c = conn.cursor()

class modelo:
	def __init__(self):
		self.cfg=config()


class config:
	#wifi = False
	#bt = False	
	def __init__(self):
		c.execute("UPDATE T_Config SET Valor='False' WHERE Nombre='wifi'")
		self.wifi = False
		c.execute("UPDATE T_Config SET Valor='False' WHERE Nombre='bt'")
		self.bt = False
		# Save (commit) the changes
		conn.commit()
	
	def setWifi(self,estado):
		if estado:
			c.execute("UPDATE T_Config SET Valor='True' WHERE Nombre='wifi'")
			self.wifi = True
			conn.commit()
		elif not estado:
			c.execute("UPDATE T_Config SET Valor='False' WHERE Nombre='wifi'")
			self.wifi = False
			conn.commit()
	
	def setBt(self,estado):
		if estado:
			c.execute("UPDATE T_Config SET Valor='True' WHERE Nombre='bt'")
			self.bt = True
			conn.commit()
		elif not estado:
			c.execute("UPDATE T_Config SET Valor='False' WHERE Nombre='bt'")
			self.bt = False
			conn.commit()