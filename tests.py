import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self,collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_cannot_add_same_book_twice(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['', 'A' * 41])
    def test_add_new_book_invalid_length(self, collector, book_name):
        collector.add_new_book(book_name)

        assert collector.get_books_genre() == {}

    def test_set_book_genre_sets_correct_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')

        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_set_book_genre_does_not_set_invalid_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Неизвестный жанр')

        assert collector.get_book_genre('Война и мир') == ''

    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book('Книга детская')
        collector.add_new_book('Книга взрослая')
        collector.set_book_genre('Книга детская', 'Мультфильмы')
        collector.set_book_genre('Книга взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Книга детская']

    def test_add_book_in_favorites_adds_once(self, collector):
        collector.add_new_book('Книга любимая')
        collector.add_book_in_favorites('Книга любимая')
        collector.add_book_in_favorites('Книга любимая')

        assert collector.get_list_of_favorites_books() == ['Книга любимая']

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Книга любимая')
        collector.add_book_in_favorites('Книга любимая')
        collector.delete_book_from_favorites('Книга любимая')

        assert collector.get_list_of_favorites_books() == []
    