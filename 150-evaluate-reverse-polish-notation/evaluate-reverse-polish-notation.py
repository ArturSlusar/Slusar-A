class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                #Достаем два последних числа из стэка
                b = stack.pop()
                a = stack.pop()

                #Выполняем операцию и кладем результат обратно в стэк
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b)) #Чтобы усекать дробную часть к нулю
            
            else:
                stack.append(int(token))

        return stack[0]
        