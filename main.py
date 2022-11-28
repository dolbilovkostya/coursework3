from flask import Flask, request, render_template, redirect
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
import json
from api.api import api_blueprint

POST_PATH = "data/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api_blueprint)


@app.route("/")
def page_index():
    """
    Представление главной страницы
    :return: Список постов
    """
    post = get_posts_all()

    """
    Передаю в шаблон список с закладками и вывожу в счетчике закладок длину этого списка
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    return render_template('index.html', item=post, header__wrapper=bookmarks)


@app.route("/posts/<int:postid>")
def page_post(postid):
    """
    Представление страницы поста по его номеру
    :param postid: Номер поста
    :return: Пост пользователя
    """
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', items=post, item__bottom=comments)


@app.route("/search/")
def search_page():
    """
    Представление поиска
    :return: Список постов по заданному поиску
    """
    search_query = request.args.get('s', '')
    posts = search_for_posts(search_query)
    return render_template('search.html', search__input=search_query, items=posts)


@app.route("/users/<username>")
def user_page(username):
    """
    Представление стрницы пользователя
    :param username: Номер пользователя
    :return: Список постов пользователя
    """

    posts = get_posts_by_user(username)
    return render_template('user-feed.html', items=posts, username=username)


@app.route("/bookmarks/add/<int:postid>", methods=['GET', 'POST'])
def add_to_bookmarks(postid):
    """
    Добавление поста в закладки
    :param postid: Номер поста
    :return: После довабления поста возвращает на главную страницу
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    post = get_post_by_pk(postid)
    posts_in_bookmarks = []

    """
    Проходим по списку закладок и добавляем все номера постов
    """
    for item in bookmarks:
        posts_in_bookmarks.append(int(item['pk']))

    """
    Если пост с таким postid уже есть в закладках, то он не добавится в список закладок
    """
    if postid not in posts_in_bookmarks:
        bookmarks.append(post)

    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file)

    return redirect("/", code=302)


@app.route("/bookmarks/remove/<int:postid>", methods=['GET', 'POST'])
def remove_to_bookmarks(postid):
    """
    Удаление поста из закладок
    :param postid: Номер поста
    :return: После удаления поста возвращает на главную страницу
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    for post in bookmarks:
        if postid == post['pk']:
            bookmarks.remove(post)

    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file)

    return redirect("/", code=302)


@app.route("/bookmarks", methods=['GET'])
def bookmarks_page():
    """
    Представление страницы с закладками
    :return: Страница с закладками
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    return render_template('bookmarks.html', items=bookmarks)


@app.route("/tag/<tagname>")
def tag_page(tagname):
    """
    Представление страницы поиска по хэштегу
    :param tagname: Хэштег
    :return: Список постов содержащих хэштег
    """
    posts = get_posts_all()
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


app.run(host='0.0.0.0', port=800)
