def count_place(place):
    p=[]
    for i in place:
        if len(i)>=5:
            p.append(i)
    print(p)

place=[]
print("enter place name:")
for i in range(5):
    x=input()
    place.append(x)
count_place(place)