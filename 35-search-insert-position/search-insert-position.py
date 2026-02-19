from typing import List

class Solution:
    def searchInsert(self,nums:List[int], target:int) -> int:
        l,r = 0, len(nums) - 1

        while l <=r:
            mid = (l+r) // 2
    
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l

s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))

        