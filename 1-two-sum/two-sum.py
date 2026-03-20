class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #создвем хэш таблицу для хранения уже просмотренных чисел ключ которых это само числоо а знпчение это его индекс в массиве
        seen = {}

        #Проходим по массиву получая индекс i и значение num
        for i, num in enumerate(nums):
            #Ищем число котороые в сумме с num выдаст target
            complement = target - num
            #Проверяем есть ли это число в нашей хэш таблице
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return[]

        