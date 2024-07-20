n = int (input( "Nhap n: "))
def tongchuso(n) :
    result = 0
    while n > 0: 
        result += n % 10
        n //= 10
    return result 
print("Tong cac chu so trong n la: ", tongchuso(n))
   
m = int (input("Nhap m: "))
def tinhuoc(m): 
    res = 0
    for i in range(1, m + 1, 1):
        if m % i == 0:
            res += i
    return res
print("Tong cac uoc cua m la: ", tinhuoc(m))
a = int (input("Nhap a: "))
b = int (input("Nhap b: "))
c = int (input("Nhap c: "))
def checktamgiac(a, b, c):
    if a == b == c :
        print("Tam giac deu")
    elif a == b or b == c or c == a:       
        print("Tam giac can")
    elif a ** 2 + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a :
        print("Tam giac vuong") 
    elif a ** 2 + b ** 2 < c ** 2 :
        print("Tam giac tu")
    else:
        print("Tam giac nhon")
print(checktamgiac(a, b, c))
   
    
    


    
    

