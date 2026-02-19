from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <=r:
            m = l + ((r-l)//2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

solution = Solution()
result_1 = solution.search(nums=[-1,0,3,5,9,12], target=9)
print(result_1)

result_2 = solution.search(nums=[-1,0,3,5,9,12], target=2)
print(result_2)