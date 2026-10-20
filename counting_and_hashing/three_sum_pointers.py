
from collections import Counter


def get_triplets(list_of_ints: list[int]) -> list[list[int]]:
    n = len(list_of_ints)

    # SPACE CHANGE: O(1) -> O(n)
    # A new sorted list is created so the original input remains unchanged.
    # TIME CHANGE: O(1) -> O(n log n)
    # Sorting n integers takes O(n log n) time.
    numbers = sorted(list_of_ints)

    # SPACE: O(1) initially; grows as results are appended.
    triplets = []

    # TIME CHANGE: O(n log n) -> O(n^2) overall
    # The outer loop runs O(n) times, and the inner scan takes O(n)
    # per iteration. Their combined worst-case cost is O(n^2).
    for i in range(n - 2):

        # EARLY EXIT:
        # Since numbers is sorted, if numbers[i] > 0, every remaining
        # number is positive. No zero-sum triplet is possible.
        # Practical runtime improves, but worst-case time remains O(n^2).
        if numbers[i] > 0:
            break

        # Skip duplicate starting values.
        # TIME: O(1) per check; avoids redundant scans in practice.
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        # EARLY SKIP:
        # If even the two largest remaining values cannot bring the sum
        # to zero, no triplet starting at numbers[i] can work.
        # This saves scans for some inputs; worst-case time remains O(n^2).
        if numbers[i] + numbers[n - 2] + numbers[n - 1] < 0:
            continue

        # SPACE: O(1) — only two pointers are stored.
        left, right = i + 1, n - 1

        # TIME: O(n) per outer iteration.
        # Each pointer moves only inward, so this loop does O(n) work
        # for each i. Combined with the outer loop: O(n^2).
        while left < right:
            # TIME: O(1) — three integer additions and comparisons.
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum == 0:
                # OUTPUT SPACE CHANGE:
                # Each appended triplet adds O(1) space.
                # With k results, output space is O(k), where k can be O(n^2).
                triplets.append([
                    numbers[i], numbers[left], numbers[right]
                ])

                # Skip duplicate left values.
                # O(n) total pointer movement across each inner scan,
                # not O(n) for every individual comparison.
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1

                # Skip duplicate right values.
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                # TIME: O(1) — advance left to increase the sum.
                left += 1
            else:
                # TIME: O(1) — advance right to decrease the sum.
                right -= 1

    # Return takes O(1) time; the returned result already occupies O(k) space.
    return triplets


def test_get_triplets():
    test_cases = [
        ([-1, 0, 3, 1, 2, -1, -4],
         [[-4, 1, 3], [-1, -1, 2], [-1, 0, 1]]),
        ([-1, 0, 1, 2, -1, -4],
         [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, 3, 4], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1], []),
        ([1, -1], []),
        ([2, 0, 0, 2, 2], []),
        ([-2, -1, 0, 1, 2, 3, -3],
         [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3],
          [-2, 0, 2], [-1, 0, 1]]),
    ]

    def normalize(triplets):
        return {tuple(sorted(t)) for t in triplets}

    for idx, (nums, expected) in enumerate(test_cases, start=1):
        original = list(nums)
        actual = get_triplets(nums)

        assert normalize(actual) == normalize(expected), (
            f"Case {idx} failed: {original} -> {actual} != {expected}"
        )

        assert all(sum(t) == 0 for t in actual), (
            f"Case {idx}: non-zero triplet found: {actual}"
        )

        assert len(actual) == len(normalize(actual)), (
            f"Case {idx}: duplicate triplets found: {actual}"
        )

        assert nums == original, f"Case {idx}: input was mutated"

        input_counts = Counter(nums)
        for t in actual:
            t_counts = Counter(t)
            for val, count in t_counts.items():
                assert count <= input_counts[val], (
                    f"Case {idx}: value {val} used {count} times, "
                    f"only {input_counts[val]} available"
                )

        if actual:
            print(f"Case {idx} PASSED | nums={nums} -> triplets found: {actual}")
        else:
            print(f"Case {idx} PASSED | nums={nums} -> no triplets found")

    print("All test_get_triplets cases passed")


RUN_TESTS = True

if __name__ == "__main__":
    if RUN_TESTS:
        test_get_triplets()
    else:
        sample = [-1, 0, 3, 1, 2, -1, -4]
        result = get_triplets(sample)
        print(f"Input: {sample}")
        print(f"Unique triplets that sum to zero: {result}")
