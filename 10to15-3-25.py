[10/03/25}

#1.Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

'''
s=input("Enter any string: ").upper()

S=''

for i in s:
    if i in "AEIOU" and i not in S:
        S+=i 
        
print(S)

'''


'''
#2.Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=-1
while  (index:=a . find('is' , index + 1))!= -1:
	print(index)
	
print('End')

'''

'''  
#3.index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

try:
    index=-1
    while (index:=a . index('is' , index + 1)):
        print(index)
	
except:
    print("End")
'''



'''
#4.rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=len(a)
while  (index:=a . rfind('is',0,index-1))!=-1:
    print(index)
    
print("End")
'''


'''
#5.rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

try:
    index=len(a)-1
    while (index:= a .rindex('is' ,0,index-1)):
        print(index)
        
        
except:	
    print('End') #output 46<next line>,42<next line>,23<next line>,4<next line>
    
'''


'''
#6.Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*' 
except  first  character

Enter  any  string :  babble
Result :   ba**le

'''

'''
s=input("Enter  any  string :")
S=s[1:]
print(s[0]+S.replace(s[0],'*'))

'''


'''
#7.Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method


Enter the expression: 23+456+7
Sum:  486
'''

'''
s=input("Enter the expression:").split("+")

try:
    S=0
    for i in s:
        S+=int(i)
        
    print(S)
except:
    print("Enter only int  in the expression ")
    
'''


'''
#8.Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
'''
s=input("Enter any string: ")

if(len(s)<3):
    print(s)
    
else:
    if(s.endswith("ing")):
        print(s+"ly")
        
    else:
        print(s+"ing")
        
'''
[11/03/25} part 1

#1.isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #False due to A
print('\n  \t' . isspace()) #True 
print('\n  7\t' . isspace()) #False due to 7
print('\n' . isspace()) #True
print('\n  $\t' . isspace()) #False due to $
print('\t' . isspace()) #True
print('' . isspace()) #False due to no space 
print(' ' . isspace()) #True

'''

'''
#2.Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #25,10.8,Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #25,10.8,Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #Hyd,10.8,25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #Hyd,Hyd,Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #25,10.8,Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #Hyd,10.8,25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #25,25,25

'''


'''
#3.Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet

'''

'''

s=input("Enter any Character: ")

if(s.isalnum()):
    print("Alpha  Numeric  Character")
    
    if(s.isalpha()):
        print("Alphabet  Character")
        
        if(s.isupper()):
            print("Upper  case  Alphabet")
            
        else:
            print("Lower  case  Alphabet")
            
    else:
        print("Digit Character")
    
elif(s.isspace( ) or s=="\\t" or s=='\\n'):
    print("White space")
    
else:
    print("Special character")
    
'''

'''
#4.Write  a  program  to  reverse  a  string  without  slice


Enter  any  string : Rama Rao
Reverse  String :   oaR amaR

'''


'''
s=input("Enter  any  string :")
S=''
for i in range(1,len(s)+1):
    S+=s[-i]
    
print(S)

'''


'''
#5.Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice


Enter  any  sententce : students are getting  bored
Reverse  order  of  words :  bored getting are students

'''

'''
s=input("Enter  any  sententce :").split()

S=''

for i in range(1,len(s)+1):
    
    if(i==len(s)):
        S+=s[-i]
        
    else:
        S+=s[-i]+" "
        
print(S)
    
'''


'''
#6.Write  a  program  to  reverse  each  word  of  the  sentence

Enter  any  sentence  :  hyd is green city
dyh si neerg ytic

'''

'''
s=input("Enter  any  sentence  :").split()
S=''
for i in range(len(s)):
    
    if(i<len(s)-1):
        S+=s[i][::-1]+" "
        
        
    else:
        S+=s[i][::-1]
        
print(S)

'''


'''
#7.Write  a  program  to  sort  string  in  alphabetical  order

Enter  any  string  :  RAJESH
Sorted  string  :    AEHJRS

'''

'''
s=input("Enter  any  string  :")
l=sorted(s)
print(''.join(l))

'''


'''
#8.Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method

'''

