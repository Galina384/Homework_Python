import pytest  # noqa: F401
from string_utils import StringUtils


class TestStringUtils:
    """Тесты для класса StringUtils"""

    def setup_method(self):
        """Инициализация перед каждым тестом"""
        self.utils = StringUtils()

    def test_capitalize_positive_english(self):
        """Позитивный тест 1: английское слово"""
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_positive_russian(self):
        """Позитивный тест 2: русское слово"""
        assert self.utils.capitalize("привет") == "Привет"

    def test_capitalize_negative_empty_string(self):
        """Негативный тест 1: пустая строка"""
        assert self.utils.capitalize("") == ""

    def test_capitalize_negative_space_string(self):
        """Негативный тест 2: строка с пробелом"""
        assert self.utils.capitalize(" ") == " "

    def test_trim_positive_spaces_front(self):
        """Позитивный тест 1: пробелы в начале"""
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_positive_no_spaces(self):
        """Позитивный тест 2: без пробелов в начале"""
        assert self.utils.trim("skypro") == "skypro"

    def test_trim_negative_only_spaces(self):
        """Негативный тест 1: только пробелы"""
        assert self.utils.trim("   ") == ""

    def test_trim_negative_spaces_front_and_back(self):
        """Негативный тест 2: пробелы спереди и сзади"""
        assert self.utils.trim("   skypro   ") == "skypro   "

    def test_contains_positive_found_single(self):
        """Позитивный тест 1: найден одиночный символ"""
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_positive_found_substring(self):
        """Позитивный тест 2: найдена подстрока"""
        assert self.utils.contains("SkyPro", "kyP") is True

    def test_contains_negative_not_found(self):
        """Негативный тест 1: символ не найден"""
        assert self.utils.contains("SkyPro", "X") is False

    def test_contains_negative_empty_string(self):
        """Негативный тест 2: пустая строка для поиска"""
        assert self.utils.contains("", "S") is False

    def test_delete_symbol_positive_single_char(self):
        """Позитивный тест 1: удаление одного символа"""
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_positive_substring(self):
        """Позитивный тест 2: удаление подстроки"""
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_negative_not_found(self):
        """Негативный тест 1: символ не найден"""
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_negative_empty_symbol(self):
        """Негативный тест 2: пустой символ для удаления"""
        assert self.utils.delete_symbol("SkyPro", "") == "SkyPro"
