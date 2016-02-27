import heapq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x[0]) #sorts the given intervals based upon their starting time of the intervals
    heap = []  # stores the end time of intervals
    for i in intervals:
        print i
        if heap and i[0] >= heap[0]: 
            # means two intervals can use the same room even if their end and start time might match
            heapq.heapreplace(heap, i[1]) 
		#pops and returns the smallest item from the list, which basically
		#means that it pops the smallest end time,i.e., that particular meeting has 
		#ended and that the room can be allocated to the new meeting. 
		##It then adds the end time of the new meeting.
            #print i[1]
        else:
            # a new room is allocated
            heapq.heappush(heap, i[1]) 
		#if a meeting is already going, it assigns a new room to the meeting 
		#and thus adds the end time of that meeting to the heap.
            print i[1]
        print heap
        print '\n'
    #print heap
    return len(heap)

list = [[10,20],[5,10],[5,20],[0,5]]
print minMeetingRooms(list)

