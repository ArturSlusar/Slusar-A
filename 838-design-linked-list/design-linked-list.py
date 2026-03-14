class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None    #Указатель на начало списка
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1    #Если индекс не правельный то сразу вернем -1
            
        current = self.head
        for i in range(index):
            current = current.next    # шагаем по ссылкам нужное колличество раз

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)    #Добавление в начало это ставка на индекс 0

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)   #Добавление в конец это вставка на индекс который равен текущему размеру

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0    #Есои индекс отрицательный то ставим в начало

        new_node = Node(val)

        if index == 0:    #Если вставляем в начало то идем до узла который стоит перед нужным местом
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index -1):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        self.size = self.size + 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return    #Проверем существует ли такой индекс

        if index == 0:    #Если удаляем первую голову то идем до узла перед удаляемым
            self.head = self.head.next
        else:
            current = self.head

            for i in range(index - 1):
                current = current.next

            current.next = current.next.next

        self.size = self.size - 1