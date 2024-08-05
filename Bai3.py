n = int(input("Nhap n: "))
my_dict = {}

for i in range(n):
    x = input("Nhap ten: ")
    y = int(input("Nhap diem: "))
    my_dict[x] = y
min = my_dict[x]
for i in my_dict:
    if(my_dict[i] < min):
        min = my_dict[i]
        res = i
print(res)