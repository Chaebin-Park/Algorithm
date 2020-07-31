# BOJ 2178
# 미로 탐색
# 20200724

import sys


def cmp(a, b):
    if a == 0:
        return b + 1
    if b == 0:
        return a + 1

    if a > b:
        return b + 1
    else:
        return a + 1


def bfs(maze, x, y, N, M):
    pos = []
    visited = []
    x_check = [0, 1, 0, -1]
    y_check = [-1, 0, 1, 0]

    pos.append([x, y])
    while pos:
        x, y = pos.pop()
        visited.append([x, y])

        if [N-1, M-1] in visited:
            break

        for i in range(4):
            if 0 <= x + x_check[i] < N:
                x_pos = x + x_check[i]
            if 0 <= y + y_check[i] < M:
                y_pos = y + y_check[i]

            if 0 <= x_pos <= N and 0 <= y_pos <= M and maze[x_pos][y_pos] == 1 and [x_pos, y_pos] not in visited:
                maze[x_pos][y_pos] += maze[x][y]
                visited.append([x_pos, y_pos])
                pos.append([x_pos, y_pos])

    #for arr in maze:
    #    print(arr)

    return maze[N-1][M-1]
    #return cmp(maze[N-2][M-1], maze[N-1][M-2])


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    check = [[False] * M for _ in range(N)]

    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().strip())))

    print(bfs(maze, 0, 0, N, M))
