class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        # dp[i] the non-overlapping intervals from intervals[0]-intervals[i]
        dp = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            last_interval = dp[-1]
            
            # case 1: curr is entirely in last (curr.finish <= last.finish)
            if (curr_interval[1] <= last_interval[1]):
                continue
            # case 2: curr and last overlap (curr.start <= last.finish)
            elif (curr_interval[0] <= last_interval[1]):
                dp[-1][1] = curr_interval[1]
            
            # case 3: both disjoint (curr.start < last.finish)
            else:
                dp.append(curr_interval)
            
        return dp