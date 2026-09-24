a = 3                                                   # Operators are use to manage the data, do computations and help us to make decision using datas or variables.
b = 4
print(a+b)                                              # This sign '+' is the addition operator which is use to do additions.

                                                        
add = a + b                                             # Arithmetic operators.
print(add)                                              # Addition opearator.

print(100 - 3)                                          # Subtraction operator.

print(3 - 5)

print(3 * 6)                                            # Multiplication operator.

print(21 / 4)                                           # Division operator.

print(34 % 5)                                           # Modulo operator.

print(2 ** 3)                                           # This is pronounce as 2 to the power of 3.

print(4 // 3)                                           # Floor operator.

                                                      
print(2 == 2)                                           # Comparision operator, it compare 2 values and return a boolean value, either true or false.                                           
                                                        # Both are equal, so ofcourse it will show us as true.
print(2 != 2)                                           # It should be false, because 2 is equal to with 2.

print(5 != 2)                                           # We know this 5 is never equal with 2.

print(10 > 2)

print(10 <= 10)

                                                       
print(True and True)                                    # Logical operator, there are total 2 types of logical operators are there, 1 is for 'AND' another is for 'OR'.                                

print(0 or True)

print(1 and False)                                      # Up to these are the boolean operator.

print(not True)                                         # This is called as not operator.                 

print(not False)

                                                       
a = 10                                                  # Now we talk about the assignment operator.
print(a)
a + 5
print(a)

b = 14
print(b)
b += 6                                                  # This is called as the shortcut of addition.
print(b)
b -= 8
print(b)                                                # This shortcut can be done by subtract, multiplication and division also.
b *= 2
print(b)
b /= 3
print(b)

                                                        
a = "PWSkills"                                          # Memebership operator.
print("p" in a)                                         # Because 'p' is in capital letter in this word "PWSkills".  
print("p" not in a)                                     # That's why it will show us True. 

b = "Pranab"
print("ana" in b)                                       # We can only check either one character or a substring ofcourse which is continuous.
print("Pr" not in b)                                    # Give us False.

c = ["data", "analytics", 'science']
print("data" in c)
print("sci" in c[2])

                                                        
a = 2                                                   # Identity operator, which compares the location of 2 objects/variables.
b = 3
print(a is b)                                           # We know this 'a' is in another memory block, as well as 'b' is in another memory block, so their addresses are not same at all. 
print(a is not b)                                       # They are both in different memory block, so that's why it will give us True.

a = 2
b = a
print(a is b)                                           # Now we have assigned the address of 'a' to 'b', so now we can say this, 'b' also pointing to the same address where a is pointing.
print(a is not b)


print(10 & 10)                                          # Now we will see about bitwise operator, where we can perform operations at bit level.
print(bin(10))                                          # Representation of 1 is 2^3 2^2 2^1 2^0  --->  0 0 0 1 and representation of 2 is 2^3 2^2 2^1 2^0 ---> 0 0 1 1 and so on.
                                                        # This is called bitwise AND(&) operator, representation of 10 is 1010, we can check the representation by doing this.
print(3 | 5)                                            # This is calles bitwise OR(|) operator, representation of 3 is 0011 and representation of 5 is 0101.
print(bin(3 | 5))                                       # This is the representation of 7, which is 0111 and also the result of bitwise OR between 3 and 5.                         
                                                        
                                                                                   
print(~3)                                               # Now it's time for negation, which is symbolized as '~'.
print(-100)


print(5 ^ 3)                                            # This '^' operator called as bitwise XOR(^) operator, there is only one rule of it, the result will always be 0 at there when both the inputs will be same.
                                                        # Representation of 5 is 0101 and 3 is 0011, so after doing this xor we will get 6 whose representation is 0110.

print(35 << 3)                                          # Now it's time for shift operator, there are total 2 types of it, this is left shift operator(<<), it will shift the representation towards left by a specified number of position by filling 0s at the right end.
print(bin(35))                                          # This is the representation of 35 is 100011, after shifting left to 3 times, the result will be clearly 100011000.                                    
print(bin(35 << 3))                                     # This is the the representation of 280.
   
print(280 >> 3)                                         # This is the right shift operator.
print(bin(280))                                         # Thi is the representation of 280 is 100011000, so after shifting right 3 times means, total 3 digits from right end will be erased, so the final representation will be 100011.
print(bin(280 >> 3))                                    # Through this we can assure ourself.


print(2+3-8)                                            # Execution of python statement will be from left to right. 


print((5+3) - 4)                                        # Now we will know about order of precedence in python.
print(4 - (5+3))                                        # In the precedence order, bracket/paranthesis always comes 1st, that's why here also 1st it got calculate which is inside of the paranthesis.