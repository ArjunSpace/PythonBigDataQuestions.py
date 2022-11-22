## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Q2. Why is Python called a dynamically typed language?

Q3. List some pros and cons of Python programming language?

Q4. In what all domains can we use Python?

Q5. What are variable and how can we declare them?

Q6. How can we take an input from the user in Python?

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Q8. What is type casting?

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Q10. What are keywords?

Q11. Can we use keywords as a variable? Support your answer with reason.

Q12. What is indentation? What's the use of indentaion in Python?

Q13. How can we throw some output in Python?

Q14. What are operators in Python?

Q15. What is difference between / and // operators?

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Q18. What are boolean operator?

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```

Q20. What are conditional statements in Python?

Q21. What is use of 'if', 'elif' and 'else' keywords?

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Q26. What is a string? How can we declare string in Python?

Q27. How can we access the string using its index?

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

string = "Big Data iNeuron"
print(string[9:16])

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

string = "Big Data iNeuron"
print(string[16:8:-1])

o/p : norueNi

Q30. Resverse the string given in the above question.
string = "Big Data iNeuron"

print(string[::-1])

o/p: norueNi ataD giB

Q31. How can you delete entire string at once?
string = "Big Data iNeuron"



Q32. What is escape sequence?

An escape character is a backslash \ followed by the character you want to insert.

Code    	Result	
\'	      Single Quote	
\\	      Backslash	
\n	      New Line	
\r	      Carriage Return	
\t	      Tab	
\b	      Backspace	
\f	      Form Feed	
\ooo	    Octal value	
\xhh	    Hex value
Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```
print("iNeuron's Big Data Course")

   or
  
print(' iNeuron\'s Big Data Course')


Q34. What is a list in Python?
The list is a sequence data type which is used to store the collection of data.
Lists in Python can be created by just placing the sequence inside the square brackets[].
A single list may contain DataTypes like Integers, Strings, as well as Objects. 
Lists are mutable, and hence, they can be altered even after their creation.


Q35. How can you create a list in Python?

Lists in Python can be created by just placing the sequence inside the square brackets[].


Q36. How can we access the elements in a list?

In order to access the list items refer to the index number. 
Use the index operator [ ] to access an item in a list. 
The index must be an integer. Nested lists are accessed using nested indexing. 


Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 
print(lst[4][2])

o/p: iNeuron

Q38. Take a list as an input from the user and find the length of the list.

def len_list():
  lst = list(input("enter the list: "))
  print(len(lst))

len_list()

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

lst = ["Welcome", "to", "Data", "course"]
lst.insert(3,'Big')
print(lst)
print(lst.index('Big')) #to verify the index

o/p: ['Welcome', 'to', 'Data', 'Big', 'course']
      3
Q40. What is a tuple? How is it different from list?

Q41. How can you create a tuple in Python?

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

Q44. Take a tuple as an input and print the count of elements in it.

Q45. What are sets in Python?

Q46. How can you create a set?

Q47. Create a set and add "iNeuron" in your set.

Q48. Try to add multiple values using add() function.

Q49. How is update() different from add()?

Q50. What is clear() in sets?

Q51. What is frozen set?

Q52. How is frozen set different from set?

Q53. What is union() in sets? Explain via code.

Q54. What is intersection() in sets? Explain via code.

Q55. What is dictionary ibn Python?

Q56. How is dictionary different from all other data structures.

Q57. How can we delare a dictionary in Python?

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
<class 'dict'>  
Q59. How can we add an element in a dictionary?

Q60. Create a dictionary and access all the values in that dictionary.

Q61. Create a nested dictionary and access all the element in the inner dictionary.

Q62. What is the use of get() function?

Q63. What is the use of items() function?

Q64. What is the use of pop() function?

Q65. What is the use of popitems() function?

Q66. What is the use of keys() function?

Q67. What is the use of values() function?

Q68. What are loops in Python?

Q69. How many type of loop are there in Python?

Q70. What is the difference between for and while loops?

Q71. What is the use of continue statement?

Q72. What is the use of break statement?

Q73. What is the use of pass statement?

Q74. What is the use of range() function?

Q75. How can you loop over a dictionary?


### Coding problems
Q76. Write a Python program to find the factorial of a given number.

def factorial(n):

    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(1, n+1):
        result = result * num
    
    return result
    

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

def simple_intrest():
  p = int(input('Enter the principle amount '))
  t = int(input('Enter the time duration in years '))
  r = int(input('Enter Annual rate of intrst '))
  SI = (p*t*r)/100
  return SI

simple_intrest()

 or
  
  def simple_intrest(**kwargs):
   p = kwargs['principle']
   t = kwargs['time']
   r = kwargs['rate']
   SI = (p*t*r)/100
   return SI

simple_intrest(principle = 1000, time = 2, rate = 2)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

def compound_intrest(**kwargs):
   p = kwargs['principle']
   t = kwargs['time']
   r = kwargs['rate']
   CI = p*(1+(r/100))**t
   return CI

compound_intrest(principle = 1000, time = 2, rate = 10)

Q79. Write a Python program to check if a number is prime or not.

def is_prime():
  n = int(input('Enter the number '))
  if n > 1:
    for i in range(2,n):  
      if n % i == 0:       # for checking factors of n
        print(n, 'is not a prime number')
        break     #if condition satisfies come out of loop
                  # as 1 multiple is enough
    else:
        print(n, 'is a prime number')

is_prime()
Q80. Write a Python program to check Armstrong Number.

def is_armstring():
  n = input('Enter the number ')
  sum = 0
  for i in n:
    r = int(i)
    sum += r**3
  if sum == int(n):
    print(n, 'is a arm string number')
  else:
    print(n, 'is not a arm string number')
is_armstring()  


