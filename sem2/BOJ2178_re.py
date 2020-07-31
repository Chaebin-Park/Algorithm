import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maze = []   # 입력받은 미로
    pos = [[0, 0]]  # 좌표 입력 큐
    visited = [[0]*M for _ in range(N)] # 방문여부 확인
    visited[0][0] = 1 # 시작지점은 무조건 탐색

    # 현재 좌표의 상,하,좌,우 확인하기 위한 x,y 좌표쌍
    x_check = [0, 1, 0, -1]
    y_check = [-1, 0, 1, 0]

    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().strip())))

    while pos:
        # 현재 좌표
        x, y = pos.pop(0)

        for i in range(4):
            # 현재 좌표의 상,하,좌,우 칸 확인
            x_pos = x + x_check[i]
            y_pos = y + y_check[i]

            # 미로 좌표 벗어나는 경우 체크
            if 0 > x_pos or x_pos >= N:
                continue
            if 0 > y_pos or y_pos >= M:
                continue

            # 좌표가 0일 경우 길이 아님
            if maze[x_pos][y_pos] == 0:
                continue

            # 이미 방문한 곳인지 확인
            if visited[x_pos][y_pos]:
                continue

            # 길이 확인된 경우 방문했다고 체크하기
            visited[x_pos][y_pos] = visited[x][y] + 1
            pos.append([x_pos, y_pos])

    print(visited[N-1][M-1])