# This is a sample Python function.
def fun():
    print("Welcome")

fun()    

#A function to convert minutes to hours taking minutes as a user input
minutes = int(input("Enter the number of minutes: "))
def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours    

result = minutes_to_hours(minutes)
print("That is equal to", result, "hours")

#A function with more than one parameter, this function takes two numbers as input and returns their sum
minutes, seconds = int(input("Enter the number of minutes: ")), int(input("Enter the number of seconds: "))
def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

result = minutes_to_hours(minutes, seconds)
print(f"That is equal to {result: .2f} hours.") #the : .2f in the f-string formats the result to 2 decimal places
