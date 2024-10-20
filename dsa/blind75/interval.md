Here are the solutions to the interval problems you've requested using Python:

---

### 1. **Insert Interval**

You are given a set of non-overlapping intervals sorted by their start time, and you need to insert a new interval into the list of intervals, merging if necessary.

#### Solution

We can iterate over the list of intervals, insert the new interval at the correct position, and then merge any overlapping intervals.

```python
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # Step 1: Add all intervals that come before the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    # Add the merged interval
    result.append(new_interval)
    
    # Step 3: Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result
```

---

### 2. **Merge Intervals**

Given a collection of intervals, merge all overlapping intervals.

#### Solution

To merge intervals, first sort the intervals by their start time. Then, iterate through the sorted list and merge overlapping intervals.

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        # If the current interval overlaps with the last merged one, merge them
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    
    return merged
```

---

### 3. **Non-overlapping Intervals**

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#### Solution

This is a classic "greedy interval scheduling" problem. We want to minimize the number of intervals removed by keeping as many non-overlapping intervals as possible.

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    # Sort by end time to facilitate the greedy approach
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the count of non-overlapping intervals
    count = 1
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    
    # The number of intervals to remove is the total intervals minus non-overlapping intervals
    return len(intervals) - count
```

---

### 4. **Meeting Rooms (Leetcode Premium)**

Given an array of meeting time intervals where `intervals[i] = [start, end]`, determine if a person could attend all meetings.

#### Solution

To check if a person can attend all meetings, we need to verify if there are any overlapping intervals. We can do this by sorting intervals based on start time and checking for any overlap between consecutive intervals.

```python
def can_attend_meetings(intervals):
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # Overlap
            return False
    
    return True
```

---

### 5. **Meeting Rooms II (Leetcode Premium)**

Given an array of meeting time intervals where `intervals[i] = [start, end]`, find the minimum number of conference rooms required.

#### Solution

This problem can be solved using a min-heap (or priority queue). The idea is to track the end time of meetings that are currently ongoing. Every time a new meeting starts, you check if a room is freed up.

```python
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min-heap to track end times of ongoing meetings
    heap = []
    
    # Add the first meeting's end time
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # If the room is free (the meeting with the earliest end time is over)
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        
        # Add the current meeting's end time to the heap
        heapq.heappush(heap, intervals[i][1])
    
    # The size of the heap will tell us the minimum number of rooms needed
    return len(heap)
```

---

Each of these problems can be optimized further depending on the constraints and use case, but these solutions provide a good balance of simplicity and efficiency. Let me know if you'd like to dive deeper into any specific problem!