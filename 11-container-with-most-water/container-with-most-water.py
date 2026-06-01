class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        links = 0
        rechts = len(height)-1
        while (links < rechts):
            if (height[links]<height[rechts]):
                if (height[links]*(rechts-links) > max):
                    max = height[links]*(rechts-links)
                links += 1
            else:
                if (height[rechts]*(rechts-links) > max):
                    max = height[rechts]*(rechts-links)
                rechts -= 1
        return max
