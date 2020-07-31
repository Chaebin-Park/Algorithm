# 20200709

import sys


class bracket:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        item = ""
        try:
            item = self.stack[-1]
        except IndexError:
            item = ""
        return item

    def check(self, str):
        flag = True
        for ch in str:
            if ch == "(" or ch == "[":
                self.push(ch)
            elif ch == ")":
                if len(self.stack) == 0:
                    flag = False
                    break
                if self.top() == "(":
                    self.pop()
                else:
                    flag = False
                    break
            elif ch == "]":
                if len(self.stack) == 0:
                    flag = False
                    break
                if self.top() == "[":
                    self.pop()
                else:
                    flag = False
                    break
        return flag


if __name__ == "__main__":
    while True:
        str = input().rstrip()
        if str == ".":
            break
        b = bracket()

        if b.check(str):
            print("yes")
        else:
            print('no')
