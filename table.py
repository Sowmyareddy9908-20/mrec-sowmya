#in simple way
for i in range(0,11):
     n=2
     print(n,"x",i,"=",n*i)

#using functions
def table():
    for i in range(0,11):
        n=5
        print(n,"x",i,"=",n*i)
table()

def table():
    for i in range(0,21):
        print(n,"*",i,"=",i*n)
        # formatted string : print(f"{n}*{i}={n*i}")
table()

# for even
def table():
    for i in range(0,11):
        if i%2==0:
            print(n,"X",i,"=",2*i)
table()

# using not equal
def table():
    n=2
    for i in range(11):
        if i%2 !=0:
            print(n,"x",i,"=",n*i)
table()