# -*- coding: utf-8 -*-
import os
import web

from views.base import View
import json

class realtime(View):
	def GET(self):
		web.header('Content-Type', 'application/javascript')
		d = json.dumps({"address": "Shanghai", "tm": "00:00:00" })
		return 'some_func(' + d + ');'