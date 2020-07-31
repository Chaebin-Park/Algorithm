# Chaebin Park
# 20200702

num = int(input())
floor = 1
seq = 6
cmp = 1

while num > cmp:
    if num == 1:
        break
    cmp += seq
    seq += 6
    floor += 1

print(floor)
