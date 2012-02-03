# -*- coding: utf-8 -*-
from web import form

def DropDown(confstr,name):
	li = []
	for i in confstr.split(','):
		a = i.split('-')
		li.append((a[0],a[1]))
	return form.Dropdown(name,args=li)

def Login():
	"""
	Generates Login Form
	"""
	vusername = form.regexp(r".{3,50}$", 'must be between 3 and 20 characters')
	#validator of the username
	
	login = form.Form(
		form.Textbox(
			'username',vusername,
			description="USERNAME"
		),
		form.Password(
			'password',
			description="PASSWORD"
		),
		validators = [
		form.Validator(
			"Username and Password can't be the same",
			lambda i: i.username != i.password
			)
		]
	)
	return login