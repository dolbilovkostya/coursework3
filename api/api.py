from flask import jsonify
from flask import Blueprint
from api.utils import load_posts, get_post_by_pk
import logging


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_all_posts():
    """
    Возвращает список JSON-словаря со всеми постами
    :return: список со словарем
    """
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info('Запрос api/posts')
    return jsonify(load_posts())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    """
    Возвращает JSON-словарь с одним постом по заданному postid
    :param postid: Номер поста
    :return: JSON-словарь
    """
    path = f'api/posts/{postid}'
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info(f'Запрос {path}')
    return jsonify(get_post_by_pk(postid))
