import pytest



class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected, book_genre",  [
        ("Matrix 3 перезагрузка", True, "Science fiction"),
        ("", False, "None"),
        ("0"*41, False, "None"),
        ("9"*39, True, "Action"),
        ("$#&@(%", True, "Drama"),
    ])
    def test_add_new_book(self, collector, book_name, expected, book_genre):
        collector.add_new_book(book_name)
        result = book_name in collector.books_genre
        assert result == expected


    def test_set_book_genre(self, collector, book_genre_params):
        book_name, genre = book_genre_params
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre


    @pytest.mark.parametrize("book_name, genre", [
        ("Matrix 3 перезагрузка", "Фантастика"),
        ("Кошмар на улице Вязов", "Ужасы")])
    def test_get_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre


    @pytest.mark.parametrize("book_name, genre", [
        ("Matrix 3 перезагрузка", "Фантастика"),
        ("Кошмар на улице Вязов", "Ужасы")
    ])
    def test_get_books_with_specific_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(genre)
        assert books_with_specific_genre
        for book in books_with_specific_genre:
            assert collector.get_book_genre(book) == genre


    def test_get_books_genre(self, collector):
        collector.add_new_book("Matrix 3 перезагрузка")
        books_genre = collector.get_books_genre()
        assert isinstance(books_genre, dict)
        assert "Matrix 3 перезагрузка" in books_genre


    def test_get_books_for_children(self, collector):
        collector.add_new_book('Достать ножи')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Достать ножи', 'Комедии')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Достать ножи', 'Винни Пух']


    @pytest.mark.parametrize("book_name, add_to_books, expected_in_favorites", [
        ("Harry Potter", True, True),
        ("Lord of the Rings", False, False)
    ])
    def test_add_book_in_favorites(self, collector, book_name, add_to_books, expected_in_favorites):
        if add_to_books:
            collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert (book_name in favorites) == expected_in_favorites


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        collector.delete_book_from_favorites('Кошмар на улице Вязов')
        assert 'Кошмар на улице Вязов' not in collector.get_list_of_favorites_books()


    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        assert collector.get_list_of_favorites_books() == ['Кошмар на улице Вязов']
