# BOJ 10989

import sys


if __name__ == "__main__":
    max_idx = int(sys.stdin.readline())
    fq_ls = [0] * 10000

    for _ in range(max_idx):
        val = int(sys.stdin.readline())
        fq_ls[val - 1] += 1

    for i in range(10000):
        for j in range(fq_ls[i]):
            print(i+1)



