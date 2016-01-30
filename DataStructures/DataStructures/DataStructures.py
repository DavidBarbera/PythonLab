#Some data structures and very interesting input output formatting ways with Python


#sets
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
print fruit
print 'orange' in fruit

#dictionaries
tel = {'jack': 4098, 'shape': 4139}
tel['guido'] = 4127
print tel
del tel['shape']
tel['irv'] = 4127
print tel
print 'guido' in tel
tel['may'] = 4128,4129
print tel
print tel['may']

for x in range(1,11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

#Example how to read multiple formatted input data at once and "unpack it"
#User input: Krishna 67 68 69
n = int(raw_input())
items=[x for x in raw_input().split(" ")]
name, m1, m2, m3 = items  #unpacking
print items
print name
print m1
print m2
print m3

#using it to make a dictionary
n = int(raw_input())

marks={}

for i in range(0,n):
    items =[x for x in raw_input().split(" ")]
    name, m1, m2, m3 = items
    marks[name]=int(m1),int(m2),int(m3)

print marks


#using it to make a dictionary
n = int(raw_input())

marks={}

for i in range(0,n):
    items =[x for x in raw_input().split(" ")]
    name, m1, m2, m3 = items
    marks[name]=int(m1),int(m2),int(m3)
    
name = str(raw_input())
a,b,c=marks[name]
print round((a+b+c)/3,3)

#using it to make a dictionary
n = int(raw_input())

marks={}

for i in range(0,n):
    items =[x for x in raw_input().split(" ")]
    name, m1, m2, m3 = items
    marks[name]=float(m1),float(m2),float(m3)
    
name = str(raw_input())
a,b,c=marks[name]
d = (a+b+c)/3
print("{0:.2f}".format(d)) #returns 56.00

# this version of print is capable of printing out without spaces
# output is 123, rather then 1 2 3
from __future__ import print_function
import sys
n = int(raw_input())
a= n-2
b= n-1
c= n
    
print(a,b,c, sep='', file=sys.stdout)

#and this is a generalisation for any N integer
from __future__ import print_function
import sys
n = int(raw_input())
    
map(lambda x:print(x,sep='',end='', file=sys.stdout),range(1,n+1))

    