"""
Write a function that, given an array A consisting of integers (fuel demands for
cars in the queue) and integers X, Y, Z (fuel available in each of the three
pumps), returns the maximum waiting time for a car. If any car cannot refuel,
return -1.
"""

def solution(A, X, Y, Z):
    fuel_pumps = [X, Y, Z]
    fuel_pumped = [0, 0, 0]
    max_wait = 0

    for needed in A:
        pump_id = next((i for i, f in enumerate(fuel_pumps) if f >= needed), -1)
        if pump_id == -1:
            return -1

        # waiting time for this car is how much that pump already dispensed
        max_wait = max(max_wait, fuel_pumped[pump_id])

        # update pump state
        fuel_pumps[pump_id] -= needed
        fuel_pumped[pump_id] += needed

    return max_wait


if __name__ == "__main__":
    print(solution([2, 8, 4, 3, 2], 7, 11, 3))  # 8
    print(solution([2, 8, 4, 2], 7, 11, 3))     # 8
    print(solution([5, 6, 7], 5, 5, 5))         # -1 (last car cannot refuel)
    print(solution([1, 2, 3], 3, 3, 3))         # 1
