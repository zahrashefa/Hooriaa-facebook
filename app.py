from flask import Flask, render_template , send_from_directory

app = Flask(__name__)

students=[{"name":"zahra", "age":20 , "city":"New York"}, {"name":"Hussain", "age":22 , "city":"New York"}]


@app.route("/")
def hello():
  return render_template('home.html' , st=students)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
