# functions
n=3
s="sowmya"
for i in range(3):
    print(s)

n2=4
s2="boom"
for i in range(n2):
    print(s2)

#for reusability we use functions:
def sowmya():
    print("hello machas")
    for i in range(2):
        print("reddy")
sowmya()#function call

def chinnu(n):
    print("hy")
    for i in range(n):
        print("hello")
    print("bye")
chinnu(2)
chinnu(3)

def kabali(n,s):
    for i in range(n):
        print(s)
    
kabali(1,"mani")
kabali(5,"age")
kabali(6,"weight")

#
def fun():
    print("myself sowmya")
print("started")
fun()
print("ended")

#return keyword

#today
def fun():
    print("sowmyareddy")
    print("lingampally")
fun()

def kabali():
    print("dairymilk")
    for i in range(4):
        print("kitkat")
    print("milkybar")
kabali()
# kabali()

#for repeated 
def kabali(n):
    print("hy")
    for i in range(n):
        print("hello")
    print("bye")
kabali(2)

 # using 2 variables
def kabali(n,s):
    print(n,s)
kabali(3,"sow")
kabali(1,"man")
kabali(2,"mvn")

#for forloop
def kabali(n,s):
    for i in range(n):
        print(s)
kabali(2,"mum")
kabali(3,"gun")

def fun():
    print("i am middle")
print("just now started")
fun()
print("just now ended")

def marrige():
    print("i am getting married")
print("tommorow is my marrige")
marrige()
print("yesterday i have completed")

# return in function
def fun():
    print("it is a first return statement")
    return "im second stmt"
macha=fun()
print(macha)

def fun(n):
    print("hello in function")
    return n+5
bunny=fun(5)  or print(fun(8))
print(bunny)
print(fun(2))

#function with return stmt
def fun():
    print("i should sucess")
    return "yes for surely"
print(fun())