# string_count-digit.py
# count no of upper case ,lower case,digits and whitespace in a string


x=input("Enter a string")
ct1=0
ct2=0
ct3=0
ct4=0
for i in range(len(x)):
    if x[i].isupper():
        ct1+=1
    elif x[i].islower():
        ct2+=1
    elif x[i].isdigit():
        ct3+=1
    elif x[i].isspace():
        ct4+=1
print("The uppercase character is {}".format(ct1))
print("The lowrcase character is {}".format(ct2))
print("The digit is {}".format(ct3))
print("The whitespace is {}".format(ct4))


