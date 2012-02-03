import os
import sys
import web

curdir = os.path.dirname(__file__)
sys.path.append(curdir)

from views.index import index
from views.user import user

web.config.debug = True

urls = (
	'/','index',
	'/user/(.*)','user'
)

application = web.application(urls, globals()).wsgifunc()