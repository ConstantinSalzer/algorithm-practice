class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range (len(nums)-2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            left = i +1
            right = len(nums)-1
            while (left < right):
                sum = nums[i]+nums[left]+nums[right] 
                if (sum == 0):
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -=1
                    while True:
                        if (left >= right):
                            break
                        if (nums[left-1] == nums[left]):
                            left+= 1
                        if (nums[right+1] == nums[right]):
                            right-= 1
                        if (nums[right+1] != nums[right] and nums[left-1] != nums[left]):
                            break
                if (sum < 0):
                    left += 1
                if (sum > 0):
                    right -=1
        return res
