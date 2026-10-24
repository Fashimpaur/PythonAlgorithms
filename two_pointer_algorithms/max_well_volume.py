"""
Container With Most Water (Max Well Volume)

Problem Description:
Given an array of non-negative integers `heights` where each element represents 
the height of a vertical wall at index `i`, find two distinct walls that together 
with the x-axis enclose a container holding the maximum possible water volume.

Formula:
    Volume(i, j) = (j - i) * min(heights[i], heights[j])
"""


def max_well_volume(heights: list[int]) -> int:
    """Calculates the maximum water volume that can be contained between two walls.

    Args:
        heights: A list of non-negative integers representing the height of walls
          at each index.

    Returns:
        The maximum volume of water that can be enclosed between any pair of
        walls.

    Complexity Targets:
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    """
    pass


if __name__ == "__main__":
    test_cases = [
        # Format: (heights, expected_volume, scenario_description)
        (
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49,
            "Standard multi-wall configuration with optimal pair (index 1 to index 8)",
        ),
        ([1, 1], 1, "Minimal valid input of two identical short walls"),
        ([4, 3, 2, 1, 4], 16, "Symmetric outer tall walls spanning the full width"),
        ([1, 2, 1], 2, "Small peak where outermost pair yields maximum volume"),
        (
            [2, 3, 4, 5, 18, 17, 6],
            17,
            "Narrow tall interior peaks (indices 4 and 5) outperforming wider shorter boundaries",
        ),
        (
            [10, 1, 1, 1, 1, 1, 1, 1, 10],
            80,
            "Deep wide basin with tall outer walls and flat shallow floor",
        ),
        ([5, 4, 3, 2, 1], 6, "Strictly monotonically decreasing wall heights"),
        ([1, 2, 3, 4, 5], 6, "Strictly monotonically increasing wall heights"),
        ([4, 4, 4, 4], 12, "Uniform flat heights spanning maximum available width"),
        (
            [1, 100, 100, 1],
            100,
            "Interior tall container dominating low outer boundaries",
        ),
        ([0, 2], 0, "Boundary containing a zero-height wall"),
        ([5], 0, "Edge Case: Single wall cannot enclose water"),
        ([], 0, "Edge Case: Empty array"),
    ]

    for heights, expected, description in test_cases:
        result = max_well_volume(heights)
        status = "Pass" if result == expected else "Fail"
        print(f"[{status}] {description} | Expected: {expected} | Got: {result}")
