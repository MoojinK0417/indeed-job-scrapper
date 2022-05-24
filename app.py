from flask import Flask, render_template, request, request_started

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("index.html")


@app.route("/<username>")
def potato(username):
  return f"Hello your name is {username}"


@app.route("/report")
def report():
  word = request.args.get('word')
  
  return render_template("report.html", searchingBy=word)


app.run(host="127.0.0.1:5000")