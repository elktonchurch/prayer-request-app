from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    user = request.form['user']
    typeOfRequest = request.form['typeOfRequest']
    prayerRequest = request.form['prayerRequest']
    # print(user, typeOfRequest, prayerRequest)
    if user == '' or typeOfRequest == '' or prayerRequest == '':
      return render_template('index.html', message='Please fill in all of the required fields, which are denoted by an " * " (asterisk)')
    return render_template('success.html')


if __name__ == '__main__':
  app.debug = True
  app.run()