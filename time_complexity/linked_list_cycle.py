"""
Linked List Cycle (detect whether a singly linked list contains a cycle)
=========================================================================

PROBLEM
-------
Given the head of a singly linked list, return True if the list contains a
cycle, otherwise return False.

A cycle exists if some node can be reached again by continuously following
`next` pointers. (Internally, the tail's `next` points back to an earlier node.)

INPUT / OUTPUT
--------------
Input : head -> Optional[ListNode]
Output: bool

CONSTRAINTS (typical)
---------------------
- Number of nodes: 0 to 10,000 (can be larger in practice)
- Node values: -100,000 to 100,000 (values are irrelevant to the answer)
- You are NOT given the cycle position as input; it only exists in how the
  nodes are linked.

GUIDELINES (read before coding)
-------------------------------
1. Understand the shape: a list without a cycle ends in None. A list with a
   cycle never reaches None. A naive "walk until None" loop will hang forever
   on a cyclic list, so you need a way to know when you have gone around.
2. Compare nodes by identity, not by value. Two different nodes can hold the
   same value, so `a.val == b.val` does not mean `a is b`.
3. Handle edge cases explicitly:
     - empty list (head is None)
     - single node, with and without a self-loop
     - two nodes
     - cycle that includes the head vs. a cycle that starts mid-list
4. Think about complexity before coding. Aim to first get a correct solution,
   then ask: can I do it in O(n) time AND O(1) extra space?
5. Never modify node values or permanently destroy the list structure
   unless you restore it. Tests may reuse the same list.
6. Guard against infinite loops in your own tests. If a test hangs, your
   termination condition is wrong (the harness below has a timeout helper).

STEPS TO WORK THROUGH
---------------------
  [ ] Step 1: Write down, in plain English, how you would detect "I've been
              here before" while walking the list.
  [ ] Step 2: List what extra state you need to carry while walking.
  [ ] Step 3: Decide the loop termination conditions (both outcomes).
  [ ] Step 4: Trace your idea by hand on Test 3 and Test 5 below.
  [ ] Step 5: Implement, run the tests, then consider the O(1)-space follow-up.

FOLLOW-UPS TO CONSIDER
----------------------
- Can you solve it without any additional data structure that grows with n?
- Can you return the node where the cycle begins (or None)?
- Can you compute the length of the cycle?
"""

import time
import tracemalloc
from typing import Optional, List, Callable, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ---------------------------------------------------------------------------
# Brute force attempt
# ---------------------------------------------------------------------------


def has_cycle_brute_force(head: Optional[ListNode]) -> bool:
    visited = []
    current = head
    while current is not None:
        if current in visited:      # linear scan of the list each time
            return True
        visited.append(current)
        current = current.next
    return False

# Time:  O(n^2)  (each "in" check scans up to n items)
# Space: O(n)


def has_cycle_hash_set(head: Optional[ListNode]) -> bool:
    seen = set()
    current = head
    while current is not None:
        if current in seen:         # O(1) average lookup
            return True
        seen.add(current)
        current = current.next
    return False

# Time:  O(n)
# Space: O(n)


# ---------------------------------------------------------------------------
# Two pointer slow and fast
# ---------------------------------------------------------------------------


