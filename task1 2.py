'''Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''

#1.  Takes two numbers as input from the user.

a = float(input("Enter the first number: " ))

b = float(input("Enter the Second number: " ))

'''2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division'''

add= a +b 

sub =a-b

multi = a* b

if b != 0:
    divi= a/b
else:
    divi = "undifan"


print(f"Addition: {add}")
print(f"Suntraction: {sub}")
print(f"Multiplication: {multi}")
print(f"Division: {divi}")



'''Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

name = str(input("Enter your first name :" ))

lastname =str(input(" Enter your last name : "))

fullname =name +" "+lastname


print(f"Hello , {fullname}! welcome  to the pythone program .")

