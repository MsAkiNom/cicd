from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/ping")
def pong():
    return "Pong"

if __name__ == "__main__":
    app.run(debug=True)