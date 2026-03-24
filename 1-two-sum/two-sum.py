class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            #Ищем число котороые в сумме с num выдаст target
            need = target - num
            #Проверяем есть ли это число в нашей хэш таблице
            if need in seen:
                return [seen[need], i]
            seen[num] = i

        return[]

