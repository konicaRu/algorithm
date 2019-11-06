class PowerSet:

    def __init__(self):
        self.slots = []  # создает массив под множество

    def size(self):
        return len(self.slots)
        # количество элементов в множестве

    def put(self, value):
        if self.get(value) == True:  # если значение уже есть во множестве
            return
        else:
            self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True  # возвращает True если value имеется в множестве,
        else:  # иначе False
            return False

    def remove(self, value):
        if self.get(value) == True:  # возвращает True если value удален
            self.slots.remove(value)
            return True
        else:  # иначе False
            return False

    def intersection(self, set2):
        arr = []
        for i in set2:
            if i in self.slots:  # пересечение текущего множества и set2
                arr.append(i)
        return arr

    def union(self, set2):
        for i in set2:
            if self.get(i) == True:  # объединение текущего множества и set2
                continue
            else:
                self.put(i)
            return self.slots

    def difference(self, set2):
        inter_set = []
        for i in self.slots:
            if i not in set2:  # пересечение текущего множества и set2
                inter_set.append(i)
        return inter_set
        # разница текущего множества и set2

    def issubset(self, set2):
        count = 0
        for i in set2:
            if i in self.slots:
                count += 1
        if count == len(set2):
            return True
        else:
            return False
