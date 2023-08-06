'''
Given an array of meeting time intervals consisting of start 
and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a 
person could attend all meetings.
'''

def canAttendMeetings(intervals):

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
            return False 
        
    return True 

# Just checking if the previous meeting ends before the current meeting starts.
# Return true if this ever happens, else return False 


# Space | Time: O(n log(n)) | O(1)

