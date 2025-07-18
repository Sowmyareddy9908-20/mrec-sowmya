second=3
second=second+1
second=second+1
print(second)
b=8//4
print(b)

#for loop
a=1
b=2
c=9
print(a)
print(b)
print(c)

#array
#a=[3,"sowmmya reddy",5,6,7]
#print(a[0])
#print(a[2])
#print(a[1])

a=[3,"sowmmya reddy",5,6,7]
for i in range(5):
    print(a[i])

#single value
print(list(range(12)))
#2 variables
print(list(range(2,4)))
#skipping number
print(list(range(2,9,2)))

arr=[5,6,7,8,9]
for i in arr:
    print(i)
    print("bunny")

arr=[1,3,4,2,1,2,1,1,1,1,1,3,46,2]
count=0
for i in arr:
    if i==1:
        count=count+1
print(count)

arr=["ammu","chinnu","ammu",2,3]
count=0
for i in arr:
    if i=="ammu":
        count=count+1
print(count)
# using range
arr=[3,4,2,3,2]
ans=0
for i in range(4):
    if arr[i]==2:
        ans=ans+1
print(ans)

'''we are printing index values so output will be 0,1,2,3'''
arr=[6,7,8,9]
for i in range(4):
    print(i)

arr=[6,7,8,9]
for i in range(4):
    print(arr[i])
