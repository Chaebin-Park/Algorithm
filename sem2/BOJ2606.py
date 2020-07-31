# BOJ 2606
# 바이러스
# 20200723

import sys


def bfs(dic, idx):
    queue = [idx]
    visited = []

    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited


if __name__ == "__main__":
    com = int(sys.stdin.readline())
    pair = int(sys.stdin.readline())

    check = [False] * com
    net = {i: [] for i in range(1, com + 1)}

    for _ in range(pair):
        key, val = map(int, sys.stdin.readline().split())
        net[key].append(val)
        net[val].append(key)

    print(len(bfs(net, 1)) - 1)
