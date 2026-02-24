from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        for point in points:
            x = point[0]
            y = point[1]

            #Считааем квадрат расстоянич
            dist = (x * x) + (y * y)

            distances.append([dist, point]) 

        #Сортируем список по возрастанию дистанции так как индекс стоит на нулевом индексе в паре
        sorted_distances = sorted(distances)

        result = []
        for item in sorted_distances[:k]:
            result.append(item[1])

        return result

sol = Solution()

print("Example 1: ", sol.kClosest([[1,3], [-2, 2]], 1))
print("Example 2: ", sol.kClosest([[3,3], [5, -1], [-2, 4]], 2))