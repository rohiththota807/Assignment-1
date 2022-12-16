even=0
odd=0
num=[]
series=int(input("enter the total no of elements in series:"))
for i in range(1,series+1):
    value=int(input("enter the value of %d series:"%i))
    num.append(value)

for j in range(series):
    if num[j]%2==0:
        even+=1
    else:
        odd+=1
print("\nNumber of even numbers : ",even)
print("Number of odd numbers : ",odd)
