"""
Write a function that, given a positive integer N, returns the length of its
smallest binary period. If no period exists, return -1.
"""

def solution(N: int) -> int:
    bits = [int(b) for b in bin(N)[2:]]  # binary digits as a list of ints
    l = len(bits)

    for p in range(1, l):
        if bits[:l - p] == bits[p:]:
            return p
    return -1


if __name__ == "__main__":
    print(solution(955))   # example test
    print(solution(21))    # binary 10101 -> period 2
    print(solution(42))    # binary 101010 -> period 2
    print(solution(7))     # binary 111 -> period 1
    print(solution(8))     # binary 1000 -> -1