'''

s=input("Enter  any  string  :")
l=sorted(s)

d=''
a=''

for i in l:
    if i.isdigit():
        d+=i 
        
    else:
        a+=i 
        
print(a+d)


'''

[11/03/25} part 2
'''
#1.What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ') #[25,10.8,'Hyd',True]
print(type(a)) #<class 'str'>
print(a) # [25,10.8,'Hyd',True]
b = eval(a) # [25,10.8,'Hyd',True]
print(b)  # [25,10.8,'Hyd',True]
print(type(b)) # <class 'list'>

'''

'''
# 2.Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a #same reference
print(a  is  b) # True
print(a  ==  b) # True same Value
b[2] = 12 
print(a) # [10,20,12,18]

'''

'''
# 3.Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10 , 20 , 15 , 18 , 100 , 200 , 150]
#print(a + 5) # Error list + int 
#print(a + '5') # Error list + str
#print([10 , 20] + (30 , 40)) # error list + tuple 

'''

'''
#4.Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  25,[10.8,'Hyd'],True
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list # 25,[10.8,'Hyd',True]
print('x : ' , x) #25
print('y : ' , y) #[10.8,'Hyd',True]
*p , q = list #[25 , 10.8 , 'Hyd'],True
print('p : ' , p) #[25 , 10.8 , 'Hyd']
print('q : ' , q) #True

'''


'''
#5.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list #error due to less args 
a , b , *c , d , e = list #25,10.8,[],'Hyd',True
print('a : ' , a) #25
print('b : ' , b) #10.8
print('c : ' , c) #[]
print('d : ' , d) #'Hyd'
print('e : ' , e) #True
#a , b , *c , d , e , f = list #error due to less args 

'''

'''
#6.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list 
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ :  ' , _) #'Hyd'
print('d : ' , d)  #True

'''

'''
#7.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list  
print('a : ' , a) #(3+4j)
print('b : ' , b) #10.8
print('d : ' , d) #True


'''


'''
#8.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)  #25
print('b : ' , b)  #10.8
print('_ : ' , _)  #(3+4j)
print('d : ' , d)  #True
print('_: ' , _)   #(3+4j)

'''

'''
#9.Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #error due to multiple *


'''


'''
#10. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #[25,10.8]
print('b :  ' , b) #'Hyd'
print('c :  ' , c) #True


'''

'''
#11. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # 25
print('b : ' , b) #10.8
print('c : ' , c) #'Hyd'
print('d : ' , d) #True
#a , b , c , d = list #error due to less unpack args 


'''

'''
#12. Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)  # True
print(a  is   b) # False
print(a < c) #True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False

'''

'''
#13.Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False

'''

'''
# 14.len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3

'''

'''
#15.sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False] 
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True] 
#print(sum(e)) #error due to 'Hyd'
'''

'''
#16.Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) #error 
print(sum(a[0]))
print(sum(*a))

'''

'''
#17.max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #'Vamsi'
print(min(b)) #'Amar'
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #error due to complex
d = [25 , '35'] 
#print(max(d)) # error 
#print(max([])) #error
#print(min([])) #error

'''

'''
#18.list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10,20,15,18]
print(type(b)) #,class 'int'>
print(a  is  b) # False
print(a == b) # False

'''

'''
#19.Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) 
print(b)  #[4,6,8]
print(type(b)) #<class 'list'>
a = list('Vamsi')
print(a) #['V','a','m','s','i']
a = list()
print(a) #[]
#print(list(25)) #error 
#print(list(10.8)) #error
#print(list(True)) #error
#print(list(None)) #error list arg is nothing or any sequence


'''

'''

#20.Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10 , 20] , (30 , 40) , {50 , 60}]

'''

'''
#21.Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) 
print(b) #['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']
print(a) #['Rama','Rajesh','Amar','Sita','Vamsi' ,'Kiran','Rama  Rao']

'''

'''
#22.all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #True *


'''

'''
#23. any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #False

'''


[12/03/25}

'''
# 1. append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10,20,15,18]
list . append(19) # APEEND ALWAYS INSERT IN LAST OF THE LIST
print(list) #[10,20,15,18,19]

'''


