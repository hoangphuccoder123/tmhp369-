month=int(input())
year =int(input())
if month in [ 1,3,5,7,8,10,12]:
    num_days=31
elif month in [4,6,9,11]:
    num_days=30
elif month ==2:
    if ( year %4 ==0 and year %100!=0) or (year %400==0):
        num_days=29
    else:
        num_days=28
else:
    print("thang ko hop le!")
if month in range (1,13):
    print(num_days,month,year)
