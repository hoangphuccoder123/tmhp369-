A = int(input("Nhập số nguyên A: "))
fibonacci_1 = 1
fibonacci_2 = 1
fibonacci_max = fibonacci_2
while fibonacci_max <= A:
    fibonacci_max = fibonacci_1 + fibonacci_2
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_max
fibonacci_max = fibonacci_1  
print("Số Fibonacci lớn nhất nhưng không vượt quá", A, "là", fibonacci_max)