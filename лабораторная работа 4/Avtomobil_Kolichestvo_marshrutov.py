from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    paths_ = [[0 for _ in range(m)] for _ in range(n)]
    paths_[0][0] = 1

    for x in range(n):
        for y in range(m):
            if 0 <= y + 1 < m:
                paths_[x][y+1] += paths_[x][y]
            if 0 <= x + 1 < n:
                paths_[x+1][y] += paths_[x][y]
            if 0 <= x + 1 < n and 0 <= y + 1 < m:
                paths_[x+1][y+1] += paths_[x][y]

    return paths_


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
