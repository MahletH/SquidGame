class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniques = set(nums)
        return len(uniques) if 0 not in uniques else len(uniques) - 1