from flask import Flask
import requests
app = Flask(__name__)


@app.route("/home/<num>")
def home(num):
    numb = int(num)
    if (numb % 2) == 0:
        numb = True
    else:
        numb = False
    return str(numb)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)