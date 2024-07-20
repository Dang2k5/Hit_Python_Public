n = int (input("Nhap n: "))
def armstrong(n):
    res = 0
    while(n > 0):
        res += (n % 10) ** 3
        n /= 10
    return res
for i in range(1, n + 1, 1):
    if armstrong(i) == i:
        print(i)