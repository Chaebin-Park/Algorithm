# stack

import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    check = [False for i in range(N)]
    result = []

    def dfs_rec(dep, N, M):
        if dep == M:
            print(' '.join(map(str, result)))
            return

        for i in range(N):
            if not check[i]:
                check[i] = True
                result.append(i+1)
                dfs_rec(dep + 1, N, M)
                check[i] = False
                result.pop()

    dfs_rec(0, N, M)
