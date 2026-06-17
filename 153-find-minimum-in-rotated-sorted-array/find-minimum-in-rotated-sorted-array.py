class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (nums[0] < nums [len(nums)-1]):
            return nums[0]
        num = len(nums) // 2
        if num // 2 > 0:
            inc = num //2
        else:
            inc = 1
        while nums[num] > nums [num-1]:
            if nums[num] > nums[0]:
                num += inc
            else:
                num -= inc
            if inc // 2 > 0:
                inc = inc // 2
            else:
                inc = 1
        return nums[num]