class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        res.append(0)
        days = []
        days.insert(0,[temperatures.pop(), len(temperatures)])
        for i in range (len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while days:
                if temp >= days[0][0]:
                    days.pop(0)
                else:
                    res.insert(0, days[0][1]-i)
                    days.insert(0,[temp,i])
                    break
            if not days:
                res.insert(0,0)
                days.insert(0,[temp,i])
        return res