def has_cycle_slow_and_fast(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next            # moves 1 step
        fast = fast.next.next       # moves 2 steps
        if slow is fast:            # they can only meet inside a cycle
            return True
    return False                    # fast reached the end, so no cycle

# Time:  O(n)
# Space: O(1)


# Default implementation
has_cycle = has_cycle_slow_and_fast


# ---------------------------------------------------------------------------
# TEST HELPERS
# ---------------------------------------------------------------------------
def build_list(values: List[int], pos: int = -1) -> Optional[ListNode]:
    """
    Build a linked list from `values`.
    If pos >= 0, the tail's next pointer is connected to the node at index
    `pos` (creating a cycle). If pos == -1, there is no cycle.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# ---------------------------------------------------------------------------
# TEST CASES: (description, values, pos, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    ("1. Empty list",                         [],                   -1, False),
    ("2. Single node, no cycle",              [1],                  -1, False),
    ("3. Single node, self-loop",             [1],                   0, True),
    ("4. Two nodes, no cycle",                [1, 2],               -1, False),
    ("5. Two nodes, tail points to head",     [1, 2],                0, True),
    ("6. Two nodes, tail points to itself",   [1, 2],                1, True),
    ("7. Long list, no cycle",                list(range(100)),     -1, False),
    ("8. Cycle starts at head",               [3, 2, 0, -4],         0, True),
    ("9. Cycle starts mid-list",              [3, 2, 0, -4],         1, True),
    ("10. Cycle only at the tail node",       [1, 2, 3, 4, 5],       4, True),
    ("11. Duplicate values, NO cycle",        [7, 7, 7, 7, 7],      -1, False),
    ("12. Duplicate values, WITH cycle",      [7, 7, 7, 7, 7],       2, True),
    ("13. Large list with cycle",             list(range(10000)),  5000, True),
    ("14. Large list without cycle",          list(range(10000)),   -1, False),
]


def run_variant_tests(
    func: Callable[[Optional[ListNode]], bool],
    variant_name: Optional[str] = None,
) -> Tuple[int, int, float, int]:
    """
    Runs all test cases on a specific has_cycle variant independently,
    measuring execution time and peak memory consumed by the function.
    Returns (passed_count, total_count, total_time_seconds, peak_memory_bytes).
    """
    display_name = variant_name if variant_name else func.__name__
    print(f"\n{'=' * 70}")
    print(f"Running Tests for: {display_name} ({func.__name__})")
    print(f"{'=' * 70}")

    passed = 0
    total_time = 0.0
    peak_mem = 0

    for desc, values, pos, expected in TEST_CASES:
        head = build_list(values, pos)
        try:
            tracemalloc.start()
            tracemalloc.reset_peak()
            start_time = time.perf_counter()
            result = func(head)
            end_time = time.perf_counter()
            _, test_peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
        except NotImplementedError:
            if tracemalloc.is_tracing():
                tracemalloc.stop()
            print(f"[SKIP] {desc}: not implemented yet")
            continue
        except Exception as e:
            if tracemalloc.is_tracing():
                tracemalloc.stop()
            print(f"[ERROR] {desc}: {e}")
            continue

        elapsed = end_time - start_time
        total_time += elapsed
        peak_mem = max(peak_mem, test_peak)

        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        print(f"[{status}] {desc} | expected={expected} got={result}")

    print(f"\nResults: {passed}/{len(TEST_CASES)} tests passed for {display_name}")
    print(f"--- Performance Stats for {func.__name__} ---")
    print(f"  Total Execution Time : {total_time * 1000:.3f} ms ({total_time:.6f} s)")
    print(f"  Peak Memory Consumed : {peak_mem} bytes ({peak_mem / 1024:.2f} KiB)")

    return passed, len(TEST_CASES), total_time, peak_mem


def run_tests() -> None:
    """
    Runs all test cases independently across all has_cycle variants,
    displaying individual test results and performance statistics for each,
    followed by a summary comparison.
    """
    variants = [
        ("Brute Force (List/Array Lookup)", has_cycle_brute_force),
        ("Hash Set (Seen Nodes)", has_cycle_hash_set),
        ("Two Pointers (Slow & Fast / Floyd's Cycle Detection)", has_cycle_slow_and_fast),
    ]

    summary = []
    for display_name, func in variants:
        passed, total, elapsed, mem = run_variant_tests(func, display_name)
        summary.append((func.__name__, passed, total, elapsed, mem))

    print(f"\n{'=' * 70}")
    print("Summary Comparison Across Variants:")
    print(f"{'-' * 70}")
    print(f"{'Variant':<26} {'Passed':<10} {'Time (ms)':<14} {'Peak Memory'}")
    print(f"{'-' * 70}")
    for name, passed, total, elapsed, mem in summary:
        mem_str = f"{mem} B ({mem / 1024:.2f} KiB)"
        print(f"{name:<26} {f'{passed}/{total}':<10} {elapsed * 1000:<14.3f} {mem_str}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    # Tip: if the script hangs, your loop has no valid exit for cyclic input.
    # Press Ctrl+C and re-check your termination conditions.
    run_tests()
