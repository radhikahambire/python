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