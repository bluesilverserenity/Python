#a variable stores a value
now = "Good morning"
print(now)
#now is a variable that stores the string "Good morning"

#multiple variables can be assigned in one line with same or different values
x = y = z = 0             #same value assigned to multiple variables
print(x, y, z)
a, b, c = 1, 2, 3         #different values assigned to different variables
print(a, b, c)

#swapping values of two variables
a, b = 10, 15
a, b = b, a
print(a, b)              #a is now 15 and b is now 10

print([m for m in dir(now) if not m.startswith('_')])  #prints all the attributes and methods of the variable 'now' that do not start with '_'
