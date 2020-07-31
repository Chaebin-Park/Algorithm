# BOJ9012 괄호

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return -1
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            return -1
        return self.top.data

    def is_empty(self):
        if self.top:
            return False
        return True


if __name__ == "__main__":
    max = int(input())

    result = []

    for i in range(max):
        str = sys.stdin.readline().strip()

        flag = True
        stack = Stack()

        for ch in str:
            if ch == "(":
                # ch is (
                stack.push(ch)
            elif ch == ")":
                # ch is )
                if stack.is_empty():
                    # ch is ) && stack is empty
                    flag = False
                    break
                if stack.peek() == "(":
                    # ch is ) && peek is ( then pop
                    stack.pop()
                else:
                    # "ch is ) && stack is not empty && peek is not (
                    flag = False
                    break

        if flag and stack.is_empty():
            result.append("YES")
        else:
            result.append("NO")

    for i in range(max):
        print(result[i])