'''
4/3/2025

1.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

'''

'''
a=eval(input("Enter the List:"))#enter the input may be 10,20,30
e=eval(input("Entee the element need to be search in the list:"))#maybe 20
    
for i in range(len(a)):
    if a[i]==e :
        print(F"Found  at  index {i}")#found at index a[1]
        break
            
else:
    print("Not  found")

'''

'''
2.Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''

'''
sum=c=0 

try:
    while(True):
        e=eval(input("Enter input  (-1  to  stop)  :"))
        if(e==-1):
            break 
        
        sum+=(e)
        c+=1 
        
        
    print("Average :",sum/c)
    
except:
    print("Don't enter sequence None complex")
    
''' 

'''
5/3/2025

1.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''

'''
a=eval(input("List:"))#enter list maybe 19,20,25,30,25
e=eval(input("element:"))#25
c=0
for i in range(len(a)):
    if a[i]==e:
        print(F"{a[i]} is fount at index {i}")#prints the value found at index a[2]
        c+=1 
        
if(c!=0):
    print(F"{e} is found {c} times")#found 2 times
    
else:
    print("not found")
    
'''


'''
2.Modify  following   program  with  walrus  operator average -1 
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''


'''
try:
    sum=c=0 
    while((x:=eval(input("Enter input  (-1  to  stop)  :")))!=-1):
        sum+=x 
        c+=1 
        
    print(F"Average: {sum/c}")
    
except:
    print("Don't enter sequence or complex and 1st i/p need not be -1")
        
'''

'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8    7   40    35.6
    What  is  the  largest  command  line  input ?  --->	40
    What  is  argv ?  ---> ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?  ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  --->  '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->  Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  --->	Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->	'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  ---> Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''

'''

import sys 
from sys import argv

try:
	a=[]

	for i in range(1,len(argv)):
		a.append(eval(argv[i]))#the a is empty before appending, after append it maybe any int,flot etc
		
	if(len(a)==0):
		print("enter at least 1 element to find max ")

	else:
		print(max(a))

except:
	print("enter same type of elements to find max without complex")


'''


'''
4.Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  --->	len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  ---> Pls  send  number  inputs
'''

'''

import sys 
from sys import argv

try:
	a=[]
    
	for i in range(1,len(argv)):
		a.append(eval(argv[i]))#the a is empty before appending, after append it maybe any int,flot etc
		
	if(len(a)==0):
		print("enter at least 1 element to find avg ")

	else:
		avg=sum(a)/len(a)
		print(F"Average :{avg}")

except:
	print("enter only int Float bool")#don't send input like strings
	
'''


'''
5.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''

'''

import sys 
from sys import argv

try:
	a=[]
    
	for i in range(1,len(argv)):
		a.append(eval(argv[i]))#the a is empty before appending, after append it maybe any int,flot etc
		
	if(len(a)==0):
		print("enter at least 1 element to find avg ")

	else:
		a.sort()
		print("Ascending :",*a)
        
		a.sort(reverse=True)
		print("Descending :",*a)

except:
	print("enter only int Float bool or only strings or lists or tuple but don't give mixed type ")
'''

'''6/3/2025 
#1.
a = 'Rama Rao'
print(a [ : 7 : 2]) #[0:7:2] Rm a
print(a [ : 7]) #[0:7:1] Rama Ra
print(a [2 : 4]) #[2:4:1] ma
print(a [2 : ]) #[2:len(a):1] ma Rao 
print(a [ : 4 ]) #[0:4:1] Rama 
print(a [ : : 2]) #[0:len(a):2] Rm a 
print(a [-6 : -1]) #[-6:-1:1] ma Ra
print(a [-6 : ]) # [-6:len(a):1] ma Rao 
print(a [: -4 : -1]) #[-1:-4:-1] oaR
print(a [-3 : -1]) # [-3:-1:1] Ra
print(a [-3 : ]) # [-3: len(a) :1] Rao 
print(a [ : : ]) #[0:len(a):1] Rama Rao
print(a [ : ]) #[0:len(a):1] Rama Rao
print(a [ : : -1]) #[-1:-len(a)-1:-1] oaR amaR
print(a [ : : -2]) #  a[-1 : -len(a)-1 : -2] oRaa
print(a [ -2 : : -2]) #[-2: -len(a)-1:-2] a m R
print(a [2 : 8]) #[2:8:1] ma Rao
print(a [2 : 8 : -1]) #[2:8:-1] # empty string 
print(a [ : -6 : -1]) #[-1:-6:-1] oaR a
print(a [2 : -3]) #[2:-3:1] ma<s>
print(a [1 : 6 : 2]) #[1:6:2] aaR
print(a [ : -5 : -5]) #[-1:-5:-5] o
print(a [2 : -5]) #[2:-5:1] #m
print(a [2 : -5 : 2]) #[2:-5:2] #m
print(a [ : 0 : -1]) #[-1:0:-1] #oaR ama
print(a [-5 : 0 : -2]) #[-5:0:-2] #aa

'''


'''
2.Write  a  program  to  concatenate  two  strings  separated  by  space  
but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Enter first string: JAVA
Enter second string: PYTHON
Result  :   PYVA JATHON
'''

