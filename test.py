from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return "hello world flask"

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=8080, debug=False)