print(2 + 5)
print('2' + 5)                                # Give error, because here '2' is a string which can't be add with an integer.
print(type('2'))                              # There will be many cases where, we will see a number will be inside of either double quote("") or single quote(''), so that will only act as string, but at some point we want it to be a number so that we can perform certion arithmetic operations, so we some how need to change the "type" of it.


a = "2"
print(type(a))
b = 3
a = int(a) + b                                # To change the type of a data, we need to use the typecasting method, we will right the data type in which we want it to be get converted, and the that variable inside of the parenthesis.
print(a)
print(type(a))


b = 6.78
print(type(b))
int_value = int(b)
print(int_value)
print(type(int_value))                        # Here, like this we can converted from int to float or string or anything, and other way around of it also.


name = "Pranab"
print(type(name))     
name_value = int(name)                        # But this is a very important point, like if a string contains all digits, then it can't be converted into either int or float or anything like this. 
print(type(name_value))


a = 5
print(type(a))                                # This is implicit typecasting, here we are not explicitly mentioning that variable 'a' is holding int data type, just like in other languages, because python understand the data type automatically.
print(2 + 3.5)                                # When this "3.5" float data type is getting added with "int" data type of 2, python automatically understand that the result will be in float.


first_name = "Pranab"                         # Here python understood, that our first_name variable is holding string value/data type.
last_name = "Sethi"                           # Our second value/last_name variable is also holding the string type of data, so these can be concatenated.
print(first_name + last_name)

last_name = "3"
print(type(last_name))
print(type(int(last_name)))                   # We can now typecasting into int, this is called explicit typecasting, where it convert the data type using inbuilt function.


print(bool(1))
print(bool(2))
print(bool(3))    
print(bool(100))                              # Boolean of any number except 0 gives us true. 
print(bool(-5))
print(bool("PW Skills"))                      # Boolean of string gives us true.
print(bool(""))                               # Boolean of empty string always give false.