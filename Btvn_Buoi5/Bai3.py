<<<<<<< HEAD
import random
n = int(input("Nhap n: "))
l = ["CNTT", "KHMT", "KTPM", "HTTT"]
my_dict = dict()
for i in range(n):
    my_dict[f"Account{i}"]= {
        "Username": + 20236000 + i + 1 , "Password": random.choice(l) + str(20236000 + 1 + i)
    }
=======
import random
n = int(input("Nhap n: "))
l = ["CNTT", "KHMT", "KTPM", "HTTT"]
my_dict = dict()
for i in range(n):
    my_dict[f"Account{i}"]= {
        "Username": + 20236000 + i + 1 , "Password": random.choice(l) + str(20236000 + 1 + i)
    }
>>>>>>> 9b86c3a98c07c7904b7012920449c87e7c2b9208
print(my_dict)