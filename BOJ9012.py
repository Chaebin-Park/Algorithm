# 20200707

def check(list):
    chk = 0
    for i in range(len(list)):
        if list.pop() == ")":
            chk += 1
        else:
            chk -= 1
        if chk < 0:
            break

    return chk


if __name__ == "__main__":

    num = int(input())
    result = []

    for i in range(num):
        bracket = list(input())
        if check(bracket) != 0:
            result.append("NO")
        else:
            result.append("YES")

    for i in range(num):
        print(result[i])
