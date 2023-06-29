from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Banglore,India',
  'Salary': 'RS.15,00,000',
  'Company': 'Wipro'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Hyderabad,India',
  'Salary': 'RS.20,00,000',
  'Company': 'Cisco'
}, {
  'id': 3,
  'title': 'Front End',
  'location': 'Pune,India',
  'Salary': 'RS.10,00,000',
  'Company': 'TCS'
}, {
  'id': 4,
  'title': 'Back end',
  'location': 'Chennai,India',
  'Salary': 'RS.12,00,000',
  'Company': 'Cognizant'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
