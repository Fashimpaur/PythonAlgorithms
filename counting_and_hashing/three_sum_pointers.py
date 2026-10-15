from collections import Counter


def get_triplets(list_of_ints: list[int]) -> list[list[int]]:
    numbers = sorted(list_of_ints)
    triplets = []

    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue  # skip duplicates
        left, right = i + 1, len(numbers) - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum == 0:
                triplets.append([numbers[i], numbers[left], numbers[right]])

                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


def test_get_triplets():
    test_cases = [
        ([-1, 0, 3, 1, 2, -1, -4], [[-4, 1, 3], [-1, -1, 2], [-1, 0, 1]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, 3, 4], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1], []),
        ([1, -1], []),
        ([2, 0, 0, 2, 2], []),
        ([-2, -1, 0, 1, 2, 3, -3], [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ]

    def normalize(triplets):
        return {tuple(sorted(t)) for t in triplets}

    for idx, (nums, expected) in enumerate(test_cases, start=1):
        original = list(nums)
        actual = get_triplets(nums)

        assert normalize(actual) == normalize(expected), (
            f"Case {idx} failed: {original} -> {actual} != {expected}\n"
        )

        assert all(sum(t) == 0 for t in actual), f"Case {idx}: non-zero triplet found: {actual}\n"

        assert len(actual) == len(normalize(actual)), f"Case {idx}: duplicate triplets found: {actual}"

        assert nums == original, (f"Case {idx}: input was mutated")

        input_counts = Counter(nums)
        for t in actual:
            t_counts = Counter(t)
            for val, count in t_counts.items():
                assert count <= input_counts[val], (f"Case {idx}: value {val} used {count} times, only "
                                                    f"{input_counts[val]} available")

        if actual:
            print(f"Case {idx} PASSED | nums={nums} -> triplets found: {actual}")
        else:
            print(f"Case {idx} PASSED | nums={nums} -> no triplets found")

        print("All test_get_triplets cases passed")

RUN_TESTS = True

if __name__ == '__main__':
    if RUN_TESTS:
        test_get_triplets()
    else:
        sample = [-1,0,3,1,2,-1,-4]
        result = get_triplets(sample)
        print(f"Input: {sample}")
        print(f"Unique triplets that were sum to zero: {result}")
