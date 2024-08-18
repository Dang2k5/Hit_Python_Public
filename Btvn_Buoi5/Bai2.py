<<<<<<< HEAD
s = input("Nhap chuoi: ").strip()
my_dict = {}
for i in s:
    my_dict[i] = my_dict.get(i, s.count(i))
=======
s = input("Nhap chuoi: ").strip()
my_dict = {}
for i in s:
    my_dict[i] = my_dict.get(i, s.count(i))
>>>>>>> 9b86c3a98c07c7904b7012920449c87e7c2b9208
print(my_dict)