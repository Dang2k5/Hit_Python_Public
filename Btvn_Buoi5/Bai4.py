<<<<<<< HEAD
my_dict = {
    "n" : 1500, "m" : 2, "CLUSTERS" : 3, "ITER" : 10000, "METHOD" : "FCM", "MEASURE" : "EUCLIDEAN", "YEARS" : 51
}
my_dict["MEASURE"] = "MANHATAN"
print(my_dict)
print(my_dict["METHOD"])
my_dict["LOSS FUNCTION"] = "NORM_2"
print(my_dict["LOSS FUNCTION"])
print(my_dict)
my_dict.pop("YEARS")
print(my_dict)
s = input("Nhap xau: ")
s1 = set()
for i in my_dict:
    s1.add(my_dict[i])
    if s == my_dict[i]:
        print("S trung voi thong so: ", i)
print(s1)
a = list(my_dict.values())
print('Values -> list:', a)
=======
my_dict = {
    "n" : 1500, "m" : 2, "CLUSTERS" : 3, "ITER" : 10000, "METHOD" : "FCM", "MEASURE" : "EUCLIDEAN", "YEARS" : 51
}
my_dict["MEASURE"] = "MANHATAN"
print(my_dict)
print(my_dict["METHOD"])
my_dict["LOSS FUNCTION"] = "NORM_2"
print(my_dict["LOSS FUNCTION"])
print(my_dict)
my_dict.pop("YEARS")
print(my_dict)
s = input("Nhap xau: ")
s1 = set()
for i in my_dict:
    s1.add(my_dict[i])
    if s == my_dict[i]:
        print("S trung voi thong so: ", i)
print(s1)
a = list(my_dict.values())
print('Values -> list:', a)
>>>>>>> 9b86c3a98c07c7904b7012920449c87e7c2b9208
