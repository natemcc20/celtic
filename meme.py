from flask import Flask, render_template, send_from_directory, url_for
import json
import requests

app = Flask(__name__)


class Meme:

    def __init__(self):
        self.s = requests.Session()
        self.url = "https://meme-api.com/gimme"

    def get(self):
        response = json.loads(self.s.request("GET", self.url).text)
        return {
            "meme_pic": response["preview"][-2],
            "subreddit": response["subreddit"]
        }


meme = Meme()


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='images/favicon-32x32.png')


# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))

@app.route("/")
def idx():
    return render_template("meme.html", **meme.get())


@app.route("/likes")
def likes():
    return render_template('likes.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)



# def get_meme():
#     url = "https://meme-api.com/gimme"
#     response = json.loads(requests.request("GET", url).text)
#     meme_large = response["preview"][-2]
#     subreddit = response["subreddit"]
#     return meme_large, subreddit
#     <a href=”/your_flask_funtion”><input type=”button” value=”call_flask_funtion”></a>
