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
n # lst1.sort()...sorting
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
"""




# Sets
# set1={1,2,3,4,5,6,7,8,9,10}
# set1.add(11)
# print=(set1)


# while loops + brake 
"""
i=0
while i<=9:
 print(i)
 if i==4:
  break
 i+=1
""" 

# for loop + braKe
"""
Name=['talha','shabir', 'ahmad']
for x in Name:
 print(x)
 if x=='shabir':
  break
"""


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
"""
class student:
    def __inite__(self,name,age):
        self.name=name
        self.age=age
p1=student("Talha",23)
print(p1.name)
"""



# Numpy
"""
import numpy as np
array=np.array([1,2,3,4,5,5,6])
print(array)
"""
"""
import numpy as np
arry=np.array([[1,2,3,4,6],[7,9,1,5,9]])
print(arry)
# print(arry[2])....print any specific index
# print(arry[1:5]) ...slicing
# print(arry[1::]).....slic
# print(arry[2, 7::])

# print(arry.shape)finding the shape
"""


# Pandas
import pandas as pd
#By applying manual data 
# calories={"apple":50,"banana":14,"mangoa":16}
# show=pd.Series(calories)........... for series

# calories={"apple":[50],"banana":[46],"mangoa":[16]}
# show=pd.DataFrame(calories)............for data frame
# --------------------------------------------------------------------------
# by apply data through csv file
# df=pd.read_csv("test.csv")

# print(df.to_string)




# Matplotlib
# import matplotlib.pyplot as plt
"""
# import numpy as  np
# x=np.array([100,200,300,400,450])
# y=np.array([1,2,3,4,5])
# plt.plot(x,y)
# plt.show()
"""

import seaborn as sb
# seaborn plot list
"""
sb.displot
sb.barplot
sb.histplot
sb.kdeplot
"""


import numpy as np
import matplotlib.pyplot as plt

# Given data
cakes = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
prices = np.array([100, 150, 250, 300, 400, 450, 600, 800, 1000, 1500, np.nan])  # Missing value

# Remove the missing value for calculations
valid_prices = prices[~np.isnan(prices)]

# Number of data points
n = len(cakes) - 1  # excluding the missing value

# Calculate sums
sum_x = np.sum(cakes)
sum_y = np.sum(valid_prices)
sum_xy = np.sum(cakes[:n] * valid_prices)
sum_x2 = np.sum(cakes**2)

# Calculate slope (m) and intercept (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

# Predict the missing price value
missing_cake_value = cakes[-1]  # Cake value for the missing price
predicted_price = m * missing_cake_value + b

print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")
print(f"Predicted Price for Cake 12: ${predicted_price:.2f}")

# Plotting
plt.scatter(cakes[:-1], valid_prices, color='blue', label='Actual data')
plt.plot(cakes, m * cakes + b, color='red', linewidth=2, label='Fitted line')
plt.scatter(cakes[-1], predicted_price, color='green', marker='o', s=100, label='Predicted Price')
plt.xlabel('Cake (in pounds)')
plt.ylabel('Price (in dollars)')
plt.title('Cake Price Prediction')
plt.legend()
plt.grid(True)
plt.show()
