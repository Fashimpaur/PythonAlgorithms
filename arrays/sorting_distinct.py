"""
Write a function that, given an array A consisting of N integers,
returns the number of distinct values of A.
"""


def solution(A: list[int]) -> int:
    return len(set(A))


if __name__ == '__main__':
    print(solution([2, 1, 1, 2, 3, 1]))  # 3
    print(solution([3, 3, 3, 3, 3, 3]))  # 1
    print(solution([1, 2, 3, 4, 5, 6]))  # 6
    print(solution([]))                  # 0
