import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()



@pytest.fixture(params=[
        ("Matrix 3 перезагрузка",  "Фантастика"),
        ("Кошмар на улице вязов", "Ужасы")
])
def book_genre_params(request):
    return request.param


