from flask import Flask, request, render_template, send_from_directory
from functions import load_posts


POST_PATH = "data/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    post = load_posts()
    return render_template('index.html', item=post)


app.run()
