from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/home/prime_checker")
def home(num):
    v = 1
    return str(False) if int(num) % 2 else str(True)


@app.route("/form")
def form():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)