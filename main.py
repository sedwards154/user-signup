from flask import Flask, request 

import cgi

import os

import jinja2



template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/")

def index():

	template = jinja_env.get_template('index.html')



	

@app.route("/create", methods= ["POST",'GET'])

def create():


	template = jinja_env.get_template('index.html')

	welcome = jinja_env.get_template('welcome.html')

	if request.method == 'POST': 
		verified = False

		var1 = 0

		var2 = 0

		template = jinja_env.get_template('index.html')

		welcome = jinja_env.get_template('welcome.html')

		username = request.form["username"]

		password1 = request.form["pas1"]

		password2 = request.form["pas2"]

		email = request.form["email"]

		if len(email) > 0:

			for char in email:

				if char=="@":

					var1+=1

				if char==".":

					var2+=1

				if var1==1 and var2 >=1:

					verified = True

				else:

					verified = False

		else:

			verified = True

		if verified == False:

			return template.render(email1=" This is not a valid email.", name1=username)

		elif verified == True:

			if password1 != password2:

				return template.render(pass2=" Passwords do not match!", name1=username, email1 = email)

			elif password1 == password2:

				if len(password1) >= 3 and len(password1) <=20 and not (' ' in password1):

					if not (' ' in username) and  (len (username) > 3) and (len (username) < 20):

						return welcome.render(user=username, name1=username, email1 = email)

					else:

						return template.render(name1=" Must have a username", email1 = email)

				else:

					return template.render(pass2=" Password must be between 3 and 20 characters long.", name1=username, email1 = email)

	else:
		return template.render()

app.run()