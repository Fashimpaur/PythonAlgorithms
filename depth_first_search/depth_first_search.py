"""
Problem: Depth-First Search Traversal
=====================================

Description
-----------
Given an undirected graph represented as an adjacency list and a starting
node, return the order in which nodes are visited during a depth-first
search (DFS).

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
1. Neighbor order matters. When choosing which neighbor to visit next,
   always process neighbors in the order they appear in the adjacency list
   (left to right).
2. Visit each node exactly once. The graph may contain cycles, so you must
   track visited nodes to avoid infinite loops.
3. Go deep first. From the current node, fully explore the first unvisited
   neighbor (and everything reachable from it) before moving on to the
   next neighbor.
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
8. You may implement this recursively or iteratively. Note: if you go
   iterative with an explicit stack, be careful that the visit order still
   matches rule 1 and rule 3, since pushing neighbors onto a stack
   naturally reverses their processing order.
"""


"""
Problem: Depth-First Search Traversal
=====================================

Description
-----------
Given an undirected graph represented as an adjacency list and a starting
node, return the order in which nodes are visited during a depth-first
search (DFS).

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
1. Neighbor order matters. When choosing which neighbor to visit next,
   always process neighbors in the order they appear in the adjacency list
   (left to right).
2. Visit each node exactly once. The graph may contain cycles, so you must
   track visited nodes to avoid infinite loops.
3. Go deep first. From the current node, fully explore the first unvisited
   neighbor (and everything reachable from it) before moving on to the
   next neighbor.
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
8. You may implement this recursively or iteratively. Note: if you go
   iterative with an explicit stack, be careful that the visit order still
   matches rule 1 and rule 3, since pushing neighbors onto a stack
   naturally reverses their processing order.
"""


def depth_first_search(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Perform a depth-first search traversal of a graph (recursive).

    Args:
        graph: Adjacency list mapping each node to a list of its neighbors.
        start: The node at which to begin the traversal.

    Returns:
        A list of nodes in the order they were first visited.
    """
    # Space: O(V) for the visited set (at most one entry per reachable node).
    visited: set[int] = set()
    # Space: O(V) for the result list (one entry per reachable node).
    result: list[int] = []

    def visit(node: int) -> None:
        # Time: O(1) per call for the set membership check. This check is what
        # keeps total work bounded: without it, cycles would recurse forever.
        if node in visited:
            return

        # Time: O(1) per node (set add + list append, amortized).
        # Each node passes this point at most once, so O(V) total.
        visited.add(node)
        result.append(node)

        # Time: this loop runs len(graph[node]) times. Summed over all visited
        # nodes, that is every adjacency entry once, so O(E) total.
        # Neighbor order is preserved (rule 1), and each recursive call finishes
        # before the loop moves on (rule 3: go deep first).
        #
        # Space: each active call adds one frame to the call stack. In the worst
        # case (a long chain) the recursion is V frames deep, so O(V) stack space.
        for neighbor in graph[node]:
            visit(neighbor)

    visit(start)
    return result


# ---------------------------------------------------------------------------
# Test cases: (graph, start, expected_output)
# ---------------------------------------------------------------------------
TESTS = [
    # Test 1: Simple tree
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 1, [1, 2, 4, 5, 3]),
    # Test 2: Graph with a cycle
    ({1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}, 1, [1, 2, 4, 3]),
    # Test 3: Single node
    ({1: []}, 1, [1]),
    # Test 4: Disconnected graph
    ({1: [2], 2: [1], 3: [4], 4: [3]}, 1, [1, 2]),
    # Test 5: Different starting node
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 4, [4, 2, 1, 3, 5]),
    # Test 6: Self-loop and duplicate neighbors
    ({1: [1, 2, 2, 3], 2: [1], 3: [1]}, 1, [1, 2, 3]),
    # Test 7: Longer chain with a branch
    ({0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2], 4: [0, 5], 5: [4]}, 0, [0, 1, 2, 3, 4, 5]),
]


def run_tests() -> None:
    passed = 0
    for i, (graph, start, expected) in enumerate(TESTS, 1):
        result = depth_first_search(graph, start)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test {i}: {status} | got {result}, expected {expected}")
    print(f"\n{passed}/{len(TESTS)} tests passed")


if __name__ == "__main__":
    run_tests()


# ---------------------------------------------------------------------------
# Test cases: (graph, start, expected_output)
# ---------------------------------------------------------------------------
TESTS = [
    # Test 1: Simple tree
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 1, [1, 2, 4, 5, 3]),
    # Test 2: Graph with a cycle
    ({1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}, 1, [1, 2, 4, 3]),
    # Test 3: Single node
    ({1: []}, 1, [1]),
    # Test 4: Disconnected graph
    ({1: [2], 2: [1], 3: [4], 4: [3]}, 1, [1, 2]),
    # Test 5: Different starting node
    ({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}, 4, [4, 2, 1, 3, 5]),
    # Test 6: Self-loop and duplicate neighbors
    ({1: [1, 2, 2, 3], 2: [1], 3: [1]}, 1, [1, 2, 3]),
    # Test 7: Longer chain with a branch
    ({0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2], 4: [0, 5], 5: [4]}, 0, [0, 1, 2, 3, 4, 5]),
]


def run_tests() -> None:
    passed = 0
    for i, (graph, start, expected) in enumerate(TESTS, 1):
        result = depth_first_search(graph, start)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test {i}: {status} | got {result}, expected {expected}")
    print(f"\n{passed}/{len(TESTS)} tests passed")


if __name__ == "__main__":
    run_tests()