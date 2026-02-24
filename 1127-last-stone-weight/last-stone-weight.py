from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Крутим цикл пока в списке больше одного камня
        while len(stones) > 1:
            stones.sort() #сортируем оставив тяжелые в конце

            #Ищем 2 самых тяжелых камня
            y = stones.pop()
            x = stones.pop()

            if y != x:
                stones.append(y - x)

        #Если камней не осталось то вернем 0
        if len(stones) == 0:
            return 0
        #вовзращаем последний оставшийся если чтото осталось
        else:
            return stones[0]

sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))
print(sol.lastStoneWeight([1]))
        
        