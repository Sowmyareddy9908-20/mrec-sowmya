s="abcde"
print(s[4])

#for reversing a list
s="bcde"
print(len(s))
li=("12344")
n=len(li)
print(n)

#for i in range(5,0,-1):
 #   print(i)
print(list(range(5,0,-1)))

#reversing a list
s="abcd" 
print(s[3]+s[2]+s[1]+s[0])
print(list(range(3,-1,-1)))

s="ABCD"
ans=s[3] #D
ans=ans+s[2] #DC
ans=ans+s[1] #DCB
ans=ans+s[0] #DCBA
print(ans)

s="ABCD"
ans=""
for i in range(3,-1,-1):
    ans=ans+s[i]
    print(ans)

#reversing a list
li=[5,8,9,5,1,4,54,3]
n=len(li)
for i in range(n-1,-1,-1):
    print(li[i])

#reversing for string
s="sowmya"
ans=""
n=len(s)
for i in range(n-1,-1,-1):
    ans=ans+s[i]
    print(ans)

#reversing using slicing
s="bunny"
print(s[::-1])

#check whether palindrome or not
b="pop"
ans=""
for i in range(len(b)-1,-1,-1):
    ans=ans+b[i]
if ans==b:
    print("YES")
else:
    print("NO")

#change False into True
a=False
if 3+1==4:
    a=True
if a:
    print("hello")

for i in range(3):
    print(i,i+2)

#palindrome reverse
s="abccba"
n=3
m=len(s)
for i in range(n):
    print(s[i],s[m-1-i])

s="abba"
n=len(s)//2#use only /2
m=len(s)
for i in range(n):#here u use int(n)
    print(s[i],s[m-1-i])

n=5/ 2
print(int(n))  

for i in range(5):
    print(i)
    if i==3:
        break


s="cdef"
ans=""
for i in range(3,-1,-1):
    ans=ans+s[i]
    print(ans)

q="manideepreddy"
ans=""
for i in range(len(q)):
    ans=ans+q[i]
    print(ans)

arr=[1,3,5,2,2,4,5,6,3,2]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])


s="sowmya"
ans=""
for i in range(len(s)):
    ans=ans+s[i]
    print(ans)
    
s="sowmya"
ans=""
for i in range(len(s)-1,-1,-1):
    ans=ans+s[i]
    print(ans)
    
li=[1,3,2,3,5,4]
ans=""
for i in range(len(li)-1,-1,-1):
    ans=ans+str(i)
    print(ans)

li=[5,9,8,1]
for i in range(len(li)-1,-1,-1):
    print(li[i])

n=3
mul=n*2
for i in range(n):
    print(i,mul-1-i)

s="abcdef"
n=3
mu=n*2
for i in range(n):
    l=s[i]
    r=s[mu-1-i]
    print(l,r)

# final palindrome 
s="abcddcba"
n=len(s)//2
mu=len(s)
for i in range(n):
    print(n,mu-1-i)