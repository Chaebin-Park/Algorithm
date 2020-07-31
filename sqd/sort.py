# BOJ 2750

import sys


if __name__ == "__main__":
    max = int(sys.stdin.readline())

    arr = []

    for _ in range(max):
        arr.append(int(sys.stdin.readline()))

    arr.sort()

    for i in arr:
        print(i)
