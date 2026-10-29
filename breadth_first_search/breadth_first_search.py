"""
Problem: Breadth-First Search Traversal
=======================================

Description
-----------
Given an undirected graph represented as an adjacency list and a starting
node, return the order in which nodes are visited during a breadth-first
search (BFS).

Why BFS? (The motivating scenario)
----------------------------------
Imagine a social network where each node is a person and each edge is a
friendship. You want to know who is a direct friend of yours, then who is a
friend-of-a-friend, then friends-of-friends-of-friends, and so on. BFS
visits nodes in exactly that order: every node that is 1 edge away from
`start` is visited before any node that is 2 edges away, and so on.

This "closest first" property is why BFS is the standard tool for:
  - Shortest path in an UNWEIGHTED graph (fewest edges / hops).
  - "Degrees of separation" and friend-suggestion features.
  - Finding the nearest resource (closest exit in a maze, nearest hospital).
  - Level-by-level processing (web crawlers limiting depth, tree levels).

Input Format
------------
- graph: a dictionary where each key is a node (an integer) and each value
  is a list of that node's neighbors.
- start: an integer that is guaranteed to be a key in `graph`.

Output Format
-------------
- A list of integers representing the nodes in the order they were first
  visited.
- Only nodes reachable from `start` should appear in the output.

Rules and Constraints
---------------------
1. Neighbor order matters. When enqueuing neighbors, always process them in
   the order they appear in the adjacency list (left to right).
2. Visit each node exactly once. The graph may contain cycles, so you must
   track visited nodes to avoid infinite loops.
3. Go wide first. Visit `start`, then ALL of its neighbors, then ALL of
   their unvisited neighbors, and so on, one "level" at a time.
4. Disconnected nodes are ignored. Nodes not reachable from `start` must
   not appear in the result.
5. The graph is undirected, so if `b` appears in `a`'s list, `a` will
   appear in `b`'s list. Your solution should not rely on this, though,
   and should work correctly for any adjacency list.
6. Edge cases to handle:
   - A graph with a single node and no edges.
   - A start node with no neighbors.
   - Cycles and self-loops (a node listing itself as a neighbor).
   - Nodes with duplicate entries in a neighbor list should still only be
     visited once.
7. Node values are unique integers. You may assume the input is well-formed
   (every neighbor listed is also a key in `graph`).
8. BFS is naturally iterative and uses a QUEUE (first in, first out). Use
   collections.deque so removing from the front is O(1); popping from the
   front of a plain list is O(n) and would quietly slow the algorithm down.
"""

from collections import deque


