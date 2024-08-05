x = int(input("Nhap x: "))
a = [1 ,2 , 3]
cnt = 0
while(x > 0):
    if(x > max(a)):
        x = x - max(a)
        cnt += 1
    else: 
        cnt = cnt + 1
        break
print(cnt)