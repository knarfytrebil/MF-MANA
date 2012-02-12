# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.spider import Crawler

class analyze(View):
	def GET(self):
		c = Crawler('117.102.189.222')
		location = c.location(str(self._ip()))
		ua = self._useragent()
		return location,ua