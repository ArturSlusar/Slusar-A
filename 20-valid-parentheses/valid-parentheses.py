class Solution:
    def isValid(self, s: str) -> bool:
        #Строка для быстрой проверки пар
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            #Если это закрывающаяся скобка
            if char in bracket_map:
                #достаем верхний элемент стека если он не пуст, ксли пуст то присваеваем например # который не совпадает
                top_element = stack.pop() if stack else '#'

                #Если открывающаяся скобка не соответствует закрывающейся 
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        result = not stack
        return result

sol = Solution()
sol.isValid("()")
sol.isValid("() [] {}")
sol.isValid("(]")
sol.isValid("([])")
sol.isValid("(([)]")

