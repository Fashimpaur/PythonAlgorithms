from tomlkit import key

intervals=[[1,5], [3,3], [6,8]]

def can_attend(intervals):
    if not intervals:
        return True
    intervals.sort(key=lambda x:x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

if __name__ == '__main__':
    can_attend(intervals)
