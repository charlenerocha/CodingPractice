class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # dp[i] represents the max money we can steal assuming we house i
        dp = [nums[0], nums[1]]
        max_amount = max(nums[0], nums[1])
        prev_max = nums[0]

        for i in range(2, len(nums)):
            curr_money = nums[i]

            dp.append(curr_money + prev_max)
            max_amount = max(dp[-1], max_amount)

            prev_max = max(dp[-2], prev_max)

        # print(dp)
        return max_amount