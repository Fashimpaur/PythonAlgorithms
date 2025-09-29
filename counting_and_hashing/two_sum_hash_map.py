"""
A non-empty array A of N integers and an integer T are given.

Your goal is to find two distinct indices i and j such that:
    A[i] + A[j] = T.

Return the indices [i, j] in increasing order (i < j).
If no such pair exists, return [-1, -1].

Write a function:

    def solution(A: list[int], T: int) -> list[int]

that, given an array A of N integers and an integer T, returns the pair of indices
as described above.

For example, given T = 9 and array A such that:
    A = [2, 7, 11, 15]
the function should return [0, 1], since A[0] + A[1] = 2 + 7 = 9.

Given T = 6 and array A such that:
    A = [3, 2, 4]
the function should return [1, 2], since A[1] + A[2] = 2 + 4 = 6.

Given T = 6 and array A such that:
    A = [3, 3]
the function should return [0, 1].

---

### Assumptions:
- N is an integer within the range [2..100,000].
- Each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
- T is an integer within the range [−1,000,000,000..1,000,000,000].
- At most one valid pair of indices exists.

---

### Goal:
Design an **efficient algorithm**.
Brute-force O(N²) will not pass when N = 100,000.
The expected solution uses a hash map for O(N) time and O(N) space.

"""


def solution(A: list[int], T: int) -> list[int]:
    checked = {}
    for i, number in enumerate(A):
        other_number = T - number
        if other_number in checked:
            return [checked[other_number], i]
        checked[number] = i
    return []


if __name__ == "__main__":
    print(solution([2, 7, 11, 15], 6))  # []
    print(solution([2, 7, 11, 15], 9))  # [0, 1]
    print(solution([3, 2, 4, 1], 6))  # [1, 2]
