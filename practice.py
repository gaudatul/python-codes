# positive or negative number

"""n=int(input("Enter a number: "))
if n==0:
      print("The number is Zero")
elif n>0:
      print("The number is Positive")
else:
      print("The number is Negative")"""


# odd or even numbers
"""n=int(input("Enter a number:"))
if n%2==0:
    print("even number")
else:
    print("odd number")"""


# Sum of natural number
"""n=int(input("Enter the number:"))
sum=(n*(n+1))/2
print("the sum of N natural number is {}".format(sum))"""

"""n=int(input("enter a number:"))
sum=0
for i in range(n+1):
    sum=sum+i
print("Sum is:",sum)"""


#sum of number in a given number:-

"""l=int(input("enter lower number:-"))
u=int(input("enter the upper number:-"))

sum=0

for i in range(l,u+1):
    sum=sum+i

print("Addition of number =",sum)"""

#Compare of number

"""f=int(input("enter the first number:"))

s=int(input("enter the second number:"))

if f>s:
    print("first is greater than second")
elif s>f:
    print("second is greater than first")
else:
    print("equal")
"""


""""f=int(input("enter the first number:"))

s=int(input("enter the second number:"))

t=int(input("enter the third number :"))

if f>s and f>t:
    print("first is greater than second and third:",f)
elif s>f and s>t:
    print("second is greater than first and third:",s)
elif t>f and t>s:
    print("third is greater than first and second:",t)
else:
    print("Number is equal")"""


# Leap year or not

"""year=int(input("Enter year:-"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Yes,{} is leap year".format(year))
        else:
            print("No,{} is not leap year".format(year))
    else:
        print("Yes,{} is leap year".format(year))
else:
    print("No,{} is not leap year".format(year))"""

"""x=int(input("enter a year:-"))
result="leap year" if x%400==0  else "leap year" if x%4==0 and x%100!=0 else "Non leap year"
print(result)"""


#prime number

"""n=int(input("Enter a number :-"))
if n<2:
    print("not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("number is prime")"""

#prime number within the range:

"""f=int(input("Enter the first number:"))
s=int(input("Enter the second number:"))

for i in range(f,s+1):
     for j in range(2,i//2):
         if i%j==0:
             break
     else:
         print("prime number :",i)"""

# Sum of digits

"""n=input("enter number:")
sum=0
for i in n:
    sum=sum+int(i)
print(sum)"""

#Reverse of number

"""n = int(input("Enter the numbers:-"))
print(str(n)[::-1])


num = (input("Enter the number:"))
for i in str(num[::-1]):
    print(i,end="") """

# palindrome numbers:- 151 and 526625

"""n=input("Enter the palindrome numbers:-")
inv_n = n[::-1]
if (n==inv_n):
    print(inv_n)
    print("Palindrome")
else:
    print("not a palindrome nuumber")"""

#Armstrong numbers

import math

"""value=int(input("Enter any positive numbers:-"))
n=[int(d) for d in str(value)]
sum=0
for i in range(0,len(n)):
    sum=sum+math.pow(n[i],len(n))

if sum==value:
    print("Given number is armstrong number ")
else:
    print("Given number is not armstrong number")"""

#Fibonacci series

"""def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(9)"""


#Too check armstrong numbers

"""i = int(input("Enter number to check armstrong:-"))
original = i
sum = 0
while (i > 0):
    sum = sum + (i % 10) * (i % 10) * (i % 10) #* (i % 10)
    i = i // 10
if original == sum:
    print("Number is armstrong")
else:
    print("number is not armstrong")

import math
value = int(input("Enter the Number: "))
num = [int(d) for d in str(value)]
sum = 0
for i in range(0, len(num)):
    sum = sum + math.pow(num[i], len(num))

if sum == value:
    print("Given number is Armstrong Number")
else:
    print("Given Number is not Armstrong Number")"""


"""import math

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

for num in range(first,second+1):
    order=len(str(num))
    sum=0
    temp=num
    while (temp>0):
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)"""

"""def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")

fib(9)"""

"""num = int(input("Enter the number:"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print("Factorial of a Given Number:", factorial)"""

"""base = int(input("Enter Base number:"))
expo = int(input("Enter Expo Number:"))
temp = 1

for i in range(0, expo):
    temp = temp * base"""
#print(temp)


