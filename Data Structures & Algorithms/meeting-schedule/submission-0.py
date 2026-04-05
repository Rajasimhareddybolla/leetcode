"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start )
        first = intervals[0]
        os , oe = first.start , first.end
        for inte in intervals[1:]:
            start , end =  inte.start , inte.end
            if start< oe :
                return False
            os , oe = start , end
        return True
