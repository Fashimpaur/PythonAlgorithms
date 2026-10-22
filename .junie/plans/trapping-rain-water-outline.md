---
sessionId: session-261022-155509-16dh
---

# Requirements

### Overview & Goals
Establish a clean, spoiler-free algorithmic template and instructional guide for calculating the maximum water trapped by buildings of various heights (Trapping Rain Water). The instructions, mathematical intuition, algorithmic guidelines, and test cases will be placed directly as structured comments and docstrings in `two_pointer_algorithms/max_trapped_water.py`.

### Scope
- **In Scope**:
  - Creation of a new Python package `two_pointer_algorithms` under the project root (`two_pointer_algorithms/__init__.py` and `two_pointer_algorithms/max_trapped_water.py`).
  - Embedding comprehensive problem guidelines, physical intuitions, guiding questions, and complexity targets as comments and docstrings in `max_trapped_water.py` without revealing the code solution.
  - Test suite with expected numerical outputs covering typical, extreme, and degenerate cases in the `if __name__ == "__main__":` block.
- **Out of Scope**:
  - Writing the completed algorithm implementation (leaving a clean `pass` / `TODO` for the user).

### Problem Formulation
Given an array of non-negative integers representing an elevation map where the width of each building/bar is `1`, compute how much water it can trap after raining.

#### Mathematical Foundation
For any given building at index `i`:
- The water level above index `i` is bounded by the tallest building to its left (`left_max`) and the tallest building to its right (`right_max`).
- Effective water level: `min(left_max, right_max)`
- Trapped water at index `i`: `max(0, min(left_max, right_max) - height[i])`
- Total water trapped is the sum of trapped water across all indices.

### Test Cases & Expected Results

| Category | Input (`heights`) | Expected Output | Explanation |
| :--- | :--- | :--- | :--- |
| **Standard Example 1** | `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]` | `6` | Classic multi-valley profile trapping water between peaks. |
| **Standard Example 2** | `[4, 2, 0, 3, 2, 5]` | `9` | Deep central trough bounded by outer tall walls. |
| **Empty / Trivial** | `[]` | `0` | No buildings available to contain water. |
| **Single Building** | `[5]` | `0` | Cannot form a container with fewer than 3 buildings. |
| **Two Buildings** | `[3, 4]` | `0` | Water spills off outer boundaries. |
| **Strictly Ascending** | `[1, 2, 3, 4, 5]` | `0` | Water runs off to the left; no depression formed. |
| **Strictly Descending** | `[5, 4, 3, 2, 1]` | `0` | Water runs off to the right; no depression formed. |
| **Uniform Flat** | `[3, 3, 3, 3]` | `0` | Flat surface without depressions cannot trap water. |
| **Simple V-Shape** | `[3, 0, 3]` | `3` | Valley of depth 3 and width 1 traps `3 * 1 = 3`. |
| **Stepped Bowl** | `[4, 1, 2, 1, 4]` | `8` | Traps `3 + 2 + 3 = 8` units across middle indices. |
| **Unequal Boundaries** | `[5, 1, 2, 1, 2]` | `2` | Right boundary (height 2) restricts water level to 2. |
| **Large Flat Bottom** | `[2, 0, 0, 0, 2]` | `6` | 3 indices each hold 2 units of water (`2 * 3 = 6`). |


# Technical Design

### File Structure
- `two_pointer_algorithms/__init__.py`: Package initialization file matching existing project package conventions.
- `two_pointer_algorithms/max_trapped_water.py`: Target module containing the outline, comments, function stub, and test assertions.

### Python File Structure & Template (`two_pointer_algorithms/max_trapped_water.py`)

```python
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
    #   'right_max' (highest bar seen from right to n - 1).
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

    # TODO: Implement your solution here
    pass


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
        assert result == expected, (
            f"Failed on [{description}] heights={heights}. Expected {expected}, got {result}"
        )

    print("All test cases passed successfully!")
```


# Testing

### Validation Strategy
- Execute `python -m two_pointer_algorithms.max_trapped_water` or run the file directly to verify assertions against all test cases.
- Confirm zero trapped water on monotonic, empty, and small inputs.
- Validate accurate water trapping on complex topography with asymmetrical walls and multiple valleys.

### Key Invariants to Verify
1. **Edge Immunity**: Boundaries (`0` and `n-1`) cannot hold water.
2. **Non-Negativity**: Trapped water at any individual position is always $\ge 0$.
3. **Monotonicity Nullity**: Monotonically non-decreasing or non-increasing arrays always return `0`.
4. **Bottleneck Principle**: Trapped water in any trough is strictly bounded by $\min(\text{left\_max}, \text{right\_max})$.


# Delivery Steps

###   Step 1: Create Package and Scaffold max_trapped_water.py
Create the `two_pointer_algorithms` package and scaffold `max_trapped_water.py` with instructional comments:
- Create `two_pointer_algorithms/__init__.py` to establish the new package under the project root.
- Create `two_pointer_algorithms/max_trapped_water.py` with module docstrings outlining the problem statement and physical intuition.
- Define `max_trapped_water(heights: list[int]) -> int` with type hints and a docstring detailing inputs, return value, and Big-O targets.
- Embed structured step-by-step guidance comments (guard conditions, two-pointer invariants, and alternative paradigms) without revealing the solution implementation.

###   Step 2: Add Test Cases and Execution Block
Implement the assertion-based test runner in `two_pointer_algorithms/max_trapped_water.py`:
- Add a comprehensive list of test tuples in the `if __name__ == "__main__":` block covering standard cases, edge cases (empty, 1-2 bars), monotonic slopes, flat profiles, and asymmetrical bowls.
- Implement an iteration loop with detailed assertion error messaging to validate algorithm output against expected results.