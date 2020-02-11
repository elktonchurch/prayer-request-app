from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
else:
  app.debug = False
  app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
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
    return render_template('success.html')


if __name__ == '__main__':
  app.run()