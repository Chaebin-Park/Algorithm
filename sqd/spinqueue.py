# 20200714

import sys
from collections import deque


class Spin:
    def __init__(self, N):
        self.deque = deque()
        self.count = 0
        for i in range(1, N+1):
            self.deque.append(i)

    # rotate right to num
    # rotation : append left(pop)
    def rotate_right(self, num):
        while True:
            if self.get_rear() == num:
                self.deque.popleft()
                break
            self.deque.appendleft(self.deque.pop())
            self.count += 1

    # rotate left to num
    # rotation : append(pop left)
    def rotate_left(self, num):
        while True:
            if self.get_rear() == num:
                self.deque.popleft()
                break
            self.deque.append(self.deque.popleft())
            self.count += 1

    # check where is num
    # if num < (list len / 2) then num is close to rear. return True
    # else then num is close to front. return False
    def check(self, num, N):
        cnt = 0
        for i in self.deque:
            if i == num:
                break
            cnt += 1
        if cnt <= int(N / 2):
            return True
        else:
            return False

    def get_rear(self):
        return self.deque[0]

    def get_count(self):
        return self.count


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    seq = map(int, sys.stdin.readline().split())

    spin = Spin(N)
    result = 0

    for i in seq:
        # If i closed to rear then rotate left
        # else then rotate right
        if spin.check(i, N):
            spin.rotate_left(i)
        else:
            spin.rotate_right(i)
        N -= 1

    print(spin.get_count())
