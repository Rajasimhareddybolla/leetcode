class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[i]<temperatures[j]:
                    res[i]