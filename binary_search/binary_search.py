def binary_search(nums: list[int], target: int, return_steps: bool = False) -> bool | tuple[bool, int]:
    left, right = 0, len(nums) - 1
    steps = 0
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if nums[mid] == target:
            return (True, steps) if return_steps else True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return (False, steps) if return_steps else False


if __name__ == "__main__":
    test_cases = [
        # (nums, target, expected_found, expected_steps, description)
        ([1, 3, 5, 7, 9], 5, True, 1, "Target in the middle of odd-length list"),
        ([1, 3, 5, 7, 9], 1, True, 2, "Target at the first position"),
        ([1, 3, 5, 7, 9], 9, True, 3, "Target at the last position"),
        ([2, 4, 6, 8], 6, True, 2, "Target in even-length list"),
        ([2, 4, 6, 8], 2, True, 2, "Target at beginning of even-length list"),
        ([2, 4, 6, 8], 8, True, 3, "Target at end of even-length list"),
        ([5], 5, True, 1, "Single element list - target found"),
        ([5], 3, False, 1, "Single element list - target not found"),
        ([], 1, False, 0, "Empty list"),
        ([10, 20, 30, 40], 5, False, 2, "Target smaller than all elements"),
        ([10, 20, 30, 40], 50, False, 3, "Target larger than all elements"),
        ([1, 3, 5, 7, 9], 4, False, 3, "Target absent between elements"),
        ([-10, -5, 0, 3, 8], -5, True, 3, "List with negative numbers - target found"),
        ([-10, -5, 0, 3, 8], -1, False, 3, "List with negative numbers - target absent"),
        ([1, 2, 2, 2, 3, 4], 2, True, 1, "List with duplicate values - target found"),
        (list(range(0, 1000, 2)), 500, True, 8, "Large list - target present"),
        (list(range(0, 1000, 2)), 501, False, 9, "Large list - target absent"),
    ]

    all_passed = True
    for nums, target, expected_found, expected_steps, desc in test_cases:
        found, steps = binary_search(nums, target, return_steps=True)
        status = "PASSED" if (found == expected_found and steps == expected_steps) else "FAILED"
        if found != expected_found or steps != expected_steps:
            all_passed = False
        nums_repr = nums if len(nums) <= 10 else f"list of length {len(nums)}"
        print(
            f"[{status}] {desc}\n"
            f"  - Input: nums={nums_repr}, target={target}\n"
            f"  - Result: found={found} in {steps} step(s) (Expected: found={expected_found} in {expected_steps} step(s))\n"
        )
        assert found == expected_found, f"Failed found assertion on test: {desc}"
        assert steps == expected_steps, f"Failed steps assertion on test: {desc}"

    if all_passed:
        print("All test cases passed successfully with step counts verified!")