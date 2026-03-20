class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        see = set()

        for num in nums:
            #Если число уже бвло добавлено то это дупликат
            if num in see:
                return True

            #Если числа не юыло то добавлем его а хэш
            see.add(num)

        #Если цикл завершился полностью то значит дупликатов нету
        return False 