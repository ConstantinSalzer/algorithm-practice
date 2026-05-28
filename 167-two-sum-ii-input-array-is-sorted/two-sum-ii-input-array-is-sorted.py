class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (numbers[right]+numbers[left] != target):
            if (numbers[right]+numbers[left]<target):
                left += 1
            else:
                right -= 1
        return [left+1, right+1]