Q81. Write a Python program to find the n-th Fibonacci Number.

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(8))

Q82. Write a Python program to interchange the first and last element in a list.

def interchange():
  lst1 = list(input("enter the list : "))
  print("original list : ",lst1)
  last_element = lst1[0]
  lst1[0] = lst1[-1]
  lst1.pop()
  lst1.append(last_element)
  
  print("list after exchanging elements : ",lst1)

interchange()

o/p:
enter the list : 12345
original list :  ['1', '2', '3', '4', '5']
list after exchanging elements :  ['5', '2', '3', '4', '1']

           or 
           
 list = list(input("enter the list : "))
list[0], list[-1] = list[-1], list[0]
print(list)

o/p:
enter the list : 12345
['5', '2', '3', '4', '1']

Q83. Write a Python program to swap two elements in a list.

def swap_pos(lst1,pos1,pos2):
  
  lst1[pos1], lst1[pos2] = lst1[pos2], lst1[pos1]
  return lst1

lst1 = [1,2,3,4,5,6,7]
swap_pos(lst1,1,4)

Q84. Write a Python program to find N largest element from a list.
ef Nth_max(n):
  list1 = list(input('enter the list : '))
  print('original list is :',list1)
  list1.sort()
  print('sorted list : ', list1)
  print(list1[-n])


Nth_max(4)

o/p:
enter the list : 123456
original list is : ['1', '2', '3', '4', '5', '6']
sorted list :  ['1', '2', '3', '4', '5', '6']
3

Q85. Write a Python program to find cumulative sum of a list.


def cum_list(list):
  #list must contain only numerics
  sum = 0
  for i in list:
    sum += int(i)
    
  return sum

list = ['1','2','3']
cum_list(list)
  
Q86. Write a Python program to check if a string is palindrome or not.
def is_polyndrome():
  string = str(input("enter the string :"))
  n = len(string)
  print(n)
  for i in range(0,int((n-1)/2)):
    if string[i] != string[(n-1)-i]:
      return ("No!! it is not a polyndrome")
  else:
    return ("yes!!, it is a polyndrome")

is_polyndrome()

o/p:
enter the string :RACECAR
7
yes!!, it is a polyndrome

Q87. Write a Python program to remove i'th element from a string.

def remove_item(str1,i):
  before_index = str1[:i]
  after_index = str1[i+1:]
  final_string = before_index + after_index
  return final_string
str1 = 'arjun'
remove_item(str1,3)

o/p:
   arjn

Q88. Write a Python program to check if a substring is present in a given string.
def sub_string():
  str = input("enter the input :")
  sub_str = input("enter the input :")
  if sub_str in str:
    print('yes!!, it is a substring') 
  else:
    print('No!!, it is not a substring try another')

sub_string()

o/p:
   enter the input :python is fun and joy
enter the input : joy
yes!!, it is a substring

enter the input :python is fun and cool
enter the input :joy
No!!, it is not a substring try another

Q89. Write a Python program to find words which are greater than given length k.
def words_of_length(str,k):
  lst = str.split()
  for i in lst:
    if len(i) > k:
      print(i)
      
    
str = "python is very fun as well as cool"
words_of_length(str,3)

o/p:
   python
   very
   well
   cool
Q90. Write a Python program to extract unquire dictionary values.
def extract_values(dict):
  lst = []
  for k,v in dict.items():
    #print(v)
    lst.append(v)
  #print(lst)
  unique = set(lst)
  print("unique dictionary values are", unique)


dict = { 'a' : 1, 'b' : 2, 'c' : 1}
extract_values(dict)

o/p: 
   unique dictionary values are {1, 2}
Q91. Write a Python program to merge two dictionary.

def merge_dict(dict_1,dict_2):
  dict_1.update(dict_2)
  return dict_1

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

merge_dict(dict_1,dict_2)

o/p:
   {1: 'a', 2: 'c', 4: 'd'}
Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```
def dict1(list):
  print(dict(list))


list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dict1(list)
o/p:
{'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```
def convertion_list(list):
  list1 = []
  for i in list:
    k = (i,i**3)
    list1.append(k)
  return list1

list = [9, 5, 6]
convertion_list(list)


Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```
def combination(tup1,tup2):
  list1 = [(i,j) for i in tup1 for j in tup2]
  list1 += [(j,i) for j in tup2 for i in tup1]
  return list1

tup1 = (7,2)
tup2 = (7,8)
combination(tup1,tup2)

o/p:
[(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```
def sort_tuple(list):
  list.sort(key = lambda list: list[1])
  return list


list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
sort_tuple(list)
Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
def shape(len):
  for i in range (len):
    for j in range(i+1):
      print("*", end = " ") #space included
    print()

len = 5
shape(len)

o/p:
* 
* * 
* * * 
* * * * 
* * * * *
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

def shape(n):
  for i in range(n):
    for j in range(i,n):
      print(' ', end = ' ')
  
    for j in range(i+1):
      print('*', end = ' ') #space between stars included
    print()   

shape(5)

o/p:
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```
def shape(n):
  for i in range(n):
    for j in range(i,n):
      print(' ', end = ' ')
    for j in range(i):
      print("*", end = " ")
    for j in range(i+1):
      print('*', end = " ")
    print()
shape(5)

o/p:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```
def shape_num(n):
  for i in range(n):
    for j in range(i+1):
      print(j+1, end = ' ')
    print()

shape_num(5)
o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 

def shape_alphabet(n):
  p = 65 #ASSCI value for A
  for i in range(n):
    for j in range(i+1):
      print(chr(p), end = ' ')    #chr converts asscci value to character
    p +=1
    print()

shape_alphabet(5)
o/p:
A 
B B 
C C C 
D D D D 
E E E E E




