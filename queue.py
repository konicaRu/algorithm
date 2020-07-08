class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)
        # вставка в хвост

    def dequeue(self):
        if self.size() == 0:
            return None  # если очередь пустая
        first_el = self.queue[0]
        self.queue.pop(0)
        return first_el

    def size(self):
        return len(self.queue)

#

