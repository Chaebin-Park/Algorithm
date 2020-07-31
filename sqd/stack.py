# List 로 구현한 Stack


class Stack(list):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    # if stack is not empty, pop data
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    # if stack is not empty, return stack's top data (index -1)
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]

    # if queue is empty, return True. if queue is not empty, return False
    def is_empty(self):
        if len(self.stack):
            return False
        return True