def breadth_first_search(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Perform a breadth-first search traversal of a graph (iterative, queue).

    Args:
        graph: Adjacency list mapping each node to a list of its neighbors.
        start: The node at which to begin the traversal.

    Returns:
        A list of nodes in the order they were first visited.
    """
    # Space: O(V) for the visited set (at most one entry per reachable node).
    # Nodes are marked visited when they are ENQUEUED, not when dequeued.
    # Marking late would let the same node be added to the queue several times
    # before it is processed, wasting time and memory (and, with the O(E)
    # bound below, potentially breaking it).
    visited: set[int] = {start}

    # Space: O(V) for the result list (one entry per reachable node).
    result: list[int] = []

    # Space: O(V) for the queue in the worst case. Each node enters the queue
    # at most once, so it can never hold more than V items. On a "wide" graph
    # (e.g. a star with one hub connected to everything) the queue holds
    # almost every node at once, which is BFS's main memory cost.
    queue: deque[int] = deque([start])

    # Time: the loop body runs once per reachable node, so V iterations total.
    while queue:
        # Time: O(1). deque.popleft() is constant time (a list's pop(0) is O(n)).
        node = queue.popleft()

        # Time: O(1) per node (list append, amortized). O(V) total.
        result.append(node)

        # Time: this inner loop runs len(graph[node]) times. Summed over all
        # dequeued nodes, that is every adjacency entry once, so O(E) total.
        # Each iteration does O(1) work (set lookup, set add, deque append).
        # Neighbor order is preserved (rule 1); the FIFO queue guarantees all
        # nodes at distance d are processed before any at distance d + 1
        # (rule 3: go wide first).
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Overall Time:  O(V + E)  (each node dequeued once, each edge scanned once).
    # Overall Space: O(V)      (visited set + queue + result list).
    return result


def bfs_distances(graph: dict[int, list[int]], start: int) -> dict[int, int]:
    """
    Return how many edges away from `start` each reachable node is.

    The plain traversal above only gives a visit ORDER (a ranking by
    closeness). This version also records the exact distance, which answers
    questions like "how closely related is this person to me?"
    (0 = you, 1 = direct friend, 2 = friend of a friend, and so on.)

    Args:
        graph: Adjacency list mapping each node to a list of its neighbors.
        start: The node at which to begin the traversal.

    Returns:
        A dictionary mapping each reachable node to its distance from start.
        Nodes that cannot be reached from `start` are not in the dictionary.
    """
    # Space: O(V). This dictionary does double duty: its keys are the visited
    # set, and its values are the distances, so no separate set is needed.
    distance: dict[int, int] = {start: 0}

    # Space: O(V) for the queue, same reasoning as breadth_first_search.
    queue: deque[int] = deque([start])

    # Time: V iterations, one per reachable node.
    while queue:
        node = queue.popleft()

        # Time: O(E) total across all nodes, same as the plain traversal.
        # A node is first discovered through the shortest possible route
        # (BFS finishes every level before starting the next), so its
        # distance is simply its parent's distance + 1. That first value is
        # final and never needs to be updated.
        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    # Overall Time:  O(V + E)  (identical to the plain traversal).
    # Overall Space: O(V)      (distance dictionary + queue).
    return distance


# ---------------------------------------------------------------------------
# Test cases: (graph, start, expected_output)
# ---------------------------------------------------------------------------
TESTS = [
    # Test 1: Simple tree
    # Level 1 (2, 3) is fully visited before level 2 (4, 5).
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 1, [1, 2, 3, 4, 5]),
    # Test 2: Graph with a cycle
    # Both neighbors of 1 are visited before reaching 4.
    ({1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}, 1, [1, 2, 3, 4]),
    # Test 3: Single node
    ({1: []}, 1, [1]),
    # Test 4: Disconnected graph
    ({1: [2], 2: [1], 3: [4], 4: [3]}, 1, [1, 2]),
    # Test 5: Different starting node
    # 1 and 5 (both next to 2) are visited before 3.
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 4, [4, 2, 1, 5, 3]),
    # Test 6: Self-loop and duplicate neighbors
    ({1: [1, 2, 2, 3], 2: [1], 3: [1]}, 1, [1, 2, 3]),
    # Test 7: Longer chain with a branch
    # The two branches are interleaved by distance from node 0.
    ({0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2], 4: [0, 5], 5: [4]}, 0, [0, 1, 4, 2, 5, 3]),
    # Test 8: Social network (direct friends, friends-of-friends, and so on)
    #
    # Node 1 is "you". Node ids are deliberately NOT in numeric order of
    # distance, so the output order shows BFS's level-by-level behavior.
    #
    #   Degree 0 (you):                      1
    #   Degree 1 (direct friends):           10, 20, 30
    #   Degree 2 (friends of friends):       11, 21, 31, 32
    #   Degree 3 (friends of friends of...): 12, 40
    #   Degree 4:                            13
    #   Not connected to you at all:         98, 99  (never appear in output)
    #
    # Notes on the structure:
    #   - 10 and 20 are friends with each other (a cycle with you), so
    #     neither is "discovered" twice.
    #   - 12 is reachable from BOTH 11 and 21; it is only visited once, at
    #     the shortest distance (degree 3).
    (
        {
            1: [10, 20, 30],
            10: [1, 20, 11],
            20: [1, 10, 21],
            30: [1, 31, 32],
            11: [10, 12],
            21: [20, 12],
            31: [30, 40],
            32: [30],
            12: [11, 21, 13],
            40: [31],
            13: [12],
            98: [99],
            99: [98],
        },
        1,
        [1, 10, 20, 30, 11, 21, 31, 32, 12, 40, 13],
    ),
]


def run_tests() -> None:
    passed = 0
    for i, (graph, start, expected) in enumerate(TESTS, 1):
        result = breadth_first_search(graph, start)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test {i}: {status} | got {result}, expected {expected}")
    print(f"\n{passed}/{len(TESTS)} tests passed")


# Labels for the social network example (Test 8).
RELATIONSHIP_LABELS = {
    0: "you",
    1: "direct friend",
    2: "friend of a friend",
    3: "friend of a friend of a friend",
    4: "4th-degree connection",
}


def run_distance_demo() -> None:
    """Use the Test 8 social network to show HOW CLOSE each person is to you."""
    graph, start, visit_order = TESTS[7]  # Test 8; its visit order stays as-is
    distance = bfs_distances(graph, start)

    expected = {
        1: 0,
        10: 1, 20: 1, 30: 1,
        11: 2, 21: 2, 31: 2, 32: 2,
        12: 3, 40: 3,
        13: 4,
    }
    status = "PASS" if distance == expected else "FAIL"
    print(f"\nDistance check (Test 8 graph): {status}")
    print(f"  got {distance}")

    # The distances agree with the BFS visit order: walking the visit order,
    # the distance never goes down.
    in_order = [distance[node] for node in visit_order]
    monotonic = in_order == sorted(in_order)
    print(f"  visit order has non-decreasing distance: {monotonic}")

    print("\nHow closely is each person related to you?")
    for node in visit_order:
        d = distance[node]
        print(f"  person {node:>2}: degree {d} ({RELATIONSHIP_LABELS[d]})")

    # Nodes missing from the dictionary are not connected to you at all.
    unreachable = sorted(set(graph) - set(distance))
    print(f"\nNot connected to you: {unreachable}")


if __name__ == "__main__":
    run_tests()
    run_distance_demo()


# ===========================================================================
# SUMMARY
# ===========================================================================
#
# What BFS does
#   Starting at `start`, BFS visits every node 1 edge away, then every node
#   2 edges away, and so on, using a FIFO queue. The visit order is therefore
#   sorted by distance from `start` (measured in edges). In the social
#   network example (Test 8) that means: you, then your direct friends, then
#   friends of friends, then the next ring out.
#
# Complexity
#   Time:  O(V + E)
#          - Each reachable node is enqueued and dequeued exactly once: O(V).
#          - Each adjacency entry is examined exactly once: O(E).
#          - Every individual operation (set lookup/add, deque append/popleft,
#            list append) is O(1), so nothing multiplies these terms.
#   Space: O(V)
#          - visited set, result list, and queue each hold at most V nodes.
#          - There is no recursion, so BFS cannot hit Python's recursion
#            limit on long chains.
#          - The queue grows with the WIDEST level of the graph, which is
#            where BFS's memory cost shows up on very wide graphs.
#
# When to choose BFS
#   - You need the shortest path (fewest edges) in an unweighted graph.
#   - You need "degrees of separation" or other level-by-level answers.
#   - The answer is likely close to the start, so there is no need to
#     explore deep, irrelevant branches first.
#
# Getting the exact degree, not just the order
#   The visit order only RANKS nodes by closeness; it does not say where one
#   degree ends and the next begins. bfs_distances() records distance[child]
#   = distance[parent] + 1 as each node is first discovered, giving the exact
#   degree of every reachable node at no extra asymptotic cost: still
#   O(V + E) time and O(V) space. A node missing from the result is not
#   connected to the start at all.
#
# Common pitfalls
#   - Marking nodes visited on dequeue instead of enqueue (duplicates in queue).
#   - Using list.pop(0) instead of deque.popleft() (turns O(1) into O(n)).
# ===========================================================================
