import pytest
from Лаба1 import find_roots


def test_two_real_roots():
    # Тест 1: Два действительных корня (дискриминант положительный)
    a, b, c = 1, -3, 2  # Уравнение: x^2 - 3x + 2 = 0
    roots = find_roots(a, b, c)
    assert roots == (2.0, 1.0), f"Ошибка: ожидались корни (2.0, 1.0), получено {roots}"


def test_one_real_root():
    # Тест 2: Один корень (дискриминант равен нулю)
    a, b, c = 1, -2, 1  # Уравнение: x^2 - 2x + 1 = 0
    roots = find_roots(a, b, c)
    assert roots == (1.0,), f"Ошибка: ожидался корень (1.0), получено {roots}"


def test_no_real_roots():
    # Тест 3: Нет действительных корней (дискриминант отрицательный)
    a, b, c = 1, 0, 1  # Уравнение: x^2 + 1 = 0
    roots = find_roots(a, b, c)
    assert roots is None, f"Ошибка: ожидался None, получено {roots}"


def test_all_coefficients_zero():
    # Тест 4: Коэффициенты все нули (особый случай)
    a, b, c = 0, 0, 0  # Уравнение: 0 = 0
    with pytest.raises(ZeroDivisionError):
        find_roots(a, b, c)


def test_linear_equation():
    # Тест 5: Линейное уравнение (a = 0, не квадратное уравнение)
    a, b, c = 0, 2, -4  # Уравнение: 2x - 4 = 0
    with pytest.raises(ZeroDivisionError):
        find_roots(a, b, c)


def test_fractional_roots():
    # Тест 6: Уравнение с дробными корнями
    a, b, c = 2, 5, -3  # Уравнение: 2x^2 + 5x - 3 = 0
    roots = find_roots(a, b, c)
    assert roots == (0.5, -3.0), f"Ошибка: ожидались корни (0.5, -3.0), получено {roots}"


def test_negative_discriminant():
    # Тест 7: Уравнение с отрицательным дискриминантом
    a, b, c = 1, 2, 5  # Уравнение: x^2 + 2x + 5 = 0
    roots = find_roots(a, b, c)
    assert roots is None, f"Ошибка: ожидался None, получено {roots}"
