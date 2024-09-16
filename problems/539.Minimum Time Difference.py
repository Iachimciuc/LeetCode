class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        s = set()
        def transform(i):
            t = i.split(":")
            return int(t[0])*60 + int(t[1])
        
        points = []
        for i in timePoints:
            p = transform(i)
            if p in s:
                return 0
            s.add(p)
            points.append(transform(i))
        points.sort()
        m = 24*60 - points[-1] + points[0]
        for i in range(len(points)-1):
            m = min(m, points[i+1]-points[i])
        return m