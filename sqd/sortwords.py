import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    word_dict = {}
    for _ in range(N):
        word = sys.stdin.readline().strip()
        word_dict[word] = len(word)

    sorted_dict = sorted(word_dict.items(),
                         key=lambda x: x[1])
    max = int(sorted_dict[len(sorted_dict)-1][1])

    for num in range(1, max+1):
        tmp_arr = []
        i = 0
        while True:
            try:
                if num == sorted_dict[i][1]:
                    tmp_arr.append(sorted_dict[i][0])
                i += 1
            except IndexError:
                break
        tmp_arr.sort()
        for e in tmp_arr:
            print(e)
