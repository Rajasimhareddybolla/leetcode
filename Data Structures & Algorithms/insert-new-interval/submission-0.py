class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(intervals , newInterval):
            intervals.append(newInterval)
            intervals = sorted( intervals , key = lambda x:x[0])
            ps , pe = intervals[0][0] , intervals[0][1]
            res = [[ps, pe]]
            for st , en in intervals[1:]:
                if st<=pe<=en:
                    pe = max(pe , en)
                    res[-1][1] = pe
                else:
                    res.append([st ,en])
            return res
        return overlap(intervals , newInterval)