'''
a=input("Enter first string:")#java
b=input("Enter second string:")#python


if(len(a)<2 or len(b)<2):
    print("Not possible")
    
else:
    print(F"Result: {b[0:2]+a[2:]+" "+a[0:2]+b[2:]}")#pyva jathon
    
'''

'''
3.Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''

'''
s=input("Enter any string:")
if(len(s)<4):#if less than 3 letters it will print nothing
    print("Nothing")
    
else:
    print(s[0:2]+s[-2::1])
    
'''

'''
4.Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

Enter the string: VAMSI
String in forward:
Character at index 0: V
Character at index 1: A
Character at index 2: M
Character at index 3: S
Character at index 4: I
String in reverse:
Character at index -1: I
Character at index -2: S
Character at index -3: M
Character at index -4: A
Character at index -5: V

'''

'''
s=input("Enter the string:")#vamsi

print("String in forward:")
for i in range(len(s)):
    print(F"Character at index {i}: {s[i]}")
    
print("String in reverse:")
for i in range(-1,-len(s)-1,-1):
    print(F"Character at index {i}: {s[i]}")
    
'''

'''
5.Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

Enter  any  string  :  Rama Rao
Characters  at  even  indexes  :   Rm a
Characters  at  odd  indexes  :   aaRo
'''

'''
s=input("Enter  any  string  :")
o=e=''
for i in range(len(s)):
    if(i%2==0):
        e+=s[i]
        
    else:
        o+=s[i]
        
print("Characters  at  even  indexes  :",e)
print("Characters  at  odd   indexes  :",o)

'''
    
    
'''
6.

Enter  any  string  with  alternate  character  and  digit :  $5P2K3Z4
Result :   $$$$$PPKKKZZZZ
    
Enter  any  string  with  alternate  character  and  digit :  hyd
Pls  enter  alternate  char  and  digit

'''

'''
s=input("Enter  any  string  with  alternate  character  and  digit :") 
S=''
if(len(s)%2==0):
    for i in range(1,len(s),2):
        if(type(s[i])!=type(1)):
            print("Pls  enter  alternate  char  and  digit")
            break 
        
        S+=(int(s[i])*s[i-1])
    else:
        print("Result :",S)
        
else:
    print("enter even number of charcters alternate  char  and  digit")
 
'''

'''
TEST Solutions 7/3/2025 expected outputs
1.

ABCDEFGFEDCBA
ABCDEF FEDCBA 
ABCDE   EDCBA 
ABCD     DCBA 
ABC       CBA 
AB         BA 
A           A 
'''

'''
n=int(input("Enter number of rows:"))

for i in range(n):
    S=''
    for j in range(ord('A'),ord('A')+n-i):
        S+=chr(j)
    if(i==0):
        print(S+(2*i-1)*" "+S[-2::-1])
        
    else:
        print(S+(2*i-1)*" "+S[::-1])
    
'''

'''
#2.pascal triangle

      1
     1  1
   1  2  1
  1 3  3  1
 1 4  6  4 1

'''

'''
from math import * 

n= int(input("Enter number of rows:"))

for i in range(n):
    print((n-i)*" ",end="")
    
    for j in range(i+1):
        print(int(factorial(i)//(factorial(i-j)*factorial(j))),end=" ")
    print()  
    
'''

'''
3.prime numbers in the given range 

'''

'''
a=int(input("Enter start:"))
b=int(input("Enter stop:"))


for i in range(a,b+1):
    if(i==1):
        continue 
    for j in range(2,i):
        if(i%j==0):
            break 
        
    else:
        print(i,end=" ")
        
'''

'''
4.nth greatest number in the list 
'''

'''
a=list(map(int,input("Enter list of elements with space separated:").split()))
n=int(input("Enter n:"))

a.sort(reverse=True)

print(F"{n}th Largest number:",a[n-1])

'''


'''
5. sorting of list of strings 
'''

'''
a=input("Enter list of strings:").lower().split()

L=[]

for i in range(len(a)):
    L.append(min(a))
    a.remove(min(a))
    
print(L)
 
'''

"""
8/3/2025

1.Write  a  program  to  merge  two  strings  to  form  a  new  string

Enter  first  string  :  VAMSI
Enter  second  string  :  HYD
Result  :   VHAYMDSI

"""

'''
a = input("Enter  first   string  :")
b = input("Enter  second  string  :")

m=min(len(a),len(b))
i=0 
S=''

while(i<m):
    S+=a[i]+b[i]
    i+=1
    
if(m==len(a)):
    S+=b[m:]

else:
    S+=a[m:]
    
print("Result  :",S)

'''

'''
2.Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

'''

'''
s=input("Enter  any  string  :")
S=''

for i in s:
    if i not in S:
        S+=i 
        
print("String  without  duplicates  :",S)

'''


'''
3.

Enter  any  string  with  alternate  character  and  digit  :  M3K2$5z2
Result  :   MPKM$)z|

Enter  any  string  with  alternate  character  and  digit  :  hyd
Pls  enter  string  with  alternate  char  and  digit

'''

'''
s=input("Enter  any  string  with  alternate  character  and  digit  :")
S=''

try:
    for i in range(0,len(s),2):
        S+= s[i]+chr(ord(s[i])+int(s[i+1]))
        
    print(S)
    
except:
    print("Pls  enter  string  with  alternate  char  and  digit of even number of characters")
    
'''
