from heapq import heapify, heappush, heappop

target = 1
k = 3


def k_closest_integer(nums, t, step):
    h_arr = []
    diff_dict = {}
    result = []

    for x in nums:
        diff = abs(t - x)
        if diff in diff_dict:
            diff_dict[diff].append(x)
        else:
            diff_dict[diff] = [x]
            heappush(h_arr, diff)

    while h_arr and len(result) < step:
        diff = heappop(h_arr)
        for val in sorted(diff_dict[diff]):  # ties: smaller value first
            if len(result) >= step:
                break
            result.append(val)

    return result


get_k_closest = k_closest_integer


def main():
    arr = [-1, 0, 1, 4, 6]
    target = 1
    k = 3
    result = k_closest_integer(arr, target, k)
    print(result)  # [5, 7, 8]


if __name__ == "__main__":
    main()




