class Node:
    def __init__(self, v, d=None):
        self.value = v
        self.next = d


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node != None:
            if node.value == val:
                return node
            else:
                node = node.next
        return None

    def len(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def clean(self):
        self.head = None
        self.tail = None

    # проверить если элемента нет в списке
    def delete(self, val, all=False):  # если нужно найти на удаление более 2 х элементов мб
        if self.head == None:  # после нахождения 1 го запускать цикл по новой
            return
        one_run = self.head
        two_run = self.head
        if one_run.value == val and self.head.next == None:  # если удаляем один элемент
            self.head = self.tail = None
            return
        if one_run.value == val:  # если удаляем первый элемент
            self.head = self.head.next
        while one_run != None:
            if one_run.value == val:
                two_run.next = one_run.next
                if one_run == self.tail:
                    self.tail = two_run
                if all == False:
                    return
                else:
                    one_run = self.head
                    two_run = self.head
            else:
                two_run = one_run
                one_run = one_run.next

    def find_all(self, val):
        node = self.head
        arr = []
        while node != None:
            if node.value == val:
                arr.append(node)
                node = node.next
            else:
                node = node.next
        return arr

    def insert(self, afterNode, newNode):# на вход подаются ноды my_list.insert(None, Node(63))
        node = self.head
        end = self.tail
        if self.head == None:
            self.tail = self.head = newNode  # self.tail = self.head = Node(newNode)
            return
        while node != None:
            if node.value == end.value: # вставляем ноду в конец списка
                node.next = newNode #node.next = newNode(node.next)
                self.tail = self.tail.next
                return
            if node.value == afterNode.value:  # вставляем ноду в начало
                    node.next = Node(newNode.value, node.next)  # node.next = newNode(node.next)
                    return
            else:
                node = node.next
#
