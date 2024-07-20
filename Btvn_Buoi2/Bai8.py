n = int(input("Nhap n: "))
def giaithua(n):
    P = 1
    for i in range(1, n + 1):
        P *= i
    return P
for i in range(0, n + 1):
    for j in range(n - i + 1):
        print(end = " ")
    for j in range(i + 1):
        print(giaithua(i) // (giaithua(i -j) * giaithua(j)), end = " ")
    print()
