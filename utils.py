import json


def get_posts_all():
    """
    Возвращает посты в формате словаря
    :return: посты в формате списка со вложенными словарями -> list[dict]
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя. Функция должна вызывать ошибку
    ValueError если такого пользователя нет и пустой список, если у пользователя нет постов.
    :param user_name: имя польщователя
    :return: посты определенного пользователя -> list[dict]
    """
    user_posts = []
    try:
        for post in get_posts_all():
            if user_name.lower() == post['poster_name'].lower():
                user_posts.append(post)
        return user_posts
    except ValueError:
        print("Такого пользователя нет")
    except user_posts == []:
        return user_posts



def get_comments_by_post_id(post_pk):
    """
    возвращает комментарии определенного поста. Функция должна вызывать ошибку ValueError если такого поста нет
    и пустой список, если у поста нет комментов.
    :param post_id: id поста
    :return: комментарии определенного поста -> list[dict]
    """
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
        comments_list = []
        try:
            for comment in comments:
                if post_pk == int(comment['post_id']):
                    comments_list.append(comment)
            return comments_list
        except ValueError:
            print("Комментариев к данному посту нет")
        except comments_list == []:
            return comments_list


def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    :param query: ключевое слово
    :return: список постов -> list[dict]
    """
    search_results = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            search_results.append(post)
    return search_results


def get_post_by_pk(pk):
    """
    возвращает один пост по его идентификатору.
    :param pk: илентификатор поста
    :return: пост по заданному идентификатору -> dict
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts_list = json.load(file)
        for item in posts_list:
            if pk == int(item['pk']):
                return item
