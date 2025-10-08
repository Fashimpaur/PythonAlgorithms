"""
Problem: Find the GCD and LCM of Two Numbers

Write a function:

def solution(A: int, B: int) -> tuple[int, int]:
    pass

that, given two positive integers A and B, returns a tuple (G, L) where:

- G is the greatest common divisor (GCD) of A and B.
- L is the least common multiple (LCM) of A and B.

Example:

solution(15, 20)  # returns (5, 60)
solution(7, 5)    # returns (1, 35)
solution(21, 6)   # returns (3, 42)
solution(13, 13)  # returns (13, 13)

Assumptions:

- A and B are integers within the range [1..2,147,483,647].
- The function should return the correct answer efficiently, even for large values of A and B.
"""


import math


def gcd(a, b) -> int:
    while b:
        a, b = b, a % b
    return a


def solution(A: int, B: int) -> tuple[int, int]:
    G = gcd(A, B)
    L = (A * B) // G

    return G, L


def lib_solution(A: int, B: int) -> tuple[int, int]:
    return math.gcd(A, B), math.lcm(A, B)


if __name__ == '__main__':
    print("Pure code solution:\n")
    print(solution(15, 20))
    print(solution(7, 5))
    print(solution(21, 6))
    print(solution(13, 13))
    print("\nPython library solution:\n")
    print(lib_solution(15, 20))
    print(lib_solution(7, 5))
    print(lib_solution(21, 6))
    print(lib_solution(13, 13))
