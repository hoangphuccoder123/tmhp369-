n=[]
while True:
    n=int(input())
    if n==-1:
        break
    n.append(n)
if len(n)>0:
    max_n=max(n)
    min_n=min(n)
print( max_n, min_n)