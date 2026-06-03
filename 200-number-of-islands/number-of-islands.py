class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for x in range(len(grid)):
            while "1" in grid[x]:
                num += 1
                lands = []
                lands.append([x,grid[x].index("1")])
                while lands:
                    land = lands.pop()
                    grid[land[0]][land[1]]="0"
                    if (land[0]>0):
                        if grid[land[0]-1][land[1]] == "1":
                            lands.append([land[0]-1, land[1]])
                    if (land[0]<len(grid)-1):
                        if grid[land[0]+1][land[1]] == "1":
                            lands.append([land[0]+1,land[1]])
                    if (land[1]>0):
                        if grid[land[0]][land[1]-1] == "1":
                            lands.append([land[0],land[1]-1])
                    if (land[1]<len(grid[0])-1):
                        if grid[land[0]][land[1]+1] == "1":
                            lands.append([land[0], land[1]+1])

        return num                    
