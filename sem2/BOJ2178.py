# BOJ 2178
# 미로 탐색
# 20200724

import sys


def bfs(maze, N, M):
    pos = [[0, 0]]
    visited = []
    x_check = [0, 1, 0, -1]
    y_check = [-1, 0, 1, 0]

    while pos:
        x, y = pos.pop()
        visited.append([x, y])

        if [N-1, M-1] in visited:
            break

        for i in range(4):
            x_pos = x + x_check[i]
            y_pos = y + y_check[i]
            try:
                if x_pos >= N-1 and y_pos >= M-1:
                    pos.append([0, 0])
                    break
                if 0 <= x_pos <= N and 0 <= y_pos <= M and maze[x_pos][y_pos] == 1 and [x_pos, y_pos] not in visited:
                    maze[x_pos][y_pos] += maze[x][y]
                    pos.append([x_pos, y_pos])
            except IndexError:
                continue

        print("=====================")
        for arr in maze:
            print(arr)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    check = [[False] * M for _ in range(N)]

    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().strip())))

    #print(bfs(maze, N, M))
    bfs(maze, N, M)
