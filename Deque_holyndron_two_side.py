class Deque:
    def __init__(self):
        self.stack = []

    def addFront(self, item):
        if self.size() == 0:
            self.stack.append(item)
        else:
            self.stack.insert(0, item)

    def addTail(self, item):
        self.stack.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None  # если очередь пуста
        first_el = self.stack[0]
        self.stack.pop(0)
        return first_el

    def removeTail(self):
        if self.size() == 0:
            return None  # если очередь пуста
        last_el = self.stack[-1]
        self.stack.pop()
        return last_el

    def size(self):
        return len(self.stack)

    def polyndrom(self):
        if self.size() == 0 or self.size() == 1:
            return 'It is polyndrom'
        while self.size() > 1:
            if self.removeFront() != self.removeTail():
                return 'It is not polyndrom'

        return 'It is polyndrom'


deq = Deque()
deq.addFront("л")
deq.addFront("а")
deq.addTail("а")
deq.addFront("8")
deq.addTail("ш")
print(deq.polyndrom())
#
