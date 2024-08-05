
l = []
l = list(input())
for char in l:
    if char == " ":
        l.remove(char)
s = set(l)
print(s)
