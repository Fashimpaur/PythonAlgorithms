def insert_interval(intervals: list, insert_list: list) -> list:
    results = []
    i = 0
    n = len(intervals)
    new_interval = list(insert_list)

    while i < n and intervals[i][1] < new_interval[0]:
        results.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    results.append(new_interval)
    for j in range(i, n):
        results.append(intervals[j])
    return results


if __name__ == "__main__":
    test_cases = [
        # (description, intervals, insert_list, expected_output)
        ("1. Empty intervals list", [], [5, 7], [[5, 7]]),
        ("2. Insert before all existing intervals (no overlap)", [[3, 5], [6, 9]], [1, 2], [[1, 2], [3, 5], [6, 9]]),
        ("3. Insert after all existing intervals (no overlap)", [[1, 2], [3, 5]], [6, 8], [[1, 2], [3, 5], [6, 8]]),
        ("4. Insert in the middle between intervals (no overlap)", [[1, 2], [6, 7]], [3, 5], [[1, 2], [3, 5], [6, 7]]),
        ("5. Overlap with a single interval", [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ("6. Overlap spanning multiple intervals (LeetCode classic example)", [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ("7. Touching boundary at start/end points", [[1, 2], [3, 5]], [2, 3], [[1, 5]]),
        ("8. Touching endpoints bridging two intervals", [[1, 4], [5, 8]], [4, 5], [[1, 8]]),
        ("9. New interval completely covers all existing intervals", [[2, 3], [4, 5], [6, 7]], [1, 10], [[1, 10]]),
        ("10. Existing interval completely contains the new interval", [[1, 10]], [3, 5], [[1, 10]]),
        ("11. Exact duplicate interval", [[1, 5]], [1, 5], [[1, 5]]),
        ("12. Single point intervals", [[1, 1], [3, 3]], [2, 2], [[1, 1], [2, 2], [3, 3]]),
    ]

    for description, intervals, insert_list, expected in test_cases:
        result = insert_interval(intervals, insert_list)
        assert result == expected, (
            f"[{description}] intervals: {intervals}, insert_list: {insert_list} | "
            f"Expected: {expected}, Got: {result}"
        )
        print(f"Testing: {description}")
        print(f"  insert_interval({intervals}, {insert_list}) -> {result} (Passed)\n")

    print("All test cases passed successfully.")
