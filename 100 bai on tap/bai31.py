def tim_uoc_chung(a,b): 
    uoc_chung=[]
    for i in range(1, min(a, b) + 1):
        if a%i==0 and b%i==0:
            uoc_chung.append(i)
    return uoc_chung
a=int(input())
b=int(input())
uoc_chung_ab= tim_uoc_chung(a,b)
print(uoc_chung_ab)
