import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        # првращаем массив в min-heap за О(N)
        heapq.heapify(self.min_heap)

        # Удаляеь минимальный элемент пока размер кучи юольше k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        #если куча не заполнилась до размера k то дополняем ее
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]

outpust1 = []
kthLargest = KthLargest(3, [4, 5, 8, 2])
outpust1.append(None)

outpust1.append(kthLargest.add(3))
outpust1.append(kthLargest.add(5))
outpust1.append(kthLargest.add(10))
outpust1.append(kthLargest.add(9))
outpust1.append(kthLargest.add(4))
print(outpust1)


outpust2 = []
kthLargest2 = KthLargest(4, [7, 7, 7, 7, 8, 3])
outpust2.append(None)

outpust2.append(kthLargest2.add(2))
outpust2.append(kthLargest2.add(10))
outpust2.append(kthLargest2.add(9))
outpust2.append(kthLargest2.add(9))
print(outpust2)

