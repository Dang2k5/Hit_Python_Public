s = input("Nhap chuoi: ").strip()
my_dict = {}
for i in s:
    my_dict[i] = my_dict.get(i, s.count(i))
print(my_dict)