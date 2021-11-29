def sum_n_nos(n):
    if n<=1:
        return 1
    else:
       return n+sum_n_nos(n-1)

num=int(input("enter a no"))
if num<0:
    print("enter positive number")
else:
    print("the sum is",sum_n_nos(num))