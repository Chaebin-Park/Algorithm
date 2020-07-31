# 20200714

import sys
from collections import deque


class AC:
    def __init__(self, deque):
        self.deque = deque
        self.is_reversed = False
        self.flag = True

    def R(self):
        print("R")
        self.is_reversed = not self.is_reversed

    def D(self):
        print("D")
        if self.is_empty():
            print("error")
            self.flag = False
        else:
            if self.is_reversed:
                self.deque.pop()
            else:
                self.deque.popleft()

    def print_deq(self):
        if self.flag:
            if self.is_reversed:
                print(str(list(map(int, reversed(self.deque)))).replace(" ", ""))
            else:
                print(str(list(map(int, self.deque))).replace(" ", ""))

    def is_empty(self):
        if self.deque:
            return False
        return True


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for i in range(T):
        command = list(sys.stdin.readline().strip())
        max = int(sys.stdin.readline().strip())
        arr = deque(str(sys.stdin.readline()).replace('[', "").replace(']', "").replace("\n", "").strip().split(','))

        print(len(arr), " ", list(arr))

        ac = AC(arr)

        idx = 0
        while True:
            try:
                if command[idx] == "R":
                    ac.R()
                else:
                    ac.D()
            except IndexError:
                break
            idx += 1

        ac.print_deq()
