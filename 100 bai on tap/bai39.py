n = int(input("Nhập một số nguyên dương: "))
n_str=str(n)
even_count=0
old_count=0
for digit in n_str :
    if int(digit)%2==0:
        even_count+=1
    else:
        old_count+=1 
    print(old_count,  even_count)