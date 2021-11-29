def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*factorial(num-1)

n=int(input("Enter a number:"))
if n<0:
    print("Enter positive number")
else:
    fact=factorial(n)
    print(f"The factorial of {n} is {fact}")