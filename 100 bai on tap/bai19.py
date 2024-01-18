import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta=b**2-4*a*c
if delta >0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta==0:
    x= -b / (2 * a)
    print("pt có nghiệm kép ")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-delta) / (2*a)
    x1 = complex(real_part, imaginary_part)
    x2 = complex(real_part, -imaginary_part)
    print("Phương trình có hai nghiệm phức:")
    print("x1 =", x1)
    print("x2 =", x2)