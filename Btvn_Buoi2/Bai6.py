n = int(input("Nhap n: "))
for i in range(1, n + 1):
    t = 0
    for j in range(1, i):
        if i % j == 0:
            t = t + j
    if t == i:
        print(i)