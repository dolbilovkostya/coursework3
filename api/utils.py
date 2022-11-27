import json


def load_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def get_post_by_pk(pk):
    posts = load_posts()

    for post in posts:
        if post['pk'] == pk:
            return post

    return f'Такой пост не найден'
