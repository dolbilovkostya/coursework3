from flask import Flask, request, render_template
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
import logging

POST_PATH = "data/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    post = get_posts_all()
    return render_template('index.html', item=post)


@app.route("/posts/<int:postid>")
def page_post(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', items=post, item__bottom=comments)


@app.route("/search/")
def search_page():
    search_query = request.args.get('s', '')
    posts = search_for_posts(search_query)
    return render_template('search.html', search__input=search_query, items=posts)


@app.route("/users/<username>")
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', items=posts)


@app.errorhandler(404)
def page_not_found(e):
    """
    в функцию `render_template()` передаем HTML-станицу с собственным
    дизайном, а так же явно устанавливаем статус 404
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    """
    в функцию `render_template()` передаем HTML-станицу с собственным
    дизайном, а так же явно устанавливаем статус 500
    """
    return render_template('500.html'), 500


@app.route("/api/posts")
def return_posts_by_json():
    """
    Возвращает список JSON-словаря со всеми постами
    :return: список со словарем
    """
    posts = get_posts_all()
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info('Запрос api/posts')
    return render_template('api_posts.html', items=posts)


@app.route("/api/posts/<int:postid>")
def return_post_by_json(postid):
    """
    Возвращает JSON-словарь с одним постом по заданному postid
    :param postid: Номер поста
    :return: JSON-словарь
    """
    post = get_post_by_pk(postid)
    path = f'api/posts/{postid}'
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info(f'Запрос {path}')

    return render_template('api_posts_post.html', items=post)


app.run(host='0.0.0.0', port=800)
