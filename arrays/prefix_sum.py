"""
Write a function that, given a non-empty string S consisting of N characters
and two non-empty arrays P and Q consisting of M integers, returns an array
consisting of M integers specifying the consecutive answers to all queries.
"""


def solution(S: str, P: list[int], Q: list[int]) -> list[int]:
    N = len(S)
    M = len(P)

    # initialize prefix sum arrays
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)
    prefix_T = [0] * (N + 1)

    for i in range(N):  # for every character in the sequence
        prefix_A[i + 1] = prefix_A[i] + (1 if S[i] == "A" else 0)
        prefix_C[i + 1] = prefix_C[i] + (1 if S[i] == "C" else 0)
        prefix_G[i + 1] = prefix_G[i] + (1 if S[i] == "G" else 0)
        prefix_T[i + 1] = prefix_T[i] + (1 if S[i] == "T" else 0)

    result = []

    # Now keep running count of each prefix
    for i in range(M):
        start, end = P[i], Q[i] + 1
        if prefix_A[end] - prefix_A[start] > 0:
            result.append(1)
        elif prefix_C[end] - prefix_C[start] > 0:
            result.append(2)
        elif prefix_G[end] - prefix_G[start] > 0:
            result.append(3)
        else:
            result.append(4)

    return result


if __name__ == '__main__':
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    print(solution(S, P, Q))  # [2, 4, 1]
