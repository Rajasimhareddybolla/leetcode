class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0] , x[1]))
        res = 0 
        per = []
        for start , end in intervals:
            if per and start<per[-1][1]:
                res +=1
            else:
                per.append([start , end])
        return res