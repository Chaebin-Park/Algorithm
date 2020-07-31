T = int(input())

for i in range(T):
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)

    floor = N % H
    room = int(N / H) + 1

    print(floor, room)
