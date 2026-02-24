from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        #Сортируем пары по убыванию частоты
        sorted_pairs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        #Собираем ответ и берем первые к пар из списка
        result =  []
        for pair in sorted_pairs[:k]:
            result.append(pair[0])

        return result

sol = Solution()

print("Example 1:", sol.topKFrequent([1,1,1,2,2,3], 2))
print("Example 2:", sol.topKFrequent([1], 1))
print("Example 3:", sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))