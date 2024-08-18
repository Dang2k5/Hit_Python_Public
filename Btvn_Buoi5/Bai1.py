my_dict = {
    "001": 3.7,
    "002": 2.5,
    "003": 3.4,
    "004": 0.7,
    "005": 3.1,
    "006": 0.1
}
my_dict["007"] = 1.5
cnt = 0
my_list = []
for i in my_dict:
    if my_dict[i] >= 3.0 and my_dict[i] <= 3.5:
        cnt += 1
    if my_dict[i] < 2.0:
        my_list.append(i)
print("So sinh vien co diem tong ket trong [3.0, 3.5]: ",cnt)        
for i in my_list:
    my_dict.pop(i)
print(my_dict)