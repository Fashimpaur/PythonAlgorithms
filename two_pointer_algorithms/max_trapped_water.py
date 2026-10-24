"""
Trapping Rain Water (Elevation Map)

Problem Description:
Given an array of non-negative integers representing an elevation map where
the width of each building / bar is 1, compute how much water it can trap after raining.

Physical Intuition & Core Principles:
- Water trapped at any column 'i' depends strictly on the bottleneck height between
  the tallest building to its left (left_max) and the tallest building to its right (right_max).
- Formula for column i:
    effective_water_level = min(left_max, right_max)
    trapped_water[i] = max(0, effective_water_level - height[i])
- Boundaries (index 0 and index n - 1) can never trap water because water spills off the edges.
- Total trapped water is the sum of trapped water across all columns.
"""


def max_trapped_water(heights: list[int]) -> int:
    """
    Calculates the maximum water trapped between buildings of various heights.

    Args:
        heights: A list of non-negative integers representing elevation / building heights.

    Returns:
        The total units of trapped rain water.

    Complexity Targets:
        - Optimal Time: O(n), where n is the number of buildings.
        - Space Efficiency:
            * O(1) auxiliary space using the Two-Pointer approach.
            * O(n) auxiliary space using Prefix/Suffix Max arrays or a Monotonic Stack.
    """
    # =========================================================================
    # STEP 1: Guard / Base Cases
    # =========================================================================
    # - If len(heights) < 3, can any concave depression exist to trap water?
    # - What should be returned immediately for empty or small inputs?
    # =========================================================================
    # STEP 2: Algorithmic Guidelines (Two-Pointer Technique)
    # =========================================================================
    # Why Two Pointers?
    # - Using two pointers ('left' at 0, 'right' at n - 1), we can eliminate the need
    #   for O(n) auxiliary space arrays for left_max and right_max.
    #
    # Core Invariant:
    # - Maintain 'left_max' (highest bar seen from 0 to left) and
    #   'right_max' (highest bar seen from right to n - 1
    # - At each step, compare 'left_max' and 'right_max':
    #     * If left_max <= right_max:
    #         - The water level at 'left' is strictly bounded by 'left_max' because
    #           we already know a wall at least as tall as 'right_max' exists to the right.
    #         - Add (left_max - heights[left]) to total water (if positive).
    #         - Increment 'left'.
    #     * Else (left_max > right_max):
    #         - The water level at 'right' is strictly bounded by 'right_max'.
    #         - Add (right_max - heights[right]) to total water (if positive).
    #         - Decrement 'right'.
    #
    # Termination:
    # - Continue while left < right (or left <= right).
    # =========================================================================
    # STEP 3: Alternative Paradigms (For Conceptual Comparison)
    # =========================================================================
    # - Approach A (Prefix & Suffix Max Arrays):
    #     Compute left_max[i] and right_max[i] in two O(n) passes, then iterate
    #     to sum min(left_max[i], right_max[i]) - heights[i]. (Time: O(n), Space: O(n))
    # - Approach B (Monotonic Stack):
    #     Maintain indices of decreasing heights. When encountering a taller bar,
    #     pop the valley bottom and compute horizontal water layers bounded by the
    #     current bar and the previous stack top. (Time: O(n), Space: O(n))

    if len(heights) < 3:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    max_volume = 0

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                max_volume += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                max_volume += right_max - heights[right]
            right -= 1

    return max_volume


if __name__ == "__main__":
    # Test cases covering edge, standard, and extreme scenarios
    test_cases = [
        # (heights, expected_output, scenario_description)
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, "Standard multi-valley profile"),
        ([4, 2, 0, 3, 2, 5], 9, "Deep central trough with outer high walls"),
        ([], 0, "Empty list"),
        ([5], 0, "Single building"),
        ([3, 4], 0, "Two buildings"),
        ([1, 2, 3, 4, 5], 0, "Strictly ascending profile"),
        ([5, 4, 3, 2, 1], 0, "Strictly descending profile"),
        ([3, 3, 3, 3], 0, "Uniform flat elevation"),
        ([3, 0, 3], 3, "Simple symmetric V-shape valley"),
        ([4, 1, 2, 1, 4], 8, "Stepped symmetrical bowl"),
        ([5, 1, 2, 1, 2], 2, "Asymmetrical boundaries constrained by shorter right wall"),
        ([2, 0, 0, 0, 2], 6, "Wide flat valley bottom"),
    ]

    for heights, expected, description in test_cases:
        result = max_trapped_water(heights)
        status = "Pass" if result == expected else "Fail"
        print(f"Test Case: {description} | Returned: {result} | Expected: {expected} | Status: {status}")
        assert result == expected, (
            f"Failed on [{description}] heights={heights}. Expected {expected}, got {result}"
        )

    print("\nAll test cases passed successfully!")