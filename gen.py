import random
list1 = []
for i in range(80):
    list2 = []
    for j in range(80):
        list2.append(random.randint(-100000,100000))
    list1.append(list2)
with open("./data2.txt","w") as f:
    f.write(str(list1))