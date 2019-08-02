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
	return template.render ()


	

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

		username_error = ""
		password1_error = ""
		password2_error = ""
		email_error = ""
		 
		if len (username) <3 or len (username)>20 or " " in username:
		 	 username_error= "must meet user name requirements"

		if password1 != password2:
			password2_error= "passwords must match"


		if len(password1) <3 or len(password1)>20 or " " in password1:
			password1_error= " Password must be between 3 and 20 characters long."

		
		
		
		if len(email) > 0:
			
			if len (email)<3 or len (email)>20 or " " in email or email.count("@") !=1 or email.count(".") !=1:
			
				email_error=" This is not a valid email."


		if username_error or email_error or password1_error or password2_error:

		
    
	  
	  			return template.render(email_error=email_error, username_error=username_error, password1_error=password1_error, password2_error=password2_error, name1=username, email1=email)
  

		else:
				return welcome.render(user=username, name1=username, email1 = email)


app.run()