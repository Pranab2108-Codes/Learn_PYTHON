a = 5                                                        # This will be stored in the memory let it be like a container, means inside of this container the value will be stored, and whenever we want to access it, we must have to use the name of it like "a".


b = "Pranab"                                                 # This Pranab going to be store in the shape of array, means all characters will be in continuous manner, at index(0)->P, index(1)->r, index(2)->a and so on, this is called positive indices.
print(b[0])
print(b[2])

print(b[-2])                                                 # This same thing can be done by negative indices also, means accessing from ending, like index(-1)->b, index(-2)->a, index(-3)->n and so on.


list_container = [1, 2, True, 5.9, "Pranab", 9-4j]           # This data structure in python called as list, it can hold any type of data like, integer, float, boolean, complex number anything at a single time.
print(type(list_container[3]))                               # This list can be also access, like we were accessing in the string like using positive indices as well as negative indices.
print(type(list_container[-2]))


list_container[-2] = "Piyush"                                # We can see this clearly, "Pranab" got changed into "Piyush", that's what called mutability.
list_container[3] = None
print(list_container)                                        # So we can say this "list" is a type of object which is mutable in nature.


str = "PWSkills"                                             # This is a string type of object/container.
str[4] = 'z'                                                 # String is immutable in nature, so we cn say this, after got created it can't be changed, not even it's single index can be change, so it wil throw an eeror of "TypeError: 'str' object does not support item assignment".