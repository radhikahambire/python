# this is single line comment
"""
This is multiline comment start and end with triple quotes
"""
print("Hello world !!")

# Variables
greeting = "Good Morning"
print (greeting + " Sanu!!")

'''
Naming Convention to variable:
1. variable should always start with letters
2. When variable names contains multiple words we should user "_" (underscore) to seperate the word. Example: happy_thoughts
'''
happy_thoughts = "happy"

print('I am very',happy_thoughts)

"""
Constant:
1. In Python, we dont have way to explicitly declaring something as constant
2. But to declare variable as constant we use upper case letters.
3. as Python is dynamically types language so we can edit constant values 
4. but in other language its completely prohibited to change the constant language and if we try to change it throws an error
"""
PI = 3.1415926
print("PI is ",PI)
PI=14
print("After constant value change, PI is",PI)

"""
Type Hinting:
1. Type hinting means we are explicitly declaring data type of declared variable.
2. to add type hinting, we add colon and data type to variable.
Ex: 1. name: str = "Mario"
    2. number: int = 15
"""
name: str = "Mario"
number: int = 15
print(number)

'''
Type Conversion:
1. Type conversion help us to mix different types together. But type should be similar or it should be related 
2. For example:
    number= 10
    text = "Test"
    result = number + int(text)
    print(result)
3. it will throw a type conversion error ValueError: invalid literal for int() with base 10: 'Test'
as types are not similar (Compatible) and related (Convertible)
'''
number= 10
text = "100"
result = number + int(text)
print(result)
print(bool(21))

'''
Integer: Integer is a whole number. It can be positive or negative without any limitation on length and without decimals.
For better readability of bigger number we can use underscore to format the number and the underscore will be ignore by python while reading 
'''
a=100
b=-100
c=100_000_000_000
print("Subtraction of a-b:", a-b)
print("Addition of b+c:",b+c)
print("Value of c:",c)

'''
Operators:
Arithmetic:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modular/modulo
Exponentiation:
7. Exponentiation power
8. Floor division
'''
x=10
y=50
z=3
addition=x+y
subtraction=x-y
multiplication=x*y
division=x/y
modular=x%y
exponentiation=x**z
floor_division=x//z
print("-----------Arithmetic Operators-----------")
print("Addition of x+y:",addition)
print("Subtraction of x-y:",subtraction)
print("Multiplication of x*y:",multiplication)
print("Division of x/y:",division)
print("Modular of x%y:",modular)
print("Exponentiation of x**z:",exponentiation)
print("Floor division of x//z:",floor_division)

'''
Assignment Operators:Assignment Operators are used to assign values to variables. 
They can also perform an operation and assign the result back to the same variable.
1. Assignment operator
2. Addition(+=)
3. Subtraction(-=)
4. Multiplication(*=)
5. Division(/=)
6. Modulo(%=)
7. Exponentiation(**=)
8. Floor division(//=)
'''
p=3
p+=5
p-=6
p*=7
p//=8
print("-------------Assignment Operators-----------")
print("Addition of p:",p)
print("Subtraction of p:",p)
print("Multiplication of p:",p)
print("Floor Division of p:",p)

'''
comparison operators: Comparison Operators are used to compare two values. They return a Boolean result: True or False.
1.equal (==)
2.not_equal (!=)
3. greater than (>)
4. less than (<)
5. greater than or equal to (>=)
6. less than or equal to (<=)
'''
a=8
b=90
print("--------Comparison Operators-----------")
print("Comparison of a==b",a==b)
print("Comparison of a!=b",a!=b)
print("Comparison of a>b",a>b)
print("Comparison of a<b",a<b)
print("Comparison of a>=b",a>=b)
print("Comparison of a<=b",a<=b)

'''
Logical Operators:Logical Operators are used to combine multiple conditions or reverse a condition. 
They return a Boolean result (True or False) when used with Boolean expressions.
1. and
2. or
3. not
'''
print("--------Logical Operators-----------")
print("a:",a, "\nb:", b)
print("a==b and b>a:",a==b and b>a)
print("a!=b or b<a:",a!=b or b<a)
print("not(a>b or b<a):",not(a>b or b<a))

'''
Identity Operator: Identity Operators are used to check whether two variables refer to the same object in memory, 
not just whether they have the same value.
1. is
2. is not
'''
print("--------Identity Operators-----------")
a=100
b=1.0*a
print("a:",a,"\nb:",b)
print("memory address of a:",id(a))
print("memory address of b:",id(b))
print("a is b:",a is b)
x=100
y=100
print("x:",x,"\ny:",y)
print("memory address of x:",id(x))
print("memory address of y:",id(y))
print("x is y:",x is y) #In Python if both variable hold exact same value then it refers tp same memory address so returns True

'''
Membership operator:Membership Operators are used to check whether a particular value or element exists in a sequence or collection, 
such as a string, list, tuple, set or dictionary.
Python has two membership operators:
1. in
2. not in
'''
s="string"
print("--------Membership Operators-----------")
print("s:",s)
print("i in s:",'i' in s)
lists=[1, 2,3,4,5]
print("list:",lists)
print("9 in list:",9 in lists)
print("9 not in list:",9 not in lists)
tuples=(1,2,3,4,5)
print("tuple:",tuples)
print("5 in tuple:",5 in tuples)
print("9 in tuple:",9 not in tuples)
dicts={1,2,3,4,5}
print("dict:",dicts)
print("5 in dict:",5 in dicts)
print("9 not in dict:",9 not in dicts)

