# 20200716
# BOJ 11725
# 트리의 부모 찾기

import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    arr = {i: [] for i in range(1, N+1)}
    result = {i: [] for i in range(1, N+1)}

    print(arr)

    for _ in range(N-1):
        d, n = sys.stdin.readline().split()
        arr[int(d)].append(int(n))
        #arr[int(n)].append(int(d))
        result[int(n)].append(int(d))

    print(arr)
    print(result)


