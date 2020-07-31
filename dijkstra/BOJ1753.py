# BOJ 1753
# 최단경로
# 20200730
# Chaebin Park

import sys


def dijkstra(graph, visited, V, K, result):
    print("_________________")
    print("start : V = ", V, " K = ", K)
    next_node = None

    print("dij : ", graph[K-1])

    # 현재 노드에서 미방문 노드를 탐색, 시험적 거리를 계산
    tmp = 11
    for i in range(V):
        # 새로 계산한 시험적 거리를 현재 값과 비교해 작은 값을 넣는다.
        print("visited[i] : ", visited[i])
        if 0 < graph[K-1][i] <= tmp and not visited[i]:
            print(next_node)
            tmp = graph[K-1][i]
            next_node = i + 1
            print("next_node : ", next_node)

    print("next_node out : ", next_node)
    if next_node is None:
        print(result)
    else:
        visited[K-1] = not visited[K-1]
        result += graph[K-1][next_node - 1]
        print("result : ", result)
        dijkstra(graph, visited, V, next_node, result)

    # 현재 인접한 모든 미방문 노드를 계산했다면 현재 노드를 방문한 것으로 표시


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    graph = [[0] * V for _ in range(V)]
    visited = [False] * V

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w

    dijkstra(graph=graph, visited=visited, V=V, K=K, result=0)


