"""
Container With Most Water (Max Well Volume)

Problem Description:
Given an array of non-negative integers `heights` where each element represents 
the height of a vertical wall at index `i`, find two distinct walls at indices `i` 
and `j` (with `i < j`) that together enclose a container (well) holding the maximum 
possible water volume.

Well Formation Rules:
For two walls at indices `i` and `j` (`i < j`) to form a valid well:
1. There must be at least one position between the two walls (i.e., `j - i >= 2`).
2. There must be a depression between the walls:
   - There must be a zero between the two walls (i.e., `0 in heights[i+1:j]`), OR
   - Every wall between them must be strictly less than both the left and right wall heights
     (i.e., `heights[k] < heights[i]` and `heights[k] < heights[j]` for all `i < k < j`).

If either of those conditions is not met (e.g., adjacent walls with no space between, 
or an intermediate wall greater than or equal to either bounding wall without a zero), 
the pair cannot form a well and can hold no water (volume = 0).

Formula for a valid well:
    Volume(i, j) = (j - i) * min(heights[i], heights[j])
"""


def max_well_volume(heights: list[int]) -> int:
    """Calculates the maximum water volume that can be contained between two walls.

    For two walls at indices `i` and `j` (`i < j`) to form a well, there must be
    space between them (`j - i >= 2`) and either there must be a zero between them
    or all walls between them must be strictly less than both bounding heights.
    If no valid well exists, 0 is returned.

    Args:
        heights: A list of non-negative integers representing the height of walls
          at each index.

    Returns:
        The maximum volume of water that can be enclosed between any pair of
        valid well walls.

    Complexity Targets:
        - Time Complexity: O(n^2) checking all candidate pairs with O(1) interval tracking
        - Space Complexity: O(1) auxiliary space
    """
    n = len(heights)
    if n < 3:
        return 0

    max_volume = 0


    return max_volume


if __name__ == "__main__":
    test_cases = [
        # Format: (heights, expected_volume, scenario_description)
        (
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            40,
            "Multi-wall configuration with optimal valid well between index 1 and index 6 (span 5, height 8)",
        ),
        (
            [4, 3, 2, 1, 4],
            16,
            "Symmetric outer tall walls with strictly lower interior walls spanning full width",
        ),
        (
            [10, 1, 1, 1, 1, 1, 1, 1, 10],
            80,
            "Deep wide basin with tall outer walls and flat shallow floor (all interior < 10)",
        ),
        (
            [3, 0, 3],
            6,
            "Simple symmetric well with zero at the bottom",
        ),
        (
            [4, 2, 4],
            8,
            "Well with intermediate wall strictly less than left and right boundaries",
        ),
        (
            [2, 0, 0, 0, 2],
            8,
            "Wide well with zeros between the outer walls",
        ),
        (
            [3, 5, 0, 5, 3],
            12,
            "Outer walls enclose zero in interior despite intermediate tall walls",
        ),
        (
            [1, 1],
            0,
            "Invalid well: Adjacent walls with no space/wall between",
        ),
        (
            [1, 2, 1],
            0,
            "Invalid well: Peak in the middle is taller than both outer walls and no zero exists",
        ),
        (
            [4, 4, 4, 4],
            0,
            "Invalid well: Flat uniform heights where intermediate walls equal boundary heights",
        ),
        (
            [5, 4, 3, 2, 1],
            0,
            "Invalid well: Strictly monotonically decreasing wall heights",
        ),
        (
            [1, 2, 3, 4, 5],
            0,
            "Invalid well: Strictly monotonically increasing wall heights",
        ),
        (
            [1, 100, 100, 1],
            0,
            "Invalid well: Tall interior plateau prevents outer walls from forming well, inner walls adjacent",
        ),
        ([0, 2], 0, "Edge Case: Two walls with one zero boundary cannot form a well"),
        ([5], 0, "Edge Case: Single wall cannot enclose water"),
        ([], 0, "Edge Case: Empty array"),
    ]

    for heights, expected, description in test_cases:
        result = max_well_volume(heights)
        status = "Pass" if result == expected else "Fail"
        print(f"[{status}] {description} | Expected: {expected} | Got: {result}")
        assert result == expected, (
            f"Failed on [{description}] heights={heights}. Expected {expected}, got {result}"
        )

    print("\nAll test cases passed successfully!")
