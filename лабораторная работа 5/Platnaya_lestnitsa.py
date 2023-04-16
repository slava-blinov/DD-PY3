from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    end = graph.number_of_nodes() - 1
    return nx.dijkstra_path_length(graph, 0, end)


def form_graph(stairs):
    if not stairs:
        raise ValueError("Пустой граф")

    nodes = [(i, i+1) for i in range(len(stairs))]
    graph = nx.DiGraph(nodes)

    edges = [(0, 1, stairs[0])]
    if len(stairs) > 1:
        for stair, cost in enumerate(stairs[1:], start=2):
            edges += [(stair - 2, stair, cost),
                      (stair - 1, stair, cost)]
    graph.add_weighted_edges_from(edges)

    return graph


if __name__ == '__main__':
    stairway = tuple([5, 11, 43, 2, 23, 43, 22, 12, 6, 8])
    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    stairway_graph = form_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
