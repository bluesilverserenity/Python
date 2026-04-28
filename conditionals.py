#If statement
Age = int(input("Enter your age: "))
if Age >= 18: print("Eligible to vote.")

#If-else statement
Name = input("Enter your name: ")
if len(Name) >= 7:
    print("Your name is long.")
else:
    print("Nice name!")

#If-elif-else statement
Number = int(input("Enter a number: "))
if Number > 0:
    print("The number is positive.")
elif Number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
