# variables for string and numbers
"""
name1="talha shabir"
age=22
print ("hello my name is ", name1,"or ma age is", age)
"""

# familiar Oprator or unfamiliar Oprator
"""
a=10
b=20
c=a+b
print(c)
"""
"""
a=20
b=200
a+=b
print(a)
"""
# data type
"""
1-string          2-Integer
3-float           4-boolean
5-complex         6-tuple
7-list            8-dictionary
9-set            10-frozenset
11-bytes         11-bytearray
"""
# if and else conditions
"""
num1=20
num2=20
if(num1<num2):
    print("num1 SMALLER  than num2")
elif(num1>num2):
    print("num1 is greater than num2")
else:print("both numbers are equal")
"""
# another example 
"""
myname="talha"
markes = 77

if(markes==90):
    print("talha is excelent / grade A")
elif(markes<90):
    print("talha is good / grade B")
else:
    print("talha is failed / grade F")
"""
# Nasted if and else 
"""
a="talha"
b="Mishal"
marks=5
Tmarks=7
Mmarks=6
if (marks == 10):
    if(Tmarks>=7) and (Mmarks>=6):
        print(a,b," excellent / grade A")
    else: print(a,b," have failed")
else : print(a,b," have failed")
"""
# list
"""
ls1=[1,2,3,4,5,6,7,8,9]
ls2=[10,11,12]
ls1.append(ls2)
print(ls1,type(ls1))
"""
"""
lst=[]
name=["talha "]
rollno=[20]
lst =name+rollno
print(lst)
"""
"""
lst1=[2,1,5,3,4]
lst2=[5,6,7,8,9]
# lst1.extend(lst2)
# del lst1[0] ....we will call index number
# lst1.remove[1]....there we will call direct number
# lst1.sort(reverse=True)....resverse sorting
# lst1.sort()...sorting
# lst1.pop(0) removing also through index
print(lst1)
"""
# Tuples
"""
tup=(1,2,3,4,5)
tup1=("talha", "shabir ","ahmed")
# print(type(tup),len(tup)) to finding lenght and type of tuple
# z=list(tup)
# z.insert(1,"talha")
# z.pop(1)...removing via index
# z.remove(1)...removing via value
y=list(tup1)
print(y[2])...directly print through index 
"""
# Dictionary
"""
mydic={"name":"talha","age":"20","city":"lahore"}
# print(dic["name"],dic["age"],)
# mydic.update({"name":"saad"})
# mydic.update({"fathername":"shabir"})
# mydic{'lastname'}="ahemd"
 Y=mydic.get("age")...for calling get or a diect key use a third variable
print(Y)
"""
"""
car = {
    "color":"pink",
    "model":19,
    "year":2019,
    "company":"toyota"
}
x=car.keys()
print(x)
car["color"]="white"
print(x)
"""

prnt = {
    "child1":{
        "name":"ashutosh",
        "age":24,
    },
    "child2":{
        "name":"Aslam",
        "age":30,
    },
    "child":{
        "name":"afaq",
        "age":12
    }
}
print(prnt)





# Sets
# set1={1,2,3,4,5,6,7,8,9,10}
# set1.add(11)
# print=(set1)





 





#Iteration or itrables
#give us the us the value on by one 
"""""
ls=["talha ","saad"," asad"]
ls=[1,2,3,4,5,6,7,8,9]
ls2=iter(ls)

print(next(ls2))
print(next(ls2))
print(next(ls2))
"""

#funtions and variables scop
# we will start funtion first and then we call it later
"""
def s():
    print(" hello word")
s()
"""
"""
def sum(P,Q,*R):
    print("HELLO WORD",P,Q,R)
sum(90,85,99,98)
"""
# Maps and filter
"""
def s(p)
    if n%2==0
    return
    """


# class and Onject


# Numpy
# import numpy
# ls=numpy .[1,2,3,4,5,5,6]

