
#string object is immutable
my_string = 'Hello world'
pring(my_string, id(my_string))
#my_string[0] = 'T'
my_string = my_string[:5] + ",my " + my_string[6:]
print(my_string, id(my_string))