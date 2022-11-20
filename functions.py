import json


def load_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        post = json.load(file)
        print(post)

load_posts()