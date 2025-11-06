"""
🧩 Problem: “Rate Limit Check”

Task description:
-----------------
You are building a system that limits how frequently a user can perform an action (for example, sending requests
to an API).

You are given:
- An integer `limit` — the maximum number of allowed actions within a rolling time window.
- An integer `window` — the duration of that time window, in seconds.
- A list of integers `timestamps`, where each element represents the time in seconds when a user performed an
  action (sorted in non-decreasing order).

Your task is to determine, for each timestamp, whether the user’s action should be allowed or rejected according
to the rate limit rule.

The rate limit rule:
--------------------
A request at time `t` is allowed if there are fewer than `limit` actions within the last `window` seconds,
including the current request.

Formally, for each request at time `t`, the valid time range (rolling window) is:

    [t - window + 1, t]

Only actions whose timestamps fall within that range count toward the limit.

If there are already `limit` or more actions within this range, the request is rejected.

Return a list of booleans (or 1/0 integers), indicating whether each request is allowed (True or 1) or rejected
(False or 0).

Example:
--------
Input:
    limit = 3
    window = 10
    timestamps = [1, 2, 3, 11, 12, 13, 14]

Output:
    [True, True, True, True, True, True, False]

Step-by-step explanation:
    t=1  → window [−8, 1]  → [1]                   → allowed
    t=2  → window [−7, 2]  → [1, 2]                → allowed
    t=3  → window [−6, 3]  → [1, 2, 3]             → allowed
    t=11 → window [2, 11]  → [2, 3, 11]            → allowed
    t=12 → window [3, 12]  → [3, 11, 12]           → allowed
    t=13 → window [4, 13]  → [11, 12, 13]          → allowed
    t=14 → window [5, 14]  → [11, 12, 13, 14]      → rejected (limit exceeded)

Function signature:
-------------------
    def solution(limit: int, window: int, timestamps: list[int]) -> list[bool]:

Constraints:
------------
    1 ≤ limit ≤ 10^4
    1 ≤ window ≤ 10^5
    1 ≤ len(timestamps) ≤ 10^5
    0 ≤ timestamps[i] ≤ 10^9
    timestamps are sorted in non-decreasing order.

Performance requirements:
-------------------------
    Expected time complexity: O(N)
    Expected space complexity: O(L), where L ≤ limit

Hint:
-----
Use a queue (deque) to store timestamps of recent allowed requests.

For each new timestamp t:
    1. Remove timestamps older than t - window + 1.
    2. If the queue size < limit, allow and append.
    3. Otherwise, reject.
"""

"""
Rate Limiter Algorithm Demo
---------------------------

This program demonstrates a basic sliding-window rate limiter.

Given:
  - `limit`: the maximum number of allowed actions within a time window
  - `window`: the window size (in seconds)
  - `timestamps`: a list of timestamps (ascending order) when actions occurred

For each timestamp, the program returns True if the action is allowed,
or False if it exceeds the rate limit.

Constraints:
  1 <= limit <= 10^4
  1 <= window <= 10^5
  1 <= len(timestamps) <= 10^5
  1 <= timestamps[i] <= 10^9
  timestamps must be non-decreasing
"""

from collections import deque


def solution(limit: int, window: int, timestamps: list[int]) -> list[bool]:
    """Return a list indicating whether each request is allowed by the rate limiter."""

    # Validate arguments
    if limit < 1 or limit > 10**4:
        raise ValueError("The limit is not in range (1 ≤ limit ≤ 10^4)")
    if window < 1 or window > 10**5:
        raise ValueError("The window is not in range (1 ≤ window ≤ 10^5)")
    if len(timestamps) > 10**5:
        raise ValueError("The number of timestamps exceeds 10^5")

    q = deque()  # stores timestamps within the active window
    allowed = []  # stores True/False results

    arg_params = f"limit={limit}, window={window}, timestamps={timestamps}"

    for index, timestamp in enumerate(timestamps):
        # Check timestamp validity
        if timestamp < 1 or timestamp > 10**9:
            raise ValueError(
                f"The timestamp {timestamp} is out of valid range. {arg_params}"
            )

        # Ensure timestamps are non-decreasing
        if index > 0 and timestamp < timestamps[index - 1]:
            raise ValueError(
                f"The timestamps are not in ascending order. {arg_params}"
            )

        # Remove timestamps that have fallen out of the window
        while q and q[0] < timestamp - window + 1:
            q.popleft()

        # Allow or deny this request
        if len(q) < limit:
            q.append(timestamp)
            allowed.append(True)
        else:
            allowed.append(False)

    return allowed


# ---------------------------------------------------------------------
# TEST HARNESS
# ---------------------------------------------------------------------
def run_tests(verbose: bool = True) -> None:
    """Run sample test cases for the rate limiter."""

    cases = [
        (3, 10, [1, 2, 3, 11, 12, 13, 14]),
        (4, 9, [2, 3, 4, 5, 6, 15, 16, 17, 19, 20]),
        (2, 2, [1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (3, 10, [14, 13, 12, 11, 3, 2, 1]),  # invalid: not ascending
        (3, 10, [5]),
        (2, 10, [1, 2, 3]),
        (3, 10, [0, 10]),  # invalid: timestamp out of range
        (3, 10, None),
    ]

    expected_outputs = [
        [True, True, True, True, True, True, False],
        [True, True, True, True, False, True, True, True, True, False],
        [True, True, False, False, False, False, False, False, False],
        None,
        [True],
        [True, True, False],
        None,
        None,
    ]

    for idx, case in enumerate(cases):
        try:
            result = solution(*case)
            expected = expected_outputs[idx]

            if result != expected:
                raise AssertionError(
                    f"\n❌ Case {case}\nGot:      {result}\nExpected: {expected}\n"
                )
            if verbose:
                print(f"✅ Case {case} passed. Output: {result}")

        except ValueError as e:
            if expected_outputs[idx] is None:
                if verbose:
                    print(f"⚠️  Case {case} raised expected ValueError: {e}")
            else:
                raise


# ---------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------
if __name__ == "__main__":
    run_tests(verbose=True)
