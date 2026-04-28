#for loops
a, b, c = int(input("Enter three numbers: ")), int(input()), int(input())
no_list = [a, b, c]
for items in no_list:
    print(' '.join(str(items)))   #prints each number in the list on a new line


#conditional statements in for loops
password = ' '
n = 3
for i in range(3):   #allows the user to enter the password 3 times
    password = input("Enter password: ")
    if password == 'mine':
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
        n = n - 1
    print("You have",n ,"attempts left.")
    if n == 0:
        print("No more attempts left. Access denied.")
        break


#while loops
password = ' '
while password != 'mine':
    password = input("Enter password: ")
    if password == 'mine':
        print("Access granted.")
    else:
        print("Incorrect password. Try again.") 
             