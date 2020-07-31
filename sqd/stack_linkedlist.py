# Linked List 로 구현한 Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Top data is pushed current data
    # Node's next data point next Node
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # If stack is not empty, return top node's data and changed top node to returned top node's next node
    def pop(self):
        if self.is_empty():
            return -1
        data = self.top.data
        self.top = self.top.next
        return data

    # If stack is not empty, return top node's data
    def peek(self):
        if self.is_empty():
            return -1
        return self.top.data

    def is_empty(self):
        if self.top:
            return False
        return True

