name = "I am Daniel"    #anything in quotes is a string
print(name)              #prints the value of the variable 'name'

#multi line string
multi_line_string = """This is a multi-line string.
It can span multiple lines."""
print(multi_line_string)

#to access individual characters in a string, we can use indexing
print(name[0])  #indexing starts at 0
print(name[5])  #prints the character at index 5

#to access a range of characters, we can use slicing
print(name[0:5])  #prints characters from index 0 to 4

#string reversal using slicing
print(name[::-1])  #prints the string in reverse order

#updating a string (strings are immutable, so we create a new string)
name2 = name.replace("Daniel", "Alice")  #replaces "Daniel" with "Alice"
print(name2)
list_ = list(name)  #converts the string into a list of characters
list_[5] = "P"  #replaces the character at index 5 with "P"
list_[6] = "e"  #replaces the character at index 6 with "e"
name3 = "".join(list_)  #joins the list back into a string
print(name3)

#deleting from a string (strings are immutable, so we create a new string)
name3 = name.replace("Daniel", "")  #removes "Daniel" from the string
print(name3)