#find the number of power

"""x=3
y=4
c=x**y
print(c)"""

"""number = int(input("Enter the Number:"))
for i in range(1, number+1):
    if number % i == 0:
        print(i, end=" ")"""


"""n = int(input("Enter any number: "))
sum= 0
for i in range(1, n):
    if(n % i == 0):
        sum= sum + i
if (sum == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")"""

#Automorphic number :
"""a=int(input("enter any number:-"))
n=a
m=a*a
print("original number:",n)
print("square of the number:", m)
n=str(n)
m=str(m)

if m.endswith(n):
    print("the number is automorphic")
else:
    print("Number is not automorpjic")"""

# to check the Harshad number:  sum of digits of 408(4+0+8) =408/ 12=34

"""n=int(input("Enter any number:-"))
p=n
sum=0
while(n>0):
    sum+=n%10
    n=n//10
if(p%sum==0):
    print("Harshad number")
else:
    print("Not harshad number")"""


"""sum=0
n=int(input("harshad number from 1 to :"))
for i in range(1,n+1):
    temp=i
    while temp!=0:
        r=temp%10
        sum=sum+r
        temp=temp//10
    if i%sum==0:
        print(i,end=" ")
    sum=0
"""



#Python program on to find  HCF of  Numbers:

"""n1=int(input("enter first number:-"))
n2=int(input("enter second number:-"))
arr=[]
if n1>n2:
    smaller =n2
else:
    smaller=n1

for i in range(1,smaller+1):
    if (n1%i==0) and (n2%i==0):
        arr.append(i)

print("The HCF of given number is : {}".format(max(arr)))"""


#Python program on to find  LCM of Numbers:

"""def lcm(n1,n2):
    if n1>n2:
        large=n1
    else:
        large=n2

    while (True):
        if(large%n1==0) and (large%n2==0):
            lcm=large
            break

        large=large+1

    print("LCM of two given number:{}".format(lcm))


lcm(2,4)"""



# Greatest common number (GCD) of any number :

"""num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))

gcdFunction(num1, num2)"""

# Binary to decimal conversion :

"""num=int(input("Enter number:"))
binary_value=num
decimal_value=0
base=1

while num>0:
    rem=num%10
    decimal_value=decimal_value+rem*base
    num=num//10
    base=base*2

print("binary number is {} and decimal number is {}".format(binary_value,decimal_value))
"""

# decimal into binary, octal,hexadecimal conversion:

"""dec=int(input("enter decimal number "))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
"""

#Binary to ocatl conversion:

"""Bin_num=0b10111
Oct_num=oct(Bin_num)

print("Number after conversion is:"+str(Oct_num))


# Octal to Binary:

oct_num=0o4
bin_num=bin(oct_num)

print("number after conversion is:"+str(bin_num))

#Octal to decimal:
Oct_num=0o51
dec_num=int(Oct_num)
print("Number after conversion is:"+str(dec_num))
"""

# How to find   Quadrant in which the given co-ordinate lies:

"""x=int(input("Enter the value of X-asix:-"))
y=int(input("Enter the value of Y-axis:-"))

if x>0 and y>0:
    print("according to the value in first quadrant ")
elif x<0 and y>0:
    print("according to the value in second quadrant")
elif x<0 and y<0:
    print("according to the value in third quadrant")
elif x>0 and y<0:
    print("according to the value in fourth quadrant")
else:
    print("X and Y at origin")
    """



""" import math
n=int(input("Enter the number of student:"))
r=int(input("Enter the number of seats:"))

num=math.factorial(n)
deno=math.factorial(n-r)

no_of_ways=num//deno

print("total number of ways are:"+str(no_of_ways))
"""

# finding maximum no. of Handshakes

"""N=int(input("Enter the number of people available:"))
no_of_handshakes=int(N*((N-1)/2))
print("Maximum number of handshakes can be :"+str(no_of_handshakes))"""


# Addition of two fraction number :

"""f1_nr=int(input("enter the numerator for 1st fraction:-"))
f1_dr=int(input("enter the denominator for the 1st fraction:-"))
f2_nr=int(input("enter the numerator for 2nd fraction:-"))
f2_dr=int(input("enter the denominator for 2nd fraction:-"))

if(f1_dr==f2_dr):
    fraction=f1_nr+f2_nr
    print("addition of two fraction are:"+str(fraction)+'/'+str(f1_dr))

else:
    fraction=(f1_nr*f2_dr)+(f2_nr*f1_dr)
    print("Addition of fractions are :"+str(fraction)+'/'+str(f1_dr*f2_dr))"""

