string1=input("Enter a string:")
string2=input("Enter another string:")
mid=int(len(string1)/2)
s=string1[:mid:] + string2[::]+ string1[mid::]
print(s)
