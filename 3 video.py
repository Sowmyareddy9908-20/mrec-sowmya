arr=[1,2,1,3,2,4,7,1,1]
ans=0
for i in arr:
    if i==1:
        ans=ans+1
print(ans)

'''using range'''
li=[1,4,2,3,4,4,4,7,8,4]
ans=0
for i in range(8):
    if li[i]==4:
        ans=ans+1
print(ans)

arr=[2,3,4,7,4,2,1,2]
b=len(arr)
print(b)

arr=[2,3,4,7,4,2,1,2]
b=len(arr)
ans=0
for i in range(b):
    if arr[i]==2:
        ans=ans+1
print(ans)

print(8%3)
print(6%3)

arr=[3,6,8,7,9,15,12]
ans=0
for i in arr:
    if i%2==0:
        ans=ans+1
print(ans)

#OR AND OPERATOR
if 1+2==3 or 5+2==1:
    print("bunny")
else:
    print("mani")

li=[2,3,12,1,6,18]
ans=0
for i in li:
    if(i%3==0 and i%2==0):
        ans=ans+1
print(ans)