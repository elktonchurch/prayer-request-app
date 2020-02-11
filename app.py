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
    if user == '' or typeOfRequest == '':
      return render_template('index.html', message='Please enter info into the required fields')
    return render_template('success.html')


if __name__ == '__main__':
  app.debug = True
  app.run()