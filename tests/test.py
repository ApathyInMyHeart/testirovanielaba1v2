from Лаба1 import find_roots
import unittest
"""
def test_find_roots():
    # Тест 1: Два действительных корня (дискриминант положительный)
    a, b, c = 1, -3, 2  # Уравнение: x^2 - 3x + 2 = 0
    roots = find_roots(a, b, c)
    assert roots == (2.0, 1.0), f"Ошибка: ожидались корни (2.0, 1.0), получено {roots}"

    # Тест 2: Один корень (дискриминант равен нулю)
    a, b, c = 1, -2, 1  # Уравнение: x^2 - 2x + 1 = 0
    roots = find_roots(a, b, c)
    assert roots == (1.0,), f"Ошибка: ожидался корень (1.0), получено {roots}"

    # Тест 3: Нет действительных корней (дискриминант отрицательный)
    a, b, c = 1, 0, 1  # Уравнение: x^2 + 1 = 0
    roots = find_roots(a, b, c)
    assert roots is None, f"Ошибка: ожидался None, получено {roots}"

    # Тест 4: Коэффициенты все нули (особый случай)
    a, b, c = 0, 0, 0  # Уравнение: 0 = 0
    try:
        roots = find_roots(a, b, c)
        assert False, "Ошибка: ожидалось исключение при делении на ноль"
    except ZeroDivisionError:
        pass  # Ожидаемая ошибка

    # Тест 5: Линейное уравнение (a = 0, не квадратное уравнение)
    a, b, c = 0, 2, -4  # Уравнение: 2x - 4 = 0
    try:
        roots = find_roots(a, b, c)
        assert False, "Ошибка: ожидалось исключение при делении на ноль"
    except ZeroDivisionError:
        pass  # Ожидаемая ошибка

    # Тест 6: Уравнение с дробными корнями
    a, b, c = 2, 5, -3  # Уравнение: 2x^2 + 5x - 3 = 0
    roots = find_roots(a, b, c)
    assert roots == (0.5, -3.0), f"Ошибка: ожидались корни (0.5, -3.0), получено {roots}"

    # Тест 7: Уравнение с отрицательным дискриминантом
    a, b, c = 1, 2, 5  # Уравнение: x^2 + 2x + 5 = 0
    roots = find_roots(a, b, c)
    assert roots is None, f"Ошибка: ожидался None, получено {roots}"

    print("Все тесты пройдены успешно!")


# Запуск тестов
test_find_roots()
"""

class TestQuadraticRoots(unittest.TestCase):
    def test_two_roots(self):
        root1, root2 = find_roots(1, -3, 2)
        self.assertAlmostEqual(root1, 1.0)
        self.assertAlmostEqual(root2, 2.0)

    def test_one_root(self):
        root1, root2 = find_roots(1, -2, 1)
        self.assertAlmostEqual(root1, 1.0)
        self.assertAlmostEqual(root2, 1.0)

    def test_no_roots(self):
        root1, root2 = find_roots(1, 1, 1)
        self.assertIsNone(root1)
        self.assertIsNone(root2)

    def test_zero_a(self):
      with self.assertRaises(ZeroDivisionError):
        find_roots(0, 1, 1)

if __name__ == '__main__':
    unittest.main()