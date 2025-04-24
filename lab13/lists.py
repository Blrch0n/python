def urj(z,n):
    k=0
    for i in range(len(z)):
        p=z[i]*n+k
        z[i]=p%10
        k=p//10
        if len(z)==i+1 and p>9:
            z.append(k)
    return z
def nem(z, z1):
    lz, lz1 = len(z), len(z1)
    min1 = min(lz, lz1)
    z3 = z[:] if lz >= lz1 else z1[:]

    k = 0
    for i in range(min1):
        p = z[i] + z1[i] + k
        z3[i] = p % 10
        k = p // 10

    idx = min1
    while k > 0 and idx < len(z3):
        p = z3[idx] + k
        z3[idx] = p % 10
        k = p // 10
        idx += 1

    if k > 0:
        z3.append(k)

    return z3

def nlist(g4):
    g5=list(g4)[::-1]
    for i in range(len(g5)):
        g5[i]=int(g5[i])
    return g5

z3=[0]

g4 = input("Үржүүлэх эхний тоо оруулах: ")
g5=input("Үржүүлэх дараагийн тоо оруулах: ")
for i in range(int(g4)):
    z3 = nem(z3,nlist(g5))
z3 = z3[::-1]
result = int(''.join(map(str, z3)))
print("Хариулт:",result,z3)