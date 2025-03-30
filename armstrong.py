num=int(input("Enter the number"))
temp=num
num_len=len(str(num))

sum_of_digit=0
while temp > 0:
    digit=temp%10
    sum_of_digit+=(digit ** int(num_len))
    temp//=10

if sum_of_digit==num:
    print(f"Number {num} is Armstrong")
else:
    print(f"Number {sum_of_digit} is Not Armstong")
