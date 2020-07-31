# 힙 정렬

import sys


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def heapify(unsorted_list, idx):
    while True:
        if idx <= 1:
            break
        swap(unsorted_list, idx, idx//2)
        idx = idx // 2

    return unsorted_list


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    heap = [0, 1]

    for i in range(1, n):
        heap.append(i+1)
        heap = swap(heap, i, i+1)
        heap = heapify(heap, i)

    print(' '.join(map(str, heap[1:])))
