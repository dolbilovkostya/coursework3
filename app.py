from flask import Flask, request, render_template, send_from_directory
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id


POST_PATH = "data/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    post = get_posts_all()
    return render_template('index.html', items=post)


@app.route("/posts/<int:postid>")
def page_post(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', items=post, item__bottom=comments)


app.run(host='0.0.0.0', port=8000)
