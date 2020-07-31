import sys


def AC(command, max, arr):
    command.replace("RR", "")
    left, right = 0, 0
    is_reversed = False
    for c in command:
        if c == "R":
            is_reversed = not is_reversed
        elif c == "D":
            if is_reversed:
                right += 1
            else:
                left += 1

    if left + right <= max:
        result = arr[left:max - right]
        if is_reversed:
            return '[' + ','.join(reversed(result)) + ']\n'
        else:
            return '[' + ','.join(result) + ']\n'
    else:
        return 'error\n'


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        command = sys.stdin.readline()
        max = int(sys.stdin.readline())
        arr = sys.stdin.readline().rstrip()[1:-1].split(',')
        sys.stdout.write(AC(command, max, arr))
