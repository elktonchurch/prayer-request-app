import os
from flask import Flask, render_template, request
# from flask_talisman import Talisman
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
DATABASE_URL = os.environ.get('DATABASE_URL')

app = Flask(__name__)
# Talisman(app)
CORS(app)

ENV = 'prod'

if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PrayerRequest(db.Model):
	__tablename__ = 'prayerRequest'
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(200))
	typeOfRequest = db.Column(db.String(200))
	prayerRequest = db.Column(db.Text())
  
	def __init__(self, user, typeOfRequest, prayerRequest):
		self.user = user
		self.typeOfRequest = typeOfRequest
		self.prayerRequest = prayerRequest
	
  
# Route that handles GET requests to the '/' endpoint
@app.route('/')
def index():
	return render_template('index.html')

# Route that handles POST requests to the '/submit' endpoint
@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		user = request.form['user']
		typeOfRequest = request.form['typeOfRequest']
		prayerRequest = request.form['prayerRequest']
	if user == '' or typeOfRequest == '' or prayerRequest == '':
		return render_template('index.html', message='Please fill in all of the required fields, which are denoted by an " * " (asterisk)')
	# Prevents duplicate prayer request form submissions from the same user 
	# if db.session.query(PrayerRequest).filter(PrayerRequest.user == user).count() == 0:
	data = PrayerRequest(user, typeOfRequest, prayerRequest)
	db.session.add(data)
	db.session.commit()
	send_mail(user, typeOfRequest, prayerRequest)
	return render_template('success.html')
	# Renders home page; displays message stating that this user has already submitted
	# return render_template('index.html', message='Thank you, but you have already submitted a prayer request')

if __name__ == '__main__':
    app.run()