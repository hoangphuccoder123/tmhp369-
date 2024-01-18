n=input()
s=0
so_hien_tai=""
for ky_tu in n :
    if ky_tu.isdigit():
        so_hien_tai=+ky_tu
    elif so_hien_tai:
        s+=int(so_hien_tai)
        so_hien_tai=""
if so_hien_tai:
    s+=int(so_hien_tai)
print(s)