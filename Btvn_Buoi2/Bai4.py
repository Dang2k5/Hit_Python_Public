n = int(input("Nhap n: "))
def fibo(n):
    fibo  = []
    a, b = 0, 1
    for i in range(n): 
        fibo.append(a)
        a , b = b, a + b
    return fibo
print("Ket qua = ", fibo(n))