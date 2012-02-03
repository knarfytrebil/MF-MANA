#!/usr/bin/env python
# encoding: utf-8
"""
User.py

Created by 姚 远 on 2011-12-27.
Copyright (c) 2011 ManaFlame. All rights reserved.
"""
from modules.base import Base

class User(Base):
	"""docstring for Settings"""
	def BasicAuth(self,username,password):
		try:
			ui = self.sdb.where(self.table,name=username)[0]
		except:
			return 0
		if password == ui.password:
			import datetime
			now = datetime.datetime.now()
			w = "WHERE name='%s'" % username
			self.sdb.update(self.table,where=w,date_login=now)
			return ui
		else:
			return 0