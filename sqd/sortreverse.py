import sys


if __name__ == "__main__":
    arr = list(sys.stdin.readline().strip())
    arr.sort(reverse=True)
    print("".join(repr(int(e)) for e in arr), sep="")