# Repalce all zero's with 1 in any given integer :

"""n=int(input("enter any integer number:"))

s=str(n)
a=list(s)
r=''

for i in range(len(a)):
    if(a[i]=='0'):
        a[i]='1'
    r=r+a[i]

del n
print(int(r))
"""

# sum of all prime number :

"""n=int(input("enter the value:-"))
sum=0
avg=[]
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,"is prime.")
        sum=sum+i

print("sum of number is:-",sum)
type(n)
"""

"""n=[45,34,10,36,12,6,80]
avg=sum(n)/len(n)
print(round(avg,2))

print(type(n))"""

# checking character vowel or constant :-

"""Char=input("Enter the character:-")
if(Char=='a' or Char=='e' or Char=='i' or Char=='o' or Char=='u'):
    print("Character is vowel")
else:
    print("constant charater")


Char=input("Enter the character:-")
if(Char=='a' or Char=='e' or Char=='i' or Char=='o' or Char=='u'):
    print("Character is vowel")
else:
    print("constant charater")"""

# Area of circle:-
"""pi=3.14;
r=float(input("enter the radius of circle:-"))
area=pi*r*r
print("the area of circle is ",end=" ")
print(area)"""

# checking char are alphabets or not:-
"""n=input("Enter the char:-")
x=ord(n)
if(65<=x<=90 or 97<=x<=122):
    print('yes',n,"is an alphabert")
else:
    print("not an alphabet")
"""

# Ascii values of a char:-

"""char=input("Enter the character:-")
Asciival=ord(char)
print(Asciival)

# convert integer 65 to ASCII character :-
y=chr(65)
print(type(y))
for i in range(65,65+26):
    print(chr(i),end=",")"""

# Calculate number of digits in an integer:-
# Integer=int(input("Enter an integer:-"))
# String=str(Integer)
# print(len(String))


# (copy paste):- converting digit / number to word:-
"""def numToWords(num):
    length_of_string = len(num)
    if (length_of_string == 0):
        print("String is Empty")
        return;
    if (length_of_string > 4):
        print("Please enter the string with supported length")
        return;
    ones_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen"]
    multiple_of_ten = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    power_of_ten = ["hundred", "thousand"];
    print(num, ":", end = " ");
    if (length_of_string == 1):
        print(ones_digits[ord(num[0]) - '0'])
        return;
    x = 0
    while (x < len(num)):
        if (length_of_string >= 3):
            if (ord(num[x]) - 48 != 0):
                print(ones_digits[ord(num[x]) - 48], end = " ")
                print(power_of_ten[length_of_string - 3], end = " ")
            length_of_string -= 1
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x]) - 48)
                print(tens_digits[sum])
                return;
            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return;
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(multiple_of_ten[i], end = " ")
                else:
                    print("", end = "")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(ones_digits[ord(num[x]) - 48])
        x += 1

numToWords("1121")
numToWords("3421")
numToWords("9999")"""


# To see know the Number of days in any year

"""Month=int(input("Enter the month:-"))
year=int(input("enter the year:-"))
if(Month==2 and (year % 400 == 0)) or (year % 100 !=0) and (year % 4 == 0):
    print("Number of days is 29")
elif(Month==2):
    print("Number of days is 28")
elif(Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month12):
    print("Number of days is 31")
else:
    print("Number of days is 30")"""


# count number by their occurrence availability:-

"""number=int(input("Enter the number:-"))
digit=int(input("Enter the occurrence digit:-"))
String1=str(number)
String2=str(digit)
print(str(String1.count(String2)))"""

# Number of integers which has exactly x divisors:-

"""number=int(input("Enter range of number:-"))
divisor=int(input("Enter exact number of divisors:-"))
count1=0
for i in range(1,number+1):
    count2=0
    for j in range(1,i+1):
        if i%j==0:
            count2+=1
        else:
            pass
    if count2==divisor:
        count1+=1
        print(i,end=" ")

print("")
print(count1)"""

# finding the Roots of quadratic in python:-

