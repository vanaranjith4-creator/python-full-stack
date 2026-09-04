'''''
Tokens
===========
--->>>> tokens are the small units in the python.

1.Identifier
---------------
identifier is a name of variable or function or class

variables->

num ='python'
print(type(num))
----------------
functions->

def add_(a,b):
print(a+b)

add_(4,5)
---------------
class->

class details:
    pass
per_1=details


2.Key words
---------------
--->key words are already saved in python for a specific reason to run...

eg--
if 
else 
for
while 
return

3.Literals
-------------
--->> literals are the data types that need to be stored in variables...
eg--

num=9
name='teja'

4.Operators
---------------
=,+,-,/,*

5.Statements
----------------
-->> statements are the instructions given to the program....

num=50
let us consider age=30
  if age>=20:
        print(age)

6.Comments
--------------
--->> once the  comments are open the lines will never execute in the python file..

1.Single line comment(#)
------------------------
-->> it is used to comment only one line...

example:
age =20
if age>= 15: #this checks whether the age is grater or equal
print(age)

2.Multi line comment(''' ''',""" """)
---------------------------------------
--->> used to comment more than one line

------------------------------------------------------------


Variables rules
-------------------

Bad ways
-----------
--->> can't use number at first position
--->> can't use special char anywhere
--->> keywords
eg
--
2num=90
$num=90
n num=07
if=07

good ways
----------
-->small letters and cap letters,(_) under
eg
--
nUm_1=90
NUM_2=78
teja_garikapati =90

a = ('name':'teja','AC_num':'3244534456454646')
b = ('name':'ranjith','AC_num':'45356564664646')
c = ('name':'kumar,,'AC_num':'545445454454554555')

SBI_teja_details=('name':'teja','AC_num':'3244534456454646')

ICIC_ranjith_details=('name':'ranjith','AC_num':'45356564664646')


num=90
print(num)

num_3,num_2=56,89
print(num_3)
print(num_2)

a , b =45,67
print('a=',a)
print('b=',b)
a , b= b , a
print('a=',b)
print('b='b)

concatenation
---------------
--->>> the + will behave two ways for numeric its works normally and for other data datatypes like string, list ,tuple it concatenate


operators 
--------------
--->>operators are used to perform operations in variables     and the values

1.arthematic operator 
--------------------------
=,-,*,/,//,%
+-->> to add the values 

e.g.-->>

num =78.3
num_2=9
print(num+num_2)

(-)subtract --->>

a=9
b=8
print(a-b)

multiplication--->>

w=23
v=34
print(w*v)

/division--->>

v=84
r=43
print(v/r)

// float division--->>

a=23.44
b=32.4333
print(a//b)

% ---->>
v=8
n=2
print(v% n)

2.assignment operators 
-------------------------
=,+=,-=,*=,%=,/=


+= --->> is a increment operator 

a=0
print(a)
a +=1
print(a)


-= --->> decrement operator 

a= 89
a -= 10
print(a)

*=---->> multiply equal to 

a=25
a*=5
print(a)

/=---->>>

a=98
a /=2
print(a)


%= ----->>
a= 10000
a %= 2
print(a)


3.comparision operator


a=9
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

a=30
b=25
print(a>=b)
print(a<=b)

4.Logical operator
-----------------------
----->>>> and, or , not
e.g.
a=9
b=12
print(a>=b and a<=10)
print(a<=b and a<=10)
print(a>=b or a<=10)
print(not(a>=b or a<=10))

5.identity operator
-------------------------

a=45
b=45
print(id(a))
print(id(b))
print(a is b)

a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is b)
print(a == b)

a=[1,'python',2]
b=[2,1, 'python']
print(a == b)
print(a is b)


a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is not b)

6.membership operator
----------------------
in ,not in
e.g.
a='python'
print('y' in a)
print( 'i' in a)
print( 'i' not in a)

7.


































































































































'''
