# complex object demo program
a = 3 + 4j
print(a)# 3 + 4j
print(type(a))#<class 'complex'>
print(id(a))#maybe 140876
print(a . real)#3.0
print(a . imag)#4.0
print(type(a . real))#float
print(type(a . imag))#float


# Find outputs (Home work)
a = 6j
print(a)#0 + 6j
print(type(a))<class 'complex'>
print(a . real)#0.0
print(a . imag)#6.0
print(5 + j6)#error due j before 6
print(3 + 4i)#error due to i
print(4+j)#error due no number before j
print(4 + 1j)#4 + 1j
print(4 + 0j)#4 + 0j


# bool object demo program
a = True
print(a)#True
print(type(a))#<class 'bool'>
print(id(a))#137168196233984
b = False#
print(b)#False
print(type(b))#<class 'bool'>
print(True + True)#2
print(True + False)#1
print(False + True)#1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#36.8
print(True > False)#True
print(True)#True
print(False)#False
print(true)#true
print(false)#false


# int()  function  demo  program
print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False)) #   Converts  False  to  0
print(int('25'))  #  Converts   '25'  to  25
print(int('0075')) #   75
print(int(0B11010)) #  Converts  binary  number  to  decimal  number  i.e.  16 + 8 + 2 = 26
print(0B11010)  #  Converts  binary  number  to  decimal  number  i.e.  16 + 8 + 2 = 26
print(int(0O6247)) #  Converts  octal   number  to  decimal  number  i.e.   6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239
print(0O6247)  #  Converts  octal   number  to  decimal  number  i.e.   6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239
print(int(0XA7B9))  #  Converts  hexa  decimal   number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(0XA7B9)  #  Converts  hexa  decimal   number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
#print(int(3 + 4j))  #  Error  becoz  complex  number  can  not  be  converted  to  integer
#print(int('25.4'))  #  Error  due  to  string  float
#print(int('Ten'))  # Error  becoz  'Ten'  can  not  be  converted to  integer


# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False)) #  Converts   False   to   0.0
print(float('92'))  #  Converts   '92'   to   92.0
print(float('36.4'))  #  Converts   '36.4'   to   36.4
print(float('0075'))  #  Converts   '0075'  to   75.0
print(float(0B1010101)) #  Converts  binary   number  to   decimal  number  i.e.   64 + 16 + 4 + 1 = 85.0
print(float(0O6247))  #  Converts  octal  number  to   decimal  number  i.e.  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239.0
print(float(0XA7B9))  #  Converts  hexa  decimal   number  to   decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937.0
#print(float(3 + 4j))  #   Error  becoz  complex  number  can  not  be  converted  to  float
#print(float('Ten'))   #   Error  becoz  'Ten'  can  not  be  converted  to  float


# float  object  demo  program (Home  work)
a = 10.8   #   Ref  'a'  points  to  float  object   10.8
print(a)  #  Value  of  object   'a'  i.e.  10.8
print(type(a))  # Type  of  object   'a'  i.e.  <class  'float'>
print(id(a)) #  Address  of  object  'a'  (may  be  1000)
b = 25.  #  Valid  and  is  interpreted  as  25.0
print(b) #  25.0
print(type(b)) #  <class  'float'>
c = .689  #  Valid  and  is  interpreted  as   0.689
print(c) #   0.689
d = 3.4E2  # 3.4 * 10 ^ 2 
print(d) #   340.0
print(type(d))#   <class  'float'>
e = 9.62e-2  #  9.62 * 10 ^ -2
print(e) #  0.0962
#print(9.8.2)  #  Error  due  to  2  decimal  points


# NoneType  object  demo  program
a = None  #  Ref  'a'  points  to  object  None
print(type(a))  #  Type  of  object 'a'  i.e.  <class  'NoneType'>
print(a) #  Value  of  object  'a'  i.e.  None
print(id(a)) #   Address  of  object  None  
print(id(None))#   Error  due  to  'n'
