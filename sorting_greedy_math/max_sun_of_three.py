#!/usr/bin/python3
"""
A non-empty array A consisting of N integers is given.

The goal is to find the maximal sum of any 3 consecutive integers.

Write a function:

    def solution(A):

that, given a non-empty array A, returns the value of the maximal sum
of 3 consecutive integers.

For example, given an array A such that:

    A[0] = -3
    A[1] = 1
    A[2] = 2
    A[3] = -2
    A[4] = 5
    A[5] = 6

the function should return 9, because:
    - (A[0] + A[1] + A[2]) = -3 + 1 + 2 = 0
    - (A[1] + A[2] + A[3]) = 1 + 2 + (-2) = 1
    - (A[2] + A[3] + A[4]) = 2 + (-2) + 5 = 5
    - (A[3] + A[4] + A[5]) = -2 + 5 + 6 = 9
and no other combination of 3 consecutive integers gives a higher sum.

Write an efficient algorithm for the following assumptions:
    - N is an integer within the range [3..100,000];
    - Each element of array A is an integer within the range [-1,000..1,000].
"""


from typing import Optional

def solution(A: list[int]) -> Optional[int]:
    """
    Find the maximum sum of 3 consecutive integers in an array using a sliding window.

    Time complexity: O(N), where N is the number of elements in array A,
                     as we iterate through the array once.
    Space complexity: O(1), as we use a fixed number of variables.

    :param A: List of integers
    :return: The maximum sum of 3 consecutive integers, or None if array has fewer than 3 elements
    """
    if len(A) < 3:
        print(f"Array A={A} must have at least 3 elements.")
        return None

    # O(1) initialization
    current_sum = sum(A[:3])
    max_sum = current_sum

    # O(N) loop
    for i in range(3, len(A)):
        # Sliding window update: subtract the element exiting, add the element entering
        current_sum = current_sum - A[i-3] + A[i]
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    """
    Test the sliding window solution with various test cases.
    """
    param_list = [
        ([1, 2, 3], 6),
        ([-3, 1, 2, -2, 5, 6], 9),
        ([-5, 5, -5, 4], 4),
        ([-3, -2, -1, 0, 1, 2, 3], 6),
        ([-5, -3, -1], -9),
        ([-5, -3, 0], -8),
        ([-10, -10, 5, 2], -3),
        ([0, 0, 0, 0], 0),
        ([10, 10, 10], 30),
        ([-1, -2, -3, -4, -5, 0], -6),
        ([1, 2], None),
    ]
    for param, expected in param_list:
        result = solution(param)
        assert result == expected, f"Failed for {param}: expected {expected}, got {result}"
        print(f"Passed: {param} -> {result}")


if __name__ == "__main__":
    main()

# Final Assessment:
# The sliding window technique provides an efficient O(N) time complexity solution
# to find the maximum sum of 3 consecutive integers, which is optimal for this problem.
# The space complexity is O(1), making it very memory-efficient.
