"""
Write a function that given an array A consisting of N integers and an integer K,
returns the array A rotated K times
"""


def solution(A: list[int], K: int):
    n = len(A) if A is not None else 0
    if not A or n > 100:
        return A

    K_normalized = K % n
    if K_normalized == 0:
        return A

    return A[-K_normalized:] + A[:-K_normalized]


if __name__ == "__main__":
    print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6], -3))  # [9, 7, 6, 3, 8]
    print(solution([1, 2, 3, 4], 4))  # [1, 2, 3, 4]
    print(solution([1, 2, 3, 4], -4))  # [1, 2, 3, 4]
    print(solution([1], 10))  # [1]
    print(solution([1], -10))  # [1]
    print(solution([0, 0, 0], 1))  # [0, 0, 0]
    print(solution([0, 0, 0], -1))  # [0, 0, 0]
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -3))
