# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.spider import Crawler
from lib.AnaCookie import Cookie

html = """
<html>
<script type="text/javascript">
window.onbeforeunload = function(){
return "必优博客提示您，您确定要退出页面吗？";
}
</script>
<html>
"""

class analyze(View):
	def GET(self):
		c = Crawler('117.102.189.222')
		ip = str(self._ip())
		location = c.location(ip)
		ua = self._useragent()
		cookie = Cookie(ua,ip)
		came = cookie.GET()
		if came:
			pass
		else:
			cis = ua+ip
			cookie.SET(cis=cis)
		return html
		
	def POST(self):
		pass