a = 3                                           # Variables/Identifiers are the placeholders, where we keep variety of data which we can use to write logic.
print(a)                                        # Variable is a reserved memory space for storing value.

a = 4.5                                         # Here we re defined our variable "a" from integer to a float number.
print(a)                                        # When ever we define a variable, in RAM there will be a space which get created with the value of that variable just like in this case, value will be 4.5 and the address to access this value will be name as a.


b = "Pranab"
print(type(b))                                  # This is a string type.


c = True
print(type(c))                                  # It will be a boolean type.


print(True * False)                             # We can do the operations of this also.
print(True/False)                               # We can't do it because int math "1/0" is not defined.


d = None
print(type(d))                                  # None is also a type in python.


complex = 5+6j
print(type(complex))                            # We can define complex number in python also.
print(complex.real)                             # In this way we can access to the real value of the complex number.
print(complex.imag)                             # In this way we can access to the imaginary part.

                                                
5 = a                                           # Rules of defining a varibale: variable start with a letter(Alphabet) or underscore character and it should not be a keyword, So we can't start with the digit/number, because it is an invalid way.
data-science = "PWSkills"                       # We can't use like this while defining variable, like in here using the subtract symbol.
data science course = "PWSkills"                # We can't also use the space between the words, while defining the variable.
@abc = 2.3                                      # We can't start with the special characters also while defining the variable.
print = "Ajay"                                  # We can use the keywords to define as a variable but, once we define it, the original job/purpose of that keyword going to be lost.
print("World")                                  # So that's why, when we will do like this, it will throw an error of "TypeError: 'str' object is not callable".

name = "Pranab Sethi"                           # This is the valid way to define a variable.
print(name)

_name = "Piyush Sethi"                          # This is also we can do while defining a variable.
print(_name)

data_science_course = "PWSkills"                # This is the correct way to define a variable when there will be more than 1 words present in the variable, by using the underscore(_) between them.
print(data_science_course)


                                                # This is a single line comment, so when ever we use comments we normally need to use this "#" symbol.
                                                # Comments been use to increase the readability of the code, it will always ignore by the compiler. 
                                
                                                # When ever we want the multiple lines to be commented we should use triple quotes at the start as well as at end.
                                                # Like '''Hey
                                                # everyone 
                                                # i am Pranab.'''  
                                                
                                                # or 

                                                # """Hey Google,
                                                # I am here
                                                # to give my intervuew."""


str = "My name is Pranab"
print(str)                                      # Here the "print", "type" all these words are the pre defined words in python, which hold special meaning and have specific purpose in python.
type(str)                                       # So these pre defined words are called keywords.

help("keywords")                                # In this way we can findout how many keywords are exactly there.


if 3 > 2:
  print("Greater number")                       # This space before the "print" is called indentation.


a = 69                                          # This is called as a "statement", whose meaning is, it is a fundamental block of code.
name = "Pranab Sethi"                           # This is also, statement can be of any type like, it might be an expression, assignment, condition, loop.


a = 8                                           # Assignment statement.


a*b                                             # Expression statement.
print(a*b)


name = input("Please enter your name: ")        # This "input" keyword let us to take the input from the user, rather than doing it manually by us.
print(name)
print(type(name))                               # Even though we will put a digit in to this name it will still be a string, because this "input" keyword always take the input as string.

print(type(int(name)))                          # This is called as typecasting, even though "input" is taking the string, we can manually convert these into anything by typecasting.        