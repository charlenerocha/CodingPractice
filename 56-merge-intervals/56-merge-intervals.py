class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        final=[]
        
        for i in intervals:
            if not final or final[-1][1]<i[0]:
                final.append(i)
            else:
                final[-1][1]=max(i[1], final[-1][1])
            
        return final