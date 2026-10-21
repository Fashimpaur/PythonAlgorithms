def insert_interval(intervals: list, insert_list: list) -> list:
    results = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < insert_list[0]:
        results.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] < insert_list[1]:
        insert_list[0] = min(insert_list[0], intervals[i][0])
        insert_list[1] = max(insert_list[1], intervals[i][1])
        i += 1
    results.append(insert_list)
    for j in range(i, n):
        results.append(intervals[j])
    return results


if __name__ == "__main__":
    result = insert_interval([[1, 3], [4,8], [10,12]], [1,9])
    print(result)
