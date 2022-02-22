from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "madfajlf"

@app.route("/")
def index():
    return "This is a <h1>Home page!</h1>"

@app.route("/<name>")
def hname(name):
	return f"Hello {name}"

@app.route("/hello")
def iindex():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", it's great to see you!")
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)