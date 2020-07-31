import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    mem_info = []
    for _ in range(N):
        age, name = sys.stdin.readline().split()
        age = int(age)
        mem_info.append([age, name])

    mem_info.sort(key=lambda x: x[0])

    for age, name in mem_info:
        print(age, name)

