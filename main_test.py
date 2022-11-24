import pytest
import main
from utils import get_posts_all


def test_return_posts_by_json():
    response = main.app.test_client().get('http://127.0.0.1/api/posts')
    assert isinstance(response, list) == True, "Страница возвращает не список"
