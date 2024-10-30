import math


def find_roots(a, b, c):
    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    # Определяем количество корней
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2  # Два различных корня
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,  # Один корень (возвращаем кортеж)
    else:
        return None  # Нет действительных корней



