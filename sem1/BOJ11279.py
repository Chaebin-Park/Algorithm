# BOJ11279
# 최대 힙
# 20200720

import heapq
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    heap = []

    # Heap push & pop
    for _ in range(N):
        x = int(sys.stdin.readline().strip())
        if x == 0:
            if not heap:
                print(0)
                continue
            print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (-x, x))