'''
# 2. Find  outputs (Home  work)
list = []
print(list) # []
list . append(25) # [25]
list . append(10.8) #[25,10.8]
list . append('Hyd') #[25,10.8,'Hyd',]
list . append(True) #[25,10.8,'Hyd',True]
print(list) # [25,10.8,'Hyd',True]

'''

'''

#3.Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # range [ start (0): end (50) :instep (10)]  [ 0,10,20,30,40]

'''

'''
# 4. Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10,20,30,'Hyd']
print(len(a)) # 4
print(a[3]) #(How  to  print  4th  element  of  list  'a')
print(a[3][0])#(How  to  print  'H')
print(a[3][1])#How  to  print  'y')
print(a[3][2])#How  to  print  'd')

'''


'''
# 5. Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) # [ 50,60,2,70]
print(a) # [ 10, 20 ,[50 , 60 , 70] ,30 , 40]
print(len(a)) #5
print(a[2])#(How  to  print  inner  list) 
print(a[2][0])#How  to  print  50)
print(a[2][1])#How  to  print  60)
print(a[2][2])#How  to  print  70)

'''
[12/03/25}
#1.append()  method  demo  program

'''
list = [10,20,15,18]
print(list) #[10,20,15,18]
list . append(19)
print(list) #[10,20,15,18,19]

'''


#2.Find  outputs

'''

list = []
print(list) #[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) #[25,10.8,'Hyd',True]


'''


#3.Find  outputs

'''

list = []
for  x  in   range(0 , 50 , 10):
	list . append(x) 
print(list) #[0,10,20,30,40]

'''


#4.Find  outputs 

'''

a = [10 , 20 , 30]
a . append('Hyd')
print(a)      # [10 , 20 , 30,'Hyd']
print(len(a)) #4
print(a[3],a[-1]) #How  to  print  4th  element  of  list  'a'
print(a[3][0],a[-1][0]) #How  to  print  'H'
print(a[3][1],a[-1][1]) #How  to  print  'y'
print(a[3][2],a[-1][2]) #How  to  print  'd'


'''

#5.Find  outputs

'''
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) 
print(a)       #[10,20,[50 , 60 , 70],30,40]
print(len(a))  #5
print(a[2],a[-3])       #How  to  print  inner  list
print(a[2][0],a[-3][0]) #How  to  print  50
print(a[2][1],a[-3][1]) #How  to  print  60
print(a[2][2],a[-3][2]) #How  to  print  70


'''
[13/03/25}
# 1.clear() method  demo program

"""
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]

"""

# 2.reverse()  method  demo  program

"""
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse()
print(a) #[18,15,20,10]

"""

# 3.sort()

"""
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort()
print(list) #[5,10,15,18,20]
list . sort(reverse = True)
print(list) #[20,18,15,10,5]

"""


# 4.Find  outputs

"""
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama  Rao']
a . sort()
print(a) #['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
a . sort(reverse = True)
print(a) #['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']

"""


# 5.Identify  error

"""
a = [25 , 10.8 ,'Hyd',  True]
#a . sort() #can't sort number and string

"""


# 6.count()  method  demo    program

"""
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #0
print(len(a)) #9

"""


# 7.Write  a  program  to  remove  all  duplicate  elements  of  list (Not  even  single  occurance)

"""
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods


"""

"""
a=eval(input("Enter a List: "))
L=[]

for i in a:
    if a.count(i)==1:
        L.append(i)
        
print(L)

"""


# 8.index()  method  demo  program

"""
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0   1     2    3    4   5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1) # 2 5 8
except:
	print(F'15  is  found  {a . count(15)}  times ') # 15  is  found  3 times

"""


"""
Gift
#9.Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [2,3,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  True  becoz  elements  2,3,4   are   in  [2,2,3,4,5]

2) First  list :  [2,4,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->	False  becoz   elements  2,4,4  are  not  in  [2,2,3,4,5]

3) First  list :  [2,4,3]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  False  becoz   elements  2,4,3   are  not  in  [2,2,3,4,5]

4) First  list :  [2,2,5]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  ---> True  becoz   elements  2,2,5    are   in  [2,2,3,4,5]

5) Hint:  Use  index()  method
"""

