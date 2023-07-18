# q1
# name="ajay devgan"
# l=[1,2,3,"ajay",True,10.5]
# a=5.5
# t=(1,2,3,"ajay",True)

# q2
# 1.string
# 2.string
# 3.list
# 4.integer

# q3
a=10
b=5
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# q4
a=[1,2,3,4,5,6,"ajay","akshay",True,10.5]
for i in a:
  print(i)
  print(type(i))

# q5
n=int(input("enter the number= "))
m=int(input("enter the second number = "))
while(n%m==0):
  a=n/m
  print(a)
  break
else:
  print("not divisible")

# q6
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in number:
  if(i%3==0):
    print("divisible by 3")
  else:
    print("not divisible")

# q7
# strings are immutable ,it cannot be changed once it is created
name="ajay"
name[0]="t"
print(name)

# lists are mutable it can be changed using indexes
b=[1,2,3]
b[0]=100
print(b)
