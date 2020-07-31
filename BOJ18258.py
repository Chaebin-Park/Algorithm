# 20200709

from collections import deque
import sys


class queue:
    def __init__(self):
        self.ls = deque()

    def push(self, item):
        self.ls.append(item)

    def pop(self):
        if self.size():
            return self.ls.popleft()
        else:
            return -1

    def size(self):
        return len(self.ls)

    def empty(self):
        val = 1
        if self.ls:
            val = 0
        return val

    def front(self):
        if self.size():
            return self.ls[0]
        else:
            return -1

    def back(self):
        if self.size():
            return self.ls[-1]
        else:
            return -1


if __name__ == "__main__":
    num = sys.stdin.readline()
    q = queue()

    for i in range(int(num)):
        command = sys.stdin.readline().strip().split()

        if command[0] == "push":
            q.push(command[1])
        elif command[0] == "pop":
            print(q.pop())
        elif command[0] == "size":
            print(q.size())
        elif command[0] == "empty":
            print(q.empty())
        elif command[0] == "front":
            print(q.front())
        elif command[0] == "back":
            print(q.back())
