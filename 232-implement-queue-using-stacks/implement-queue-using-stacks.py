class MyQueue:

    def __init__(self):
        #Используем два стека для входа и выхода
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        #Всегда добавляем элементы во вхожящий стэк
        self.stack_in.append(x)

    def pop(self) -> int:
        #Этот вызов гарантирует что stack_out не пустой
        self.peek()
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        #Возвращаем верхний элемент исходящего стека
        return self.stack_out[-1]

    def empty(self) -> bool:
        #Очередь пуста когда пусты оба стэка
        return not self.stack_in and not self.stack_out