"""
a=eval(input("First  list: "))
b=eval(input("Second list: "))

A=''
for i in a:
    A+=str(i)
    

B=''
for i in b:
    if i in a:
        B+=str(i)
        

if A in B:
    print("True")
    
else:
    print("False")
    
"""


'''
a=eval(input("First  list: "))
b=eval(input("Second list: "))

#a=[2,2,5]
#b=[2,2,3,4,5]

c=b.copy()

for i in c:
    if i not in a or b.count(i)>a.count(i):
        b.remove(i)
        
print(b)

if(len(a)!=len(b)):
    print(False)

else:
    for i in a:
        if a.index(i)!=b.index(i):
            print(False)
            break 
        
    else:
        print(True)


'''


# 10.copy()  method  demo program

"""
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) #[10 , 20 , 15 , 18]
print(a  is  b) #False
print(a  ==  b) #True
c = a[:] 
print(c) #[10 , 20 , 15 , 18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d) #[10 , 20 , 15 , 18]
print(a  is  d) #True
print(a  ==  d) #True

"""


#11.Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

'''
Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical

Enter  any  list  :  [25,25,25.0,25]
All  the  list  elements  are  identical

'''

'''
a=eval(input("Enter  any  list  : "))

if(a.count(a[0])!=len(a)):
    print("List   elements  are  not  identical")
    
else:
    print("All  the  list  elements  are  identical")
    
'''


'''
#12.Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
'''

'''
a=eval(input("Enter  any  list  : "))
x=eval(input("element need to be removed: "))

b=a.copy()

for i in b:
    if i==x:
        a.remove(i)
        
print(a)

'''

'''
Gift
#13.Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list


Enter  List  :   [10,20,15,18,10,20,15,10,20,19,10]
Mode :  10

'''

'''
a=eval(input("Enter  List  : "))
A=[]


for i in a:
    if i not in A:
        A.append(i)
        
F=[]

for i in A:
    F.append(a.count(i))
    
M=max(F)


for i in range(len(F)):
    if(F[i]==M):
        print("Mode:",A[i])
    
'''


#14.Nested  List  demo  program

'''

a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) #3
print(a[0])    #How  to  print  1st  inner  list
print(a[1])     #How  to  print  2nd  inner  list
print(a[2])    #How  to  print  3rd  inner  list
print(a[0][2]) #How  to  print  30
print(a[1][3]) #How  to  print  80
print(a[2][1])      #How  to  print  100

    
'''


#15.Find  outputs

'''
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])#How  to  print  1st   inner  list
print(a[1])#How  to  print  2nd   inner  list
print(a[2])#How  to  print  3rd   inner  list
print(*a[0])#How  to  print  number  of  elements  in  1st  inner  list
print(*a[1])#How  to  print  number  of  elements  in  2nd  inner  list
print(*a[2])#How  to  print  number  of  elements  in  3rd  inner  list

'''



#16.How  to  print  nested  list  in  differnent  ways

'''

a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]

print('Nested list  with  print function')
print(a)

print('Each  inner  list   of   outer  list  without  indexes')
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)

print(*a)
for i in a:
    print(i,end=" ")
    
print()
    
    
print('Elements  in  the  form   of  matrix   without  using  indexes')
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style(use  nested  loop)
for i in a:
    print(*i)

print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
        
    print()
'''

'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''


#17.Find  outputs

'''
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) #[10 , 20] \n [30 , 40] \n [50 , 60] \n [70 , 80] \n
print() #\n
for  x , y  in  a:
	print(x , y , sep = '...') #10...20 \n 30...40 \n 50...60 \n 70...80 \n

'''

#18.Find  outputs

'''
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) #10 , 20 , 30] \n [40 , 50 , 60] \n [70 , 80 , 90]\n
print() #\n
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') #10...20...30 \n 40...50...60 \n 70...80...90 \n

'''


#19.Find  outputs

'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) #[10 , 20] \n [30 , 40 , 50] \n [60 , 70 , 80 , 90] \n
#for  x , y  in  a:
	#print(x , y ,	sep = '...') #error due to more values to un pack 

'''


#20.Find  outputs

'''
a = [[]]
print(a[0])#How  to  print  inner  list
print(*a,a[-1])#How  to  print  inner  list  in  another  way

