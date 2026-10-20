def is_valid(s: str) -> bool:
    """
    Determine whether a string contains validly matched brackets.

    Opening brackets must be closed by the corresponding closing
    bracket in the correct order. An empty string is valid.

    Args:
        s: A string containing parentheses, square brackets, and
            curly braces.

    Returns:
        True if all brackets are correctly matched and nested;
        otherwise, False.

    Time Complexity:
        O(n), where n is the length of the input string. Each
        character is processed at most once, with O(1) average-case
        dictionary lookups and amortized O(1) stack operations.

    Auxiliary Space Complexity:
        O(n) worst case, where n is the length of the input string.
        The stack may store every character if all characters are
        opening brackets. The fixed-size dictionary and set use O(1)
        auxiliary space.
    """

    # Time: O(1); Auxiliary Space: O(1).
    # Maps each closing bracket to its matching opening bracket.
    closing_to_opening = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # Time: O(1); Auxiliary Space: O(1).
    # Identifies opening brackets using average-case O(1) membership checks.
    opening_brackets = {"(", "[", "{"}

    # Auxiliary Space: O(1) initially; O(n) worst case as items are added.
    bracket_stack = []

    # Time: O(n) overall — each input character is processed at most once.
    for char in s:
        if char in opening_brackets:
            # Time: O(1) amortized per append.
            # Auxiliary Space: O(1) per push; O(n) worst case overall.
            bracket_stack.append(char)

        elif char in closing_to_opening:
            # Time: O(1); no additional auxiliary space.
            if not bracket_stack:
                return False

            # Time: O(1) per pop.
            # Auxiliary Space: O(1) — removes the top stack element.
            top = bracket_stack.pop()

            # Time: O(1) average case for the dictionary lookup.
            if top != closing_to_opening[char]:
                return False

    # Time: O(1); Auxiliary Space: O(1).
    # Any remaining opening brackets are unmatched.
    return not bracket_stack


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        (")(", False),
        ("", True),
    ]

    for input_string, expected in test_cases:
        result = is_valid(input_string)
        assert result == expected, (
            f"Input: {input_string!r}, "
            f"Expected: {expected}, Got: {result}"
        )

    print("All test cases passed.")