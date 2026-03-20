class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Если данные отличаются то это точно не анаграммы
        if len(s) != len(t):
            return False

        counts = {}

        #Считаем буквы
        for char in s:
            if char in counts:
                counts[char] += 1 #Если буква есть то счетчик увеличивается
            else:
                counts[char] = 1 #Если нет то добавляем со значением 1

        for char in t:
            #Если букв вообще не было в первой строку это не анаграмм
            if char not in counts:
                return False

            counts[char] -= 1

            if counts[char] < 0:
                return False

        return True
