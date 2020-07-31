# List 로 구현한 Queue


class Queue:
    def __init__(self):
        self.queue = []

    # push data at index 0
    def push(self, data):
        self.queue.insert(0, data)

    # if queue is not empty, pop data
    def pop(self):
        if self.is_empty():
            return -1
        return self.queue.pop()

    # if queue is not empty, return front data (index -1)
    def peek(self):
        if self.is_empty():
            return -1
        return self.queue[-1]

    # if queue is empty, return True. if queue has data, return False
    def is_empty(self):
        if self.queue:
            return False
        return True
