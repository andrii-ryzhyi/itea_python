class _Node:

    def __init__(self, value):
        self._value = value
        self._next = None
    
    def get_value(self):
        return self._value
    
    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node
    
    def __repr__(self):
        return f"{self._value}"
    

class LinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0
    
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail
    
    def get_count(self):
        return self._count
    
    def is_empty(self):
        return self._count == 0

    def add_first(self, value):
        node = _Node(value)
        if self._head:
            temp = self._head
            self._head = node
            self._head.set_next(temp)
        else:
            self._head = node
            self._tail = node
        self._count += 1

    def add_last(self, value):
        node = _Node(value)
        if self._head:
            self._tail.set_next(node)
        else:
            self._head = node
        self._tail = node
        self._count += 1  

    def remove_first(self):
        return_node = None
        if self._head:
            return_node = self._head
            self._head = self._head.get_next()
            self._count -= 1
            if self._count == 0:
                self._tail = None
                self._head = None
        return return_node
    
    def remove_last(self):
        return_node = None
        if self._head:
            if self._count == 1:
                return_node = self._head
                self._tail = None
                self._head = None
            else:
                current = self._head
                while current.get_next() != self._tail:
                    current = current.get_next()
                return_node = current.get_next()
                current.set_next(None)
                self._tail = current
            self._count -= 1
        return return_node
    
    def remove_all(self):
        self._head = None
        self._tail = None
        self._count = 0
    
    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current.get_next()

class Stack:
    
    def __init__(self):
        self._list = LinkedList()
    
    def push(self, obj):
        self._list.add_first(obj)
    
    def pop(self):
        if self._list.is_empty():
            raise Exception("Stack is empty")
        value = self._list.get_head()
        self._list.remove_first()
        return value
    
    def peek(self):
        if self._list.is_empty():
            raise Exception("Stack is empty")
        return self._list.get_head()

    def count(self):
        return self._list.get_count()

    def clear(self):
        self._list.remove_all()

    def __iter__(self):
        return self._list.__iter__()


class Queue:

    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, obj):
        self._list.add_last(obj)
    
    def dequeue(self):
        if self._list.is_empty():
            raise Exception("Queue is empty")
        value = self._list.get_head()
        self._list.remove_first()
        return value

    def peek(self):
        if self._list.is_empty():
            raise Exception("Queue is empty")
        return self._list.get_head()

    def count(self):
        return self._list.get_count()
    
    def clear(self):
        self._list.remove_all()
    
    def __iter__(self):
        return self._list.__iter__()


print("Creating Stack")
stack = Stack()
for i in range(10):
    stack.push(i)

for element in stack:
    print(element)

print("Creating Queue")
queue = Queue()
for i in range(10):
    queue.enqueue(i)

for element in queue:
    print(element)

stack.push(20)
stack.push(21)
el = stack.pop()
print(f"pop element is: {el}")
print(f"stack count: {stack.count()}")

queue.enqueue(30)
queue.enqueue(31)
el = queue.dequeue()
print(f"Queue element removed: {el}")






                