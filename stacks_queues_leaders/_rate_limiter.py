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
