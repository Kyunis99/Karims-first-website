from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"


if__name__ == "__main__":
    app.run()
