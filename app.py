import os
from flask import Flask, render_template, request
# from flask_talisman import Talisman
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
HEROKU_DATABASE_URI = os.environ.get('HEROKU_DATABASE_URI')

app = Flask(__name__)
# Talisman(app)
CORS(app)

ENV = 'dev'

if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = HEROKU_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PrayerRequest(db.Model):
	__tablename__ = 'prayerRequest'
	id = db.Column(db.Integer, primary_key=True)
	userFirstName = db.Column(db.String(200))
	userLastName = db.Column(db.String(200))
	typeOfRequest = db.Column(db.String(200))
	prayerRequest = db.Column(db.Text())

	def __init__(self, userFirstName, userLastName, typeOfRequest, prayerRequest):
		self.userFirstName = userFirstName
		self.userLastName = userLastName
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
		userFirstName = request.form['userFirstName']
		userLastName = request.form['userLastName']
		typeOfRequest = request.form['typeOfRequest']
		prayerRequest = request.form['prayerRequest']
	if userFirstName == '' or userLastName == '' or typeOfRequest == '' or prayerRequest == '':
		return render_template('index.html', message='Please fill in ALL the fields & resubmit your form again')
	# Prevents duplicate prayer request form submissions from the same user 
	# if db.session.query(PrayerRequest).filter(PrayerRequest.user == user).count() == 0:
	data = PrayerRequest(userFirstName, userLastName, typeOfRequest, prayerRequest)
	db.session.add(data)
	db.session.commit()
	send_mail(userFirstName, userLastName, typeOfRequest, prayerRequest)
	return render_template('success.html')
	# Renders home page; displays message stating that this user has already submitted
	# return render_template('index.html', message='Thank you, but you have already submitted a prayer request')

if __name__ == '__main__':
    app.run(debug=True)