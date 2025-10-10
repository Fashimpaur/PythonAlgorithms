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
"""
