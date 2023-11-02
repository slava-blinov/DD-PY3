def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Факториал отрицательного числа")
    if not isinstance(n, int):
        raise TypeError("Факториал не от целого числа")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial
