# 20200709

import sys


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    queue = [i for i in range(1, N + 1)]    # Create Queue. 1 ~ N
    result = []
    idx = 0

    # pop each (K-1)th index
    for i in range(N):
        idx += K - 1
        if idx >= len(queue):
            idx = idx % len(queue)
        result.append(queue.pop(idx))

    print("<", ", ".join(repr(e) for e in result), ">", sep="")
