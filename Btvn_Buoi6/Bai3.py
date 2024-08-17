def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        mul= 1
        for i in args:
            mul *= i
        return mul
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else: print("Invalid operation")
s = input("Nhap chuoi: ")
a, b, c, d, e, f, g = 1 ,2 ,3 ,4 ,5 ,6 ,7
result = calculate(s, a, b, c, d, e, f, g)
print(result)