class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr_index, sum_nums):
            if sum(sum_nums) == target:
                res.append(sum_nums.copy())
                return
            if sum(sum_nums)> target:
                return
            for i in range(curr_index, len(nums)):
                sum_nums.append(nums[i])
                backtrack(i, sum_nums)
                sum_nums.pop()

        backtrack(0, [])
        return res

        