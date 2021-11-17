A=set(input('dati elementele: '))
B=set(input('dati elementele: '))
a=set()
b=set()
for i in A:
    if ord(str(i))>=65 and ord(str(i))<=90 :
        a.add((i))
for i in B:
    if ord(str(i))>=65 and ord(str(i))<=90 :
        b.add((i))
print(a)
print(b)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))