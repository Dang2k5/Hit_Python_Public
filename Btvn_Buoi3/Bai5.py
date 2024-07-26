n = int(input("Nhap n: "))
s = str(input("Nhap day so: "))
s = s.strip()
number = s.split()
numbers = list(map(int, number))
cnt = 0
result = []
for so in numbers:
    if so % 2 == 1:
        result.append(so)
        cnt += 1
print("So luong so thay ba thich la: ", cnt)
result.sort()
print("Cac so do la: ", " ".join(map(str, result)))
