'''
This is same a merging intervals question, just a new interval is present here
'''


def newIntervals(self,intervals,newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key = lambda x:x[0])

    i = 0
    while i<len(intervals)-1:
        if intervals[i][-1]>=intervals[i+1][0]:
            intervals[i][-1] = max(intervals[i][-1],intervals[i+1][-1])
            del intervals[i+1]
        else:
            i+=1
    return intervals

    
