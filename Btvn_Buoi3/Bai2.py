k = int(input("Nhap k: "))
a = [int(input(f"a[{i}]: ")) for i in range(0, k)]
n = int(input("Nhap so dong n: "))
m = int(input("Nhap so cot m: "))
b = []
if n * m > k:
    print("NO")
else:
    for i in range(n):
        row = a[i * m : (i + 1) * m]
        b.append(row)
    print("B = ", b)