from flask import Flask, render_template
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


@app.route("/")
def idx():
    return render_template("meme.html", **meme.get())


app.run("0.0.0.0", port=8080, debug=True)



# def get_meme():
#     url = "https://meme-api.com/gimme"
#     response = json.loads(requests.request("GET", url).text)
#     meme_large = response["preview"][-2]
#     subreddit = response["subreddit"]
#     return meme_large, subreddit