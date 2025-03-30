low=int(input("Enter the lower range"))
high=int(input("Enter the higher range"))

for i in range(low,high+1):
    len_num=len(str(i))
    sum_digit=0
    temp=i
    while temp > 0:
        digit=temp % 10
        sum_digit+=digit ** int(len_num)
        temp//=10

    if sum_digit==i:
        print(f"Number {sum_digit} is armstrong")