'''


#21.Find  outputs 

'''

a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
#[[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0],[15 , 'Rajesh' , 3500.0],[18 , 'Kiran' , 2800.0],[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))
#[[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0],[5 , 'Amar'  ,5000.0]]
print(a)
[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

'''


#22.Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension 
#[8, 64, 216, 512, 1000]

'''
print([i**3 for i in range(2,11,2)])

'''


#23.Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

'''
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''

'''
s=eval(input("Enter list of strings: "))
#s=['hyd' , 'pune' , 'chennai' , 'vijayawada']

C=[]

for i in s:
    C.append(i[0].upper())
    
print(C)

'''


'''
(Home  work)
#24.Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''

'''
s=eval(input("Enter list of strings: "))
#s=['hyd' , 'pune' , 'chennai' , 'vijayawada']
print([i[0].upper() for i in s])

'''



'''
#25.Write  a  program  to  append  each  word  of  the  sentence  and  its  length 
to  a  list (word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()


'''

'''
s=input("Enter any sentence :").split()

#s="hyd  is  green  city".split()

L=[]
for i in s:
    L.append([i.upper(),len(i)])
    
print(L)


'''

'''
#26.Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

'''
s=input("Enter any sentence :").split()

#s="hyd  is  green  city".split()

print([[i.upper(),len(i)] for i in s])


'''



'''
#27.Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 30 , 40 , 50 , 60 , 70]

b=eval(input("Enter 2nd list:"))
#b=[100 , 200 , 300 , 400]

i=0 
r=[]
while(i<len(a) and i<len(b)):
    r.append(a[i]+b[i])
    i=i+1 
    
print(r)

'''


'''
#28.Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''


'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 30 , 40 , 50 , 60 , 70]

b=eval(input("Enter 2nd list:"))
#b=[100 , 200 , 300 , 400]

m=min(len(a),len(b))

print([a[i]+b[i] for i in range(m) ])

'''


'''
#29.Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *


How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''

'''
r=int(input("How  many  lists  ?  :"))
c=int(input("How  many  elements  in  each  list ?  :"))

L=[]
for i in range(r):
    L.append([0]*c)
    
print(L)
    
'''


'''
#30.Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

'''
r=int(input("How  many  lists  ?  :"))
c=int(input("How  many  elements  in  each  list ?  :"))

print([[0]*c for i in range(r)])

'''


'''
#31.Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15 , 18 , 25 , 32]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 10 , 25 , 15]

L=[]

for i in a:
    if i not in b:
        L.append(i)
        
print(L)

'''


'''
#32.Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15 , 18 , 25 , 32]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 10 , 25 , 15]

print([i for i in a if i not in b])

'''

#33.Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
#Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
print([i for i in range(1,21) if i%2==0])

'''


'''
#34.Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''

'''
print([i for i in range(2,21,2) ])

'''

'''
#35.Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  
which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
'''

'''
print([i**2 for i in range(1,21) if i%2==0])
'''

#36.Repeat  previous  program  with  comprehension  and  without  using  if

'''
print([i**2 for i in range(2,21,2) ])

'''


'''
#37.Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 35 , 32]

L=[]
for i in a:
    for j in b:
        L.append(i+j)
        
print(L)

'''


'''
#38.Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 35 , 32]

print([i+j for i in a for j in b])

'''


'''
#39.Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

'''

a=input("Enter 1st string: ")
b=input("Enter 1st string: ")

print([i+j for i in a for j in b])


'''


'''
#40.Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

'''
a=eval(input("Enter nested list:"))
#a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

L=[]

for i in a:
    L.extend(i)
    
print(L)

'''


#41.Find  outputs

'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x] #[10 , 20] 2 times ,[30 , 40 , 50] 3 times ,[60 , 70 , 80 , 90] 4 times 
print(b)

'''


#42.Nested  comprehension  demo  program 

'''
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)] #[],[0],[0,1],[0,1,2],[0,1,2,3]
print(a)

'''



'''
#43.Normal  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

1) b = ['S', 'A' , 'Z' , 'K']

2) c = []

3) Iteartion  1 :  d  =  ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''


