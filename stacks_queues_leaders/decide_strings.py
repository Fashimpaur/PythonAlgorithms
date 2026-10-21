"""
PROBLEM: Decode String
======================

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is repeated exactly k times. k is always a positive integer.

You may assume:
  - The input string is always valid (no extra whitespace, brackets are
    well-formed).
  - The original data contains no digits; digits only appear as repeat counts.
  - Letters are lowercase English letters (a-z).
  - 1 <= len(s) <= 100
  - k is in the range [1, 300]

Examples:
---------
  Input:  "3[a]2[bc]"
  Output: "aaabcbc"

  Input:  "3[a2[c]]"
  Output: "accaccacc"

  Input:  "2[abc]3[cd]ef"
  Output: "abcabccdcdcdef"

  Input:  "abc3[x]"
  Output: "abcxxx"

  Input:  "10[a]"
  Output: "aaaaaaaaaa"      (note: k can be multiple digits)

Hints (read only if stuck):
---------------------------
  1. Nested brackets mean you need to remember "where you were" when you
     enter a bracket. What data structure is good at that?
  2. When you hit '[', save the current string and the current count.
  3. When you hit ']', pop what you saved and combine it with the repeated
     current string.
  4. Remember that numbers can have more than one digit.

Bonus challenges:
-----------------
  - Solve it iteratively with a stack.
  - Solve it recursively.
  - What's the time complexity? (Hint: it depends on the output length.)
"""


def decode_string_splits(s: str) -> str:
    while "[" in s:
        left, rest = s.rsplit("[", 1)  # split at the LAST '['
        inner, right = rest.split("]", 1)  # split at the first ']' after it

        # The count is the run of digits at the end of `left`
        i = len(left)
        while i > 0 and left[i - 1].isdigit():
            i -= 1
        prefix, num = left[:i], int(left[i:])

        s = prefix + inner * num + right

    return s


def decode_string(s: str) -> str:
    # TIME:  O(n + m) in the typical case.
    #        One pass over the input, and each ']' builds a string whose
    #        size is bounded by the output. (Edge case: deeply nested
    #        k=1 brackets like 1[1[1[abc]]] re-copy the inner string at
    #        every level, which can degrade toward O(n * m).)
    # SPACE: O(n + m)
    #        The stack holds saved prefixes (at most n characters total)
    #        and current_string can grow to the size of the output.
    stack = []
    current_string = ""
    current_num = 0

    for ch in s:  # O(n) iterations
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)  # O(1)
        elif ch == "[":
            stack.append((current_string, current_num))  # O(1)
            current_string = ""
            current_num = 0
        elif ch == "]":
            prev_string, num = stack.pop()  # O(1)
            # Repeat + concatenate costs O(size of the new string)
            current_string = prev_string + current_string * num
        else:
            current_string += ch  # O(1) amortized in CPython

    return current_string


# ---------------------------------------------------------------------------
# Tests - run this file with `python your_file.py`
# ---------------------------------------------------------------------------
def run_tests():
    test_cases = [
        ("3[a]21[bc]", "aaa" + 21 * "bc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[x]", "abcxxx"),
        ("10[a]", "aaaaaaaaaa"),
        ("a", "a"),
        ("2[2[2[a]]]", "aaaaaaaa"),
        ("2[a2[b]]c", "abbabbc"),
        ("1[x]", "x"),
        ("", ""),
        ("4[b]5[", "")
    ]

    passed = 0
    for i, (given, expected) in enumerate(test_cases, 1):
        try:
            result = decode_string(given)
        except Exception as e:
            result = f"<raised {type(e).__name__}: {e}>"

        if result == expected:
            passed += 1
            print(f"PASS  test {i}: {given!r} -> {result!r}")
        else:
            print(f"FAIL  test {i}: {given!r}")
            print(f"        expected: {expected!r}")
            print(f"        got:      {result!r}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
