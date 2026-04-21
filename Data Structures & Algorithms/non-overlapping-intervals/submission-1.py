class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        remove = 0 
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)): 
            start = intervals[i][0]
            end = intervals[i][1]

            if start >= prev_end: 
                prev_end = end 
            else: 
                remove += 1
                prev_end = min(prev_end, end)
        return remove