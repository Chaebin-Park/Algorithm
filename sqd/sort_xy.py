import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    coor = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coor.append(list([y, x]))

    coor.sort()

    for i in range(N):
        print(" ".join(repr(e) for e in reversed(coor[i])))
