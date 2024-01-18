a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a==0:
    if b==0:
        print("pt co vo so nghiem")
    else:
        print("pt vo nghiem")
else:
    x=-b/a
    print("nghiem cua pt la :" ,x)