'''
String: to create a string type we using quotation mark single('') or double(""). 
To creat multi line string we use triple quotation mark double("""String""") or single.
we can use single quotation inside double and vice versa
'''
print("------String------")
string="string"
print("string:",string)
multilinestring="""
1. To create a string type we using quotation mark single('') or double(\"\"). 
2. To creat multi line string we use triple quotation mark double or single.
3. We can use single quotation inside double and vice versa
"""
print("multilinestring:",multilinestring)
string_with_quotes='mark single("Str") '
print("string with quotes:",string_with_quotes)

'''
F-string: F-Strings are used to insert variables and expressions directly inside a string. 
They make string formatting easier, cleaner and more readable.
In Python, we use the letter f or F before the opening quotation mark.
1. Syntax: f"Text {variable}"
'''
print("---------F-Strings-----------")
print("Text:",string_with_quotes)
name = "Radhika"
age = 31
print(f"My name is {name} and I am {age} years old.")

a = 10
b = 20

print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")
print(f"Division: {b / a}")

'''
Boolean:
1. True: True represent 1
2. False: False represent 0
we can do addition of booleans types as well
'''
print("--------Boolean-----------")
print(f"True==True: {True==True}")
print(f"False+True:{False+True}")

'''
List:A List in Python is a collection of items stored in a single variable. 
Lists are used to store multiple values of different data types.
Lists are:
- Ordered – Items maintain their insertion order.
- Mutable – You can add, remove or modify elements.
- Allow duplicates – The same value can appear multiple times.
- Can store different data types – Integers, strings, floats, Boolean values, etc.
1. Creating a List
Lists are created using square brackets [].
2. Accessing List Elements (Indexing)
Python uses indexing to access list elements.
- Positive indexing starts from 0.
- Negative indexing starts from -1 (last element).
'''
print("--------List-----------")
people:list[str]=['Radhika', 'Pravin', 'Shradha', 'Sagar', 'Chaitrali', 'Rakesh' ]
print("List:",people)
print('first element of list:',people[0])
print('last element of list:',people[-1])

'''
List Slicing:In Python, to access a range of items in a list, we use a concept called List Slicing.
List slicing allows you to extract multiple elements from a list instead of accessing one element at a time.
1. Syntax
list_name[start:end:step]
Parameter	Meaning
start	    Index where slicing starts (included)
end	        Index where slicing stops (excluded)
step	    Number of positions to skip

we can replace element of list using range of items and assigning required values to specific range value we want to replace
Methods:
1. insert() – Add at a specific index
2. append() – Add an element at the end of the list
3. extend() – Add multiple elements or to combine two different list together
4. remove() – Remove a specific value
5. pop() – Remove an element, if we not shared index value to remove it will remove last element from list.
6. sort() – Sort elements
7. reverse() – Reverse the order
8. clear() - Clear all list element
'''
print("--------ListSlicing-----------")
print(f"people[0:2]: {people[0:2]}")
print(f"people[0:2]: {people[0:5:2]}")
# Replace value
people[0:2]=['Jai', 'Gurudev']
print(people)
#insert value
people.insert(2,'Anjali')
print(people)
#append value
people.append('Pandurang')
print(people)
#extend
people2:list[str]=['Radhika', 'Pravin']
people.extend(people2)
print(people)
#alternative to combine two list
new_people= people + people2
print(new_people)
# Remove specific value
people.remove('Sagar')
print(people)
#pop
people.pop(5)
people.pop()
print(people)
people2.clear()
print(people2)
#reverse the list
people.reverse()
print(people)
#sort
people.sort()
print(people)
'''
Tuple:A Tuple in Python is a collection of multiple items stored in a single variable. 
It is similar to a List, but the main difference is that Tuples are immutable, meaning you cannot modify their elements after creation.
Tuples are commonly used when you want to store data that should remain unchanged.
Important characteristics of Tuples
- Ordered: Maintains insertion order.
- Immutable: Cannot modify, add or remove elements after creation.
- Allows duplicates: Duplicate values are permitted.
- Multiple data types: Can store integers, strings, floats and Boolean values.
- Indexed: Supports positive and negative indexing.
You can create tuples from list by type conversion or type casting and vice versa
To access a range of items in a tuples, we use a concept called tuple Slicing.
Tuples have only two built-in methods for working with their elements.
Method	Purpose	Example
1. count()	Counts occurrences of a value	numbers.count(10)
2. index()	Returns the first index of a value	numbers.index(20)
'''
print("--------Tuple-----------")
people1:tuple ='Ram', 'Laxman', 'Seeta', 'Bharat', 'Shatrughan','Laxman'
print(f"Type of people: {type(people1)}")
print(people1)
'''
#Immutable
people.add("Radhika")
people1[0]='radhika'
print(people) #AttributeError: 'tuple' object has no attribute 'add'
'''
#allows duplicates
print(f"Zero index value: '{people1[0]}', Last index value: '{people1[-1]}'")
#length of tuples
print(f"Length of Tuple: {len(people1)}")

people_list: list[str]=list(people1)
print(f"People List by type casting: {people_list}")
print(f"new people tuple from list: {tuple(people_list)}")
#range
print(f"People from 0th index to 2nd index: {people_list[:2]} ")
print(f"All People from 2th index : {people_list[2:]} ")

#Count ()
print(f"Occurrences of 'Laxman' : {people1.count('Laxman')} ")
print(f"Index number of 'Laxman' : {people1.index('Laxman')} ")