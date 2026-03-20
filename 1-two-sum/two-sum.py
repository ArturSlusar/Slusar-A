class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #создвем хэш таблицу для хранения уже просмотренных чисел ключ которых это само числоо а знпчение это его индекс в массиве
        see = {}

        #Проходим по массиву получая индекс i и значение num
        for i in range(len(nums)):
            num = nums[i]
            #Ищем число котороые в сумме с num выдаст target
            need = target - num
            #Проверяем есть ли это число в нашей хэш таблице
            if need in see:
                return [see[need], i]
            see[num] = i

        return[]

        