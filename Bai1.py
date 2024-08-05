t = tuple(input().strip())
s = set()
for i in t:
    a = t.count(i)
    if(a % 5 == 0 and a % 2 != 0):
        s.add(i)
print(s)