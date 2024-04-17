from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id":1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "Salary": "Rs. 10,00,000"
  },
  {
    "id":2,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "Salary": "Rs. 10,00,000"
  },
  {
    "id":3,
    "title": "Data Analyst",
    "location": "Bengaluru, India"
  },
  {
    "id":4,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "Salary": "Rs. 10,00,000"
  },
]

@app.route('/api/jobs')
def lis_jobs():
  return jsonify(JOBS)

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  