n = int(input("Nhập số nguyên dương n: "))
is_power_of_two = True
while n > 1:
    if n % 2 != 0:
        is_power_of_two = False
        break
    n = n // 2
if is_power_of_two:
    print(n, "là số dạng 2^k.")
else:
    print(n, "không là số dạng 2^k.")