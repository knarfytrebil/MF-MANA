# -*- coding: utf-8 -*-
import web
from lib.common import encrypt
from lib.common import decrypt

COOKIE_EXPIRE = 3600
COOKIE_DOMAIN = 'http://122.202.100.236/'

class Cookie:
	"""
	docstring for CookieSet
	read, write the cookie
	"""
	def __init__(self,user):
		self.u = user

	def GET(self):
		"""set cookie"""
		try:
			"getting cookie"
			uis = decrypt(web.cookies().uis).split(',')
			username = uis[0]
			password = uis[1]
			BAuth = self.BasicAuth(username,password)
			if BAuth:
				return BAuth
			return False
		except Exception,e:
			"if there is no cookie"
			return False
	def username(self):
		"""docstring for username"""
		return web.cookies().username
	
	def password(self):
		"""docstring for password"""
		return web.cookies().password
	
	def level(self):
		return web.cookies().level
	
	def SET(self,COOKIE_EXPIRE=COOKIE_EXPIRE,**kwargs):
		for key in kwargs.keys():
			web.setcookie(key,encrypt(kwargs[key]),COOKIE_EXPIRE)
	
	def BasicAuth(self,username,password):
		return self.u.BasicAuth(username,password)
	
	def Sina_Auth(self,uid,access_tolken):
		return self.u.SinaAuth(uid,access_tolken)