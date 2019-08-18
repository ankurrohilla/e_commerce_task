from django.test import TestCase

# Create your tests here.
x= 0
y= x or 1
z =y and x
list1=[0,0,1]
list2=[1,1,0]

if any(list2) and z:
    print(1)
elif all(list1) or y:
    print(2)
else:
    print(3)