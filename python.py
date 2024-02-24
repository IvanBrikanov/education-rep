a = str(input())
b = str(input())

c = {}
v = {}

for i in a:
    c[i] = int(c.get(i, 0)) + 1
for j in b:
    v[j] = int(v.get(j, 0)) + 1

if c == v:
    print('YES')
else:
    print('NO')с
    
test vim page;
