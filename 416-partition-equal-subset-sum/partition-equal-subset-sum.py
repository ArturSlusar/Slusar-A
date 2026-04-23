class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Если общая сумма нечетная, разбить на две равные части невозможно
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Идем с конца, чтобы не использовать одно и то же число дважды
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[target]