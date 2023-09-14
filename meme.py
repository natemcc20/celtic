from flask import Flask, render_template, send_from_directory, url_for, request, session
import json
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

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


# for addidng the liked images to our session
@app.route("/like_image", methods=['POST'])
def like_images():
    image_url = request.form.get('url')
    session['url'] = image_url
    return 'Image stored in session'


@app.route("/likes")
def likes():
    return render_template("likes.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)