'''
a=['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]

L=[]
for i in a:
    if i[0] not in L:
        L.append(i[0])
            
#print(L)

R=[]

for i in L:
    l=[]
    for j in a:
        if j[0]==i:
            l.append(j)
            
    R.append(l)
    
print(R)
   
'''     
        
        
'''
#44.Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                        0      1      2       3      4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]

       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                     0     1       2       3
	                     
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''

'''

a=eval(input("Enter 1st List: "))
#a=[10  ,  20  , 30   ,  40   ,  50]

b=eval(input("Enter 2nd List: "))
#b=[5  ,  12  , 20   ,  37]

c=a+b 

c.sort()
print(c)

'''
[15/03/25]

#1.Find  outputs 

'''

a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) #<class 'tuple'>
#a[3] = 'Sec' #error becz tuple is immutable

'''


#2.What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?  

'''
a = input('Enter  Tuple  :  ')
print(a) #(10 , 20 , 30 , 40)
print(type(a)) #,class 'str'>

b = eval(a) 
print(b) # (10 , 20 , 30 , 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4

'''


#3.Find  outputs 

'''
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 
print(a) #(10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]  #error due tuple is immutable
print(a)

'''


#4.Find  outputs 

'''
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70 # error becz tuple is immutable 
print(a) #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90] 
print(a) #[10 , [80,90] , 50 , 60]

'''


#5.Find  outputs

'''

a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25,10.8,'Hyd',True)
print(type(x)) # <class 'tuple'>

'''


#6.Find  outputs 

'''

x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
#p , q , r =  x # error becz more values to unapck
#a , b , c , d  , e = x # # error becz not enough  values to unapck

'''


#7.Find  outputs 

'''
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) # [10.8,'Hyd']
print(c) #True

'''


#8.Find  outputs 

'''
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) #25
print(b) #10.8
print(c) #[]
print(d) #Hyd
print(e) #True

'''


#9.Find  outputs 

'''
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #(3+4j)
print(d) #True
print(_) #(3+4j)

'''


#10.tuple()  function  demo  program 

'''

a = range(100 , 150 , 10)
b = tuple(a) 
print(b) #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e) #('V','a','m','s','i')
#print(tuple(25)) #Error due to 25 
print(tuple()) #()

'''


#11.index()  and  count()  methods  demo  program 

'''

a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4   5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i) # 2 5 8 \n 15  is  found  3  times
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
'''


#12.How  to  modify  an  element  of  tuple ? 

'''
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1    2       3     4
#a[2] = 35 #error becz tuple is immutable
print(a) #(10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) #address
#How  to  modify  30  in  tuple  to  35
a=list(a)
a[2]=35 
a=tuple(a)
print(a) #(10 ,  20 ,  35,   40 ,  50)
print(id(a)) #different 

'''


#13.How  to  delete  an  element  of  tuple ? 

'''
a  = 10 , 20 , 30 , 40 , 50
#    0     1    2   3    4
#a . remove(30) #error becz tuple is immutable 
#del  a[2] #error becz tuple is immutable 
#a . pop(2) #error tuple obj doesn't have pop method 
print(a) #(10 , 20 , 30 , 40 , 50)
print(id(a)) #1000

#How  to  remove  30  from  tuple  'a'
a=a[:2]+a[2:]
print(a) #(10 , 20 , 40 , 50)
print(id(a)) #2000

'''


#14.Nested   tuple

'''
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  tuple
print(a[1]) #How  to  print  2nd  inner  tuple
print(a[2]) #How  to  print  3rd  inner  tuple
print(a[0][1])  #How  to  print  20
print(a[1][-1])  #How  to  print  50
print(a[2][-1]) #How  to  print  90


'''


#15.Find  outputs 

'''
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple
print(*a) #How  to   print  inner  tuple  in  another  way
print(a[0][0]) #How   to  print   10
print(a[0][1]) #How   to  print   20
print(a[0][2]) #How   to  print   30
b = ((),)
print(b[0]) #How  to   print  inner  tuple  of  tuple  'b'
print(*b)  #How  to   print  inner  tuple  of  tuple  'b'  in  another  way