"""import math

a=int(input("Enter value of a:-"))
b=int(input("enter the value of b:-"))
c=int(input("Enter the value of c:-"))

if a==0:
    print("A can not be zero.")
else:
    val=b**2-4*a*c
    root=math.sqrt(abs(val))

    if val>0:
        print("two real roots")
        print((-b+root)/(2*a))
        print((-b-root)/(2*a))
    elif val==0:
        print("one real root")
        print(-b/(2*a))
    else:
        print("no real roots")
        print(-b/(2*a),"+i",root)
        print(-b/(2*a),"-i",root)
        """


# Importnat codes related to array:-
# 1.Find smallest element:-

"""s=int(input("Enter array size:-"))
arr=[]
for i in range(s):
    element=int(input())
    arr.append(element)
print("Smallest element:-",min(arr))"""

# find second smallest number :-
"""n=int(input("Enter array size:-"))
arr=list()
for i in range(n):
    arr.append(int(input()))
arr=list(set(arr))
arr.sort()
print("second smallest element is:-",arr[1])

or 

mylist=[11,21,33,23,2,34,23,54,4]
mylist.sort()
print(mylist)
print("smallest number is :-",mylist[1])"""

# find largest element in an array:-

"""n=int(input("Enter size of array:-"))
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=list(set(arr))
arr.sort()
print("largest number is:-",max(arr))

or

mylist=[11,21,33,23,2,34,23,54,4]
mylist.sort()
print(mylist)
print("smallest number is :-",mylist[-1])"""


"""s=int(input("Enter array size:-"))
arr=[]
for i in range(s):
    element=int(input())
    arr.append(element)
print("Smallest element:-",min(arr))
print("largest element:-",max(arr))


mylist=[11,21,33,23,2,34,23,54,4]
mylist.sort()
print(mylist)
print("smallest number is :-",mylist[-1])
print("largest element in arary:-",mylist[0])"""

# find the sum of an array:-
"""s=int(input("Enter the array:-"))
arr=[]
sum=0
for i in range(s):
    element=int(input())
    arr.append(element)
    sum=sum+element
print("sum of array:-",sum)"""

# python program for reverse an arrray:

"""size=int(input("Enter the array:-"))
arr=[]
print("Enter the elements:-")
for i in range(size):
    element=int(input())
    arr.append(element)
print("The reversed array is:",arr[::-1],sep="\n")"""


"""arr=[2,3,4,5,8]
print(arr[::-1])"""


# sort the array in ascending and descending order :-

"""size=int(input("Enter array size:-"))
arr=[]
for i in range(size):
    element=int(input())
    arr.append(element)
print("Ascending order of array:-")
arr.sort()
print(arr)
print("Descending order of array:-")
arr.sort(reverse=True)
print(arr)"""


# sort first half in ascending order and second half in descending order array:

"""a=list(map(int,input("Enter array:-").split()))
x=[]
y=[]
n=len(a)
for i in range(n//2):
    x.append(a[i])

for i in range(n//2,n):
    y.append(a[i])

x.sort()
y.sort(reverse=True)
print("Resultant array",*(x+y))
"""

# finding the frequency of element in an array:-

"""n=int(input("Enter the array:-"))
arr=[]
print("Enter the array element:-")
for i in range(n):
    arr.append(int(input()))
x=list(dict.fromkeys(arr))

for i in x:
    print("\n {} occurs {} time(s)".format(i,arr.count(i)))
    """

"""from collections import Counter
array=[1,1,2,3,24,24,325,5,3,3,4]
print(Counter(array))
print(type(array))"""

# palindrome number:-
"""num=int(input("Enter the number:-"))
temp=num
reverse=0
while num>0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10

if temp==reverse:
    print("Given number {} is palindrome".format(temp))
else:
    print("Given number {] is palindrome".format(temp))
    """

# remove duplicates element i array:-
"""arr=list(map(int,input("enter array element").split()))
x=list(dict.fromkeys(arr))
print(x)
print("Element of array",arr)
print("Element of array without duplicates",x)
print("count of distinct element",len(x))"""

"""a=["sugar","milk","bread"]
print(a)
print(type(a))
print(a.insert(2,"salt"))
print(a)"""

import sys
lst1=[]
lst1.append(1)
lst2=[1]
print(sys.getsizeof(lst1),sys.getsizeof(lst2))




































