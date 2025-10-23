"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12,
24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


def solution(N: int) -> tuple[int, list[int]]:
    small_factors = []
    large_factors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            small_factors.append(i)
            if i != N // i:
                large_factors.append(N // i)
        i += 1

    factors_list = small_factors + large_factors[::-1]
    return len(factors_list), factors_list


if __name__ == "__main__":
    test_values = [1, 2, 4, 9, 24, 36, 100, 2147483647]
    for i in test_values:
        result = solution(i)
        print(
            f"There are {result[0]} factors in {i} and they are:\n{result[1]}\n"
        )
