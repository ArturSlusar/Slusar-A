from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int):

    # Функция востонавливающая своцства минимальной кучи
        def sift_down(heap, i, heap_size):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # проверяем, меньше ли левый потомок, чем текущий элемент
            if left < heap_size and heap[left] < heap[smallest]:
                smallest = left

            # также проверяем правого потомка
            if right < heap_size and heap[right] < heap[smallest]:
                smallest = right

            # если самый маленький элемент не родитель то меняем их местами
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                sift_down(heap, smallest, heap_size)
    
        # создаем массив для кучи из первых k элементов
        min_heap = nums[:k]

        #строим min-heap
        for i in range(k // 2 - 1, -1, -1):
            sift_down(min_heap, i, k)
        
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                min_heap[0] = nums[i]
                sift_down(min_heap, 0, k)

        return min_heap[0]

nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4

solution = Solution()
result1 = solution.findKthLargest(nums1, k1)
print("Example 1: ", result1 )

result2 = solution.findKthLargest(nums2, k2)
print("Example 2: ", result2)
     