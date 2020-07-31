# Linked List 로 구현한 Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # if queue is empty, front data = rear data
    # if queue has data, input pushed data at rear
    def push(self, data):
        if self.is_empty():
            self.front = data
            self.rear = data
        else:
            self.rear.next = data
            self.rear = self.rear.next

    # if queue has data, return front node's data and changed front node to returned front node's next node
    def pop(self):
        if self.is_empty():
            return -1
        val = self.front.data
        self.front = self.front.next

        if self.is_empty():
            self.rear = None

        return val

    # if queue has data, return front node's data
    def peek(self):
        if self.is_empty():
            return -1
        return self.front.data

    def is_empty(self):
        if self.front:
            return False
        return True


if __name__ == "__main__":
    q = Queue()
    q.push(Node("a"))
    q.push(Node("b"))
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.pop())
    q.push(Node("c"))
    print(q.pop())