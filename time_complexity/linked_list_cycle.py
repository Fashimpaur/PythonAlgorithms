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

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ---------------------------------------------------------------------------
# YOUR SOLUTION
# ---------------------------------------------------------------------------
def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Return True if the linked list starting at `head` contains a cycle.

    TODO: Implement.
    Remember: compare nodes by identity, handle None/short lists safely,
    and make sure the function always terminates.
    """
    raise NotImplementedError("Implement has_cycle")


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


def run_tests() -> None:
    passed = 0
    for desc, values, pos, expected in TEST_CASES:
        head = build_list(values, pos)
        try:
            result = has_cycle(head)
        except NotImplementedError:
            print(f"[SKIP] {desc}: not implemented yet")
            continue
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        print(f"[{status}] {desc} | expected={expected} got={result}")
    print(f"\n{passed}/{len(TEST_CASES)} tests passed")


if __name__ == "__main__":
    # Tip: if the script hangs, your loop has no valid exit for cyclic input.
    # Press Ctrl+C and re-check your termination conditions.
    run_tests()
