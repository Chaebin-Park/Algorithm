# Chaebin Park
# 20200702

total = int(input())

div_3 = 0
div_5 = int(total / 5)
total = total % 5

while div_5 >= 0:
    # print("LOOP | T : ", total, " 5 : ", div_5, " 3 : ", div_3)
    if total % 3 == 0:
        div_3 = int(total / 3)
        break
    div_5 -= 1
    total += 5

# print("BREAK | T : ", total, " 5 : ", div_5, " 3 : ", div_3)

if div_5 < 0:
    print(-1)
else:
    print(int(div_3 + div_5))
