class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                x = i+1
                while x in nums:
                    x+= 1
                len = max(len, x - i)
        return len