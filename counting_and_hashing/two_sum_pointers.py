"""
A non-empty array A of N integers and an integer T are given.

Your goal is to find two distinct indices i and j such that:
    A[i] + A[j] = T.

Return the indices [i, j] in increasing order (i < j).
If no such pair exists, return (False, -1, -1).

Write a function:

    def solution(list_of_ints: list[int], target_sum: int) -> tuple[bool, int, int]

that, given an array A of N integers and an integer T, returns a tuple containing
a boolean indicating if the pair was found, and the pair of indices (i, j) 
as described above, or (False, -1, -1) if no such pair exists.

For example, given T = 9 and array A such that:
    A = [2, 7, 11, 15]
the function should return (True, 0, 1), since A[0] + A[1] = 2 + 7 = 9.

Given T = 6 and array A such that:
    A = [3, 2, 4]
(Note: Input array should be sorted for two-pointer approach, e.g., A = [2, 3, 4])
the function should return (True, 1, 2), since A[1] + A[2] = 2 + 4 = 6.

---

### Assumptions:
- N is an integer within the range [2..100,000].
- Each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
- T is an integer within the range [−1,000,000,000..1,000,000,000].
- At most one valid pair of indices exists.
- The input array A must be sorted for the two-pointer approach to work.

---

### Goal:
Design an **efficient algorithm**.
The current solution uses two pointers for O(N) time and O(1) space.

"""


def solution(list_of_ints: list[int], target_sum: int) -> tuple[bool, int, int] | None:
    left, right = 0, len(list_of_ints) - 1
    while left < right:
        current_sum = list_of_ints[left] + list_of_ints[right]
        if current_sum == target_sum:
            return True, left, right
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return False, -1, -1


if __name__ == "__main__":
    print(solution([2, 7, 11, 15], 6))  # [-1, -1]
    print(solution([2, 7, 11, 15], 9))  # [0, 1]
    print(solution([3, 2, 4, 1], 6))  # [1, 2]
    import timeit
    time_taken = timeit.timeit(
            lambda: print(solution([i for i in range(-1000000, 1000001)], 1999999)),
            number=1
    )
    print(time_taken)
