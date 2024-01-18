chuoi=input()
so_in_hoa=0
so_in_thuong=0
so_so=0
for i in range(len(chuoi)):
    if chuoi[i].isupper():
        so_in_hoa+=1
    elif chuoi[i].islower():
        so_in_thuong += 1
    elif i.isdigit():
        so_so += 1

print("Số ký tự in hoa:", so_in_hoa)
print("Số ký tự in thường:", so_in_thuong)
print("Số ký tự số:", so_so)