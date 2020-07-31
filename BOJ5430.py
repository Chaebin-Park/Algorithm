# 20200713
# BOJ5430 AC

from collections import deque
import sys


if __name__ == "__main__":
    T = int(input())

    flag = True
    is_reversed = False
    result = []

    for i in range(T):
        command = list(sys.stdin.readline().strip())
        max = int(sys.stdin.readline().strip())
        #input_list = deque(map(int, sys.stdin.readline().strip().replace('[', "").replace(']', "").split(',')))
        input_list = sys.stdin.readline()[:-1].split(',')
        print(input_list)

        """
        if not(max == len(input_list)):
            print("error")
            continue

        for i in range(len(command)):
            if command[i] == "R":
                is_reversed = not is_reversed
            elif command[i] == "D":
                if len(input_list):
                    if is_reversed:
                        input_list.pop()
                    else:
                        input_list.popleft()
                else:
                    flag = False
                    break

        if flag:
            if is_reversed:
                input_list.reverse()
                print(str(list(input_list)).replace(' ', ''))
            else:
                print(str(list(input_list)).replace(' ', ''))
        else:
            print("error")
        """