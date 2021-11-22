#interchange the characters

s=input("Enter a string:")
x=len(s)
print(x)
s1=s[x-1]+s[1:x-1]+s[0]
print(s1)