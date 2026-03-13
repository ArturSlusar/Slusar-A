class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.max_size = k
        self. head = 0   
        self.tail = -1
        self.current_size = 0    #Считаем сколько элементво внутри 

    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False

        self.tail = self.tail + 1    #Двигаем хвост на одну позицию вперед

        if self.tail == self.max_size:
            self.tail = 0 

        self.queue[self.tail] = value
        self.current_size = self.current_size + 1     #Увеличиваем счетчик элементов
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() == True:    #Если очередь пустая то удалять нечего
            return False

        self.head = self.head + 1 #Двигаем голову вперед чтобы забыть старый элемент
        
        if self.head == self.max_size:
            self.head = 0

        self.current_size = self.current_size - 1     #Уменьшаем счетчик
        return True

    def Front(self) -> int:
        if self.isEmpty() == True:   #Возвращаем первый элемент
            return -1
        return self.queue[self.head]        

    def Rear(self) -> int:
        if self.isEmpty() == True:    #Возвращаем последнйи элемент
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.current_size == 0:    #Если элемент 0 значит пусто
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.current_size == self.max_size:    #Если элементов столько же, сколько максимум значит полная
            return True
        else:
            return False
        
