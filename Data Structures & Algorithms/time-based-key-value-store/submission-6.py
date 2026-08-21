class TimeMap:

    def __init__(self):
        self.memo = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.memo:
            self.memo[key] = []
        self.memo[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""
        
        values = self.memo[key]
        l , h = 0 , len(values)-1
        res = ""
        while l <= h :
            mid = (l + h )//2
            mv = values[mid][1]
            if mv <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                h = mid -1
        return res