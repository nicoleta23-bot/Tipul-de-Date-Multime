A=set(input('dati elementele:'))
B=set(input('dati elementele:'))
a=set()
b=set()
for i in A:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        a.add(int(i))
for i in B:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        b.add(int(i))
print(a)
print(b)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))