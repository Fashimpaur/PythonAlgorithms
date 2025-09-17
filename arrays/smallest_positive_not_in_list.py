"""
Write a function that, given a list A of N integers,
returns the smallest positive integer (greater than 0)
that does not occur in A
"""
def solution_1(A: list[int]) -> int:
    positives = {x for x in A if x > 0}

    for i in range(1, len(A) + 2):
        if i not in positives:
            return i


def solution(A: list[int]) -> int:
    n = len(A)

    # Step 1: rearrange numbers in-place
    i = 0
    while i < n:
        correct_pos = A[i] - 1
        if 1 <= A[i] <= n and A[i] != A[correct_pos]:
            # swap A[i] into the correct place
            A[i], A[correct_pos] = A[correct_pos], A[i]
        else:
            i += 1

    # Step 2: find first place where value != index+1
    for i in range(n):
        if A[i] != i + 1:
            return i + 1

    # Step 3: if all are in place
    return n + 1


if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))
    print(solution([2]))  # 1
    print(solution([1]))  # 2
    print(solution([1, 2, 4, 5]))  # 3

