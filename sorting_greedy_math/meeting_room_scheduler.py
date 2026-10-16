#!/usr/bin/python3
"""
Meeting Room Scheduler

This module provides a solution to the meeting room scheduling problem.
Given a list of meeting intervals, it determines the minimum number of meeting
rooms required to schedule all meetings without overlap.

The problem

You are given a list of meeting intervals, where each interval is represented by
a start time and an end time.

Your task is to determine the minimum number of meeting rooms required so that
every meeting can take place without overlapping with another meeting in the same room.

Each meeting is represented as:
[start, end]

For example, [9, 12] means a meeting starts at 9:00 and ends at 12:00.

Example 1
Input:

intervals = [[9, 12], [10, 13], [12, 14], [13, 15]]
expected_result = 3

Explanation:
- Meeting [9, 12] overlaps with [10, 13].
- Meeting [12, 14] can use the room freed by [9, 12], since the first meeting
  ends exactly when the next one starts.
- Meeting [13, 15] overlaps with [12, 14].

One possible schedule:
Room 1
9–12 | 12–14

Room 2
10–13 | 13–15

Two rooms are enough, and one room is not enough because two meetings
overlap between 10:00 and 12:00.

Example 2
Input:

intervals = [[1, 5], [2, 4], [3, 6], [7, 9]]
expected_result = 3

Explanation:
- Meeting [1, 5] overlaps with [2, 4].
- Meeting [2, 4] can use the room freed by [1, 5], since the first meeting
  ends exactly when the next one starts.
- Meeting [3, 6] overlaps with [2, 4].
- Meeting [7, 9] does not overlap with any previous meetings.

At time 3, the first three meetings are all active, so at least three rooms are
necessary.

Your task
Write a Python function called min_meeting_rooms(intervals) that returns the minimum number of rooms required.

Constraints
- 1 <= len(intervals) <= 10**5
- 0 <= start < end <= 10**6
- Intervals may be given in any order.
- If one meeting ends at the exact time another starts, they can use the same
  room.

Challenge requirements:
- Aim for an (O(n log n) time complexity.
- Do not use any external libraries.
- Try solving it before looking up a solution.

"""


def min_meeting_rooms(intervals):
    """
    Calculates the minimum number of meeting rooms required for the given intervals.

    Time complexity: O(N log N), where N is the number of intervals, due to sorting.
    Space complexity: O(N) to store the start and end times.

    :param intervals: List of meeting intervals, e.g., [[start, end], ...]
    :return: Minimum number of rooms required
    """
    if not intervals:
        return 0
    
    # O(N) space to store start and end times
    starts = [i[0] for i in intervals]
    # O(N log N) time to sort starts
    starts.sort()
    ends = [i[1] for i in intervals]
    # O(N log N) time to sort ends
    ends.sort()
    
    start_pointer = 0
    end_pointer = 0
    rooms = 0
    max_rooms = 0
    
    # O(N) time to iterate through intervals
    while start_pointer < len(intervals):
        if starts[start_pointer] < ends[end_pointer]:
            rooms += 1
            start_pointer += 1
        else:
            rooms -= 1
            end_pointer += 1
        max_rooms = max(max_rooms, rooms)
        
    return max_rooms


def main():
    """
    Test the min_meeting_rooms solution with predefined test cases.
    """
    test_cases = [
        ([[9, 12], [10, 13], [12, 14], [13, 15]], 2),
        ([[1, 5], [2, 4], [3, 6], [7, 9]], 3),
        ([[1, 2], [2, 3], [3, 4]], 1),
        ([[1, 10], [2, 5], [6, 9]], 2),
        ([], 0),
    ]
    for intervals, expected in test_cases:
        result = min_meeting_rooms(intervals)
        assert result == expected, f"Failed for {intervals}: expected {expected}, got {result}"
        print(f"Passed: {intervals} -> {result}")


if __name__ == "__main__":
    main()

# Final Assessment:
# Time Complexity: O(N log N), where N is the number of intervals. This is
# dominated by the sorting of the 'starts' and 'ends' lists, which are each
# O(N log N). The subsequent iteration through the sorted lists is O(N).

# Space Complexity: O(N), because we store the start and end times in two
# separate lists, each of size N.
