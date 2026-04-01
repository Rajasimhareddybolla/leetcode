class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0] ))
        res = 0 
        per = [intervals[0]]
        def duration(inte):
            return inte[1]- inte[0]
        for start , end in intervals[1:]:
            if  start<per[-1][1]:
                res +=1
                if per[-1][1] > end:
                    per.pop(-1)
                    per.append([start , end])

            else:
                per.append([start , end])
        return res