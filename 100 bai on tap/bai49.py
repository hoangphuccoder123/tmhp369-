a=input()
so="0123456789"
thuong="qưertyuiopasdfghjklzxcvbnm"
hoa="QƯERTYUIOPASDFGHJKLZXCVBNM"
d=ds=dt=dh=0
for i in range(len(a)):
    if a[i] in so:
        ds += 1
    elif a[i] in thuong:
        dt += 1
    elif a[i] in hoa:
        dh += 1
    else:
        d += 1
if d != 0 and ds != 0 and dt != 0 and dh != 0:
    print("True")
else:
    print("False")