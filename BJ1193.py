# Chaebin Park
# 20200703

num = int(input())

cmp = 1
floor = 2
loc = 0

while num >= cmp:
    print("cmp : ", cmp, " floor : ", floor, " loc : ", loc)
    if num == 1:
        loc = 1
        break
    loc = num - cmp
    cmp += floor
    floor += 1

floor -= 1

if floor % 2:  # odd
    print(floor - loc + 1, "/", loc)
else:  # even
    print(loc, "/", floor - loc + 1)
