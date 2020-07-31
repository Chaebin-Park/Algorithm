import sys
import operator


def average(arr, N):
    return round(sum(arr) / N)


def median(arr, N):
    return arr[int(N // 2)]


def mode(arr, N):
    cnt_dict = {}

    for i in arr:
        try:
            cnt_dict[i] += 1
        except:
            cnt_dict[i] = 1

    val_ls = list(cnt_dict.values())
    val_ls.sort(reverse=True)
    mode_ls = []
    key_ls = list(cnt_dict.keys())

    for i in range(len(key_ls)):
        key = key_ls[i]
        if cnt_dict[key] == val_ls[0]:
            mode_ls.append(key)

    if len(mode_ls) == 1:
        return mode_ls[0]
    else:
        mode_ls.sort()
        return mode_ls[1]


def range_arr(arr, N):
    return arr[N-1] - arr[0]


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []

    # input N integer data
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))

    # sort arr data
    arr.sort()

    # The arithmetical average(AMA)
    # 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    print(average(arr, N))
    # Intermediate value(IV)
    # 둘째 줄에는 중앙값을 출력한다.
    print(median(arr, N))
    # Best value(BV). if BV is many then print second smallest value
    # 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    print(mode(arr, N))
    # Range of array
    # 넷째 줄에는 범위를 출력한다.
    print(range_arr(arr, N))
