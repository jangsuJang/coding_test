parent = []
for i in range(0,5):
    parent.append(i)

def find(x):
    global parent
    if x==parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if(x>y):
        parent[y] = x
    else:
        parent[x] = y


union(1,4)
print(parent)
union(2,4)

print(parent)