'''


#16.Find  outputs

'''
a = ((10 , 20 , 30))
print(a) #(10 , 20 , 30)
print(*a) # 10 20 30 
b = (())
print(b) # ()
print(*b) # nothing 

'''


#17.What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}

'''
a = input('Enter  Set  :  ')
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #{10 , 20 , 15 , 18 , 12 }
print(type(b)) #<class 'sst'>

'''

#18.Find  outputs 

'''
print({(10 , 20 , 30)}) #{(10 , 20 , 30)}
#print({[10 , 20 , 30]}) # error no mutable objs 
#print({{10 , 20 , 30}}) # error no mutable objs 
#print({{}}) # no mutable objs 

'''


#19.How  to  print  set  in  differnet ways  

'''
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop

for i in a:
    print(i)
    
'''

#20.Find  outputs

'''
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{'Hyd',True,25}
print(len(s)) #3
print(type(s)) #<class 'set'>

'''


#21.Find  outputs


'''
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } whatever order here 
a , b , c , d = s
print(a) #Hyd
print(b) #25
print(c) #True 
print(d) #10.8 

'''


#22.Find  outputs

'''
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s 
print(a) #Hyd
print(b) #[ 25,  True,  10.8 ]
print(type(b)) #<class 'list'>

'''

#23.Find  outputs

'''
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b , c = s 
print(a) #Hyd 
print(b) #[25,True]
print(c) #10.8

'''

#24.Find  outputs 

'''
s = {20 , 10 , 20 , 10}
print(s) #{10 , 20}
x , y = s 
print(x) #10
print(y) #20

'''


#25.set()  function  demo  program

'''
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,110,120,130,140}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d) #{20,15,18,10,50,12}
e = set('Rama  rAo')
print(e) #{'R','a','m',' ','r','A','o'}
#print(set(25)) #Error due to 25 
print(set()) #set()

'''

#26.add()  method  demo  program

'''
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) #{True,25,10.8,'Hyd',None}
#a . add(10 , 20 , 30) #Error because add method takes 1 arg 
#a . add([10,20,30]) #Error becz set doesn't have mutable obj like list 


'''


#27.Find  outputs 

'''
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a)) #1000
a . add(tpl) 
a . add('Sec')  
print(a) #{25 , 10.8 , 'Hyd' ,'Sec' ,True,(10 , 20 , 30)}
print(id(a)) #1000
print(len(a)) #6
#a . add([100 , 200 , 300]) # #Error no mutable obj in set
#a . add(set()) #Error no mutable obj in set
#a . add({ }) #Error no mutable obj in set

'''


#28.Find  outputs

'''
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s) #{(10 , 20 , 15 , 18)}
print(len(s)) #1

'''

#29.update()  method  demo program

'''
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) 
print(len(s)) #4
print(s) #{10 , 20 , 15, 18 , 10 , 20}
#s . update(25) #Error for update arg should be sequence

'''


#30.Find  outputs

'''
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10,20,30,40,50,60,70}
print(len(s)) #7
#s . add(a , b , c) #error because 3 args 


'''


#31.Find  outputs
'''
a = set()
a . update('Rama Rao')
print(a) #{'R','a','m',' ','o'}
print(len(a)) #5
#a . update(3 + 4j , 10.8 , True) #Error due to non sequence 

'''


#32.copy()  method  demo  program

'''
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
b = a . copy()
print(b) #{10 , 20 , 15 , 18}
print(a  is  b) #False
print(a  ==  b) #True 
c = a
print(a  is  c) #True

'''

#33.remove()  method  demo  program 

'''
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') 
print(a) #{25 , 10.8 ,True}
#a . remove('Sec') #Error 

'''


#34.discard()  method  demo  program

'''
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) #{25 , 10.8 , True}
a . discard('Sec') 
print(a) #{25 , 10.8 , True}
#a . remove('Sec') #Error 

'''

#35.clear()  method  demo  program 

'''
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) #set()
print(len(a)) #0

'''


#36.Find  outputs  (Home work)

'''
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10 , 20 , 30 , 40,50,60}
#print(a | b), # Error due to |
#print(b . union(a)) # Error due to union 
#print(a + b) #Error due to +

'''
