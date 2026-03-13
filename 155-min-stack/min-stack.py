class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        #Если стэк пуст то текущий минимум равен значению который мы добавиили
        if not self.stack:
            self.stack.append((val, val))
        else:
            #Сравниваем новый элемент с предыдущем минимальным
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        #Удаляем верхний элемент
        self.stack.pop()

    def top(self) -> int:
        #Возвращаем само значение
        return self.stack[-1][0]

    def getMin(self) -> int:
        #Возвращаем минимум на текущий момент
        return self.stack[-1][1]
        
