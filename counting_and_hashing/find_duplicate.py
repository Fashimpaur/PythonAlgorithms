"""
Given a non-empty array of integers with values 1-100000, return an array of all its duplicate numbers.

Example 1:
Input: [4, 1, 3, 2] the output should be [] because no numbers are duplicates.
Example 2:
Input: [1, 3, 6, 4, 1, 2] the output should be [1] because 1 appears twice in the array.
Example 3:
Input: [1, 3, 2, 4, 3, 4] the output should be [3, 4] because both 3 and 4 appear twice.
"""
from collections import Counter


def solution(A: list[int]) -> list[int]:
    C = Counter(A)
    return [c for c,_ in C.items() if C[c] > 1]


if __name__ == '__main__':
    print(solution([4, 1, 3, 2]))  # []
    print(solution([1, 3, 6, 4, 1, 2]))  # [1]
    print(solution([1]))  # []
    print(solution([1, 3, 2, 4, 3, 4]))  # [3, 4]
