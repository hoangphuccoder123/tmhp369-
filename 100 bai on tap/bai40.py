n=int(input())
s=0
while n>0:
    z = n%10
    s+=z
    n//=10
print(s)

    