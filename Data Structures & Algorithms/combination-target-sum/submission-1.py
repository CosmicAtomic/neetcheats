class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sum_nums = []
        def backtrack(curr_index):
            total = sum(sum_nums)
            if total == target:
                res.append(sum_nums.copy())
                return
            if total > target:
                return
            for i in range(curr_index, len(nums)):
                sum_nums.append(nums[i])
                backtrack(i)
                sum_nums.pop()
        backtrack(0)
        return res

        