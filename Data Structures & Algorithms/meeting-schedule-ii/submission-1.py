"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        temp = []
        for inte in intervals:
            temp.append([inte.start , inte.end])
        if not temp:
            return 0
        intervals = temp
        intervals.sort(key = lambda x: (x[0] ))
        res = 0 
        per = [[intervals[0][0] , intervals[0][1] , 0]]
        

        for start , end ,  in intervals[1:]:
            if  start<per[-1][1]:
                res +=1
                if per[-1][1] < end:
                    rr = per.pop(-1)
                    per.append([start , end , rr[-1]+1])
                    res = max(res ,rr[-1]+1 )
            else:
                per.append([start , end , 0 ])
        return max(res ,1 )