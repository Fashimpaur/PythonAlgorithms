"""
A non-empty array A consisting of N integers is given.

The product of triplet (P, Q, R) is A[P] * A[Q] * A[R]
(for 0 ≤ P < Q < R < N).

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A):

that, given a non-empty array A, returns the value of the maximal product
of any triplet.

For example, given array A such that:

    A[0] = -3
    A[1] = 1
    A[2] = 2
    A[3] = -2
    A[4] = 5
    A[5] = 6

the function should return 60, because:
    - (A[1] * A[4] * A[5]) = 1 * 5 * 6 = 30
    - (A[2] * A[4] * A[5]) = 2 * 5 * 6 = 60
    - (A[0] * A[4] * A[5]) = -3 * 5 * 6 = -90
and no other combination gives a higher product.

Write an efficient algorithm for the following assumptions:
    - N is an integer within the range [3..100,000];
    - Each element of array A is an integer within the range [-1,000..1,000].

Test cases:
| #  | Input Array `A`            | Expected Output |
| -- | -------------------------- | --------------- |
| 1  | `[1, 2, 3]`                | `6`             |
| 2  | `[-3, 1, 2, -2, 5, 6]`     | `60`            |
| 3  | `[-5, 5, -5, 4]`           | `125`           |
| 4  | `[-3, -2, -1, 0, 1, 2, 3]` | `18`            |
| 5  | `[-5, -3, -1]`             | `-15`           |
| 6  | `[-5, -3, 0]`              | `0`             |
| 7  | `[-10, -10, 5, 2]`         | `500`           |
| 8  | `[0, 0, 0, 0]`             | `0`             |
| 9  | `[10, 10, 10]`             | `1000`          |
| 10 | `[-1, -2, -3, -4, -5, 0]`  | `0`             |

"""


def solution(A: list[int]) -> int:
    """
    Find the solution for the maximum product of three integers contained in an array
    :param A: List of integers
    :return: Calculated maximum product
    """

    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")

    for a in A:
        # max numbers being the positive and max1 being the greatest positive integer
        if a > max1:
            max2, max3 = max1, max2
            max1 = a
        elif a > max2:
            max3 = max2
            max2 = a
        elif a > max3:
            max3 = a

        # min numbers being the negative numbers with min2 being the most negative number
        if a < min1:
            min2 = min1
            min1 = a
        elif a < min2:
            min2 = a

    return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == "__main__":
    param_list = [
        [1, 2, 3],
        [-3, 1, 2, -2, 5, 6],
        [-5, 5, -5, 4],
        [-3, -2, -1, 0, 1, 2, 3],
        [-5, -3, -1],
        [-5, -3, 0],
        [-10, -10, 5, 2],
        [0, 0, 0, 0],
        [10, 10, 10],
        [-1, -2, -3, -4, -5, 0],
    ]
    for param in param_list:
        print(solution(param))
        print()
