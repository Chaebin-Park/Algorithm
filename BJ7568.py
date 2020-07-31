#Chaebin Park
#20200706

num = int(input())

height_list = []
weight_list = []

for i in range(num):
    h, w = input().split()
    h = int(h)
    w = int(w)
    height_list.append(h)
    weight_list.append(w)

count = [0 for i in range(num)]

for i in range(num):
    for j in range(num):
        if height_list[i] > height_list[j]:
            count[i] += 1
        if weight_list[i] > weight_list[j]:
            count[i] += 1

for i in range(num):
    for j in range(num):

