# -*- coding: utf-8 -*-
import os
import web

from views.base import View


class analyze(view):
	def GET(self):
		ip = self._ip()
		ua = self._useragent()
		return ip,ua