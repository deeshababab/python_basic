num=int(input("Enter the number"))
n1=0
n2=1
count=0
if num>1:
    while count < num:
        print(n1)
        fib=n1+n2
        n1=n2
        n2=fib
        count=count+1