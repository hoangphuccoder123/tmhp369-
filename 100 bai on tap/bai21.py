day = int(input())
month = int(input())
d31 = [1,3,5,7,8,10 ,12 ]
d30 = [4,6,9,11]
tong=0
for i in range (1,month+1):
    if i in d31:
        tong += 31
    elif i in d30:
        tong+=30
    else:
        tong+=28
    tong+=day-1
    print(tong)
    
        
