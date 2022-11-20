from flask import Flask, request, render_template, send_from_directory
from utils import get_posts_all


POST_PATH = "data/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    post = get_posts_all()
    return render_template('index.html', items=post)


app.run(host='0.0.0.0', port=8000)
