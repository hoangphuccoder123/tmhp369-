a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or c == a:
        if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Các số a, b, c không thể tạo thành độ dài của một tam giác")