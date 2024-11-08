# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
print("Hello user, what is your name?")
while True:
    username = input("Name:")
    if username.isalpha(): 
        break
    else: print('INVALID. PLEASE ENTER LETTERS ONLY!')
   
# TODO: Ask the user for their age and store it in a variable
print("So what is your age?")
while True:
    age = input("Age:")
    if age.isdigit():
        break
    else: print('INVALID. PLEASE ENTER NUMBERS ONLY')

# TODO: Print a greeting using the name and age variables
print('Hello' ' '+ username + ', age ' + age )
#------------------------------------------------------------------------------------
# Question 2: Integer Operations
print ('Moving on......')
# TODO: Ask the user for the length of a rectangle and store it as an integer
print('What is the length of a rectangle?')
length = int(input ("number:"))

# TODO: Ask the user for the width of a rectangle and store it as an integer
print('What is the width of a rectangle?')
width = int(input ("number:"))

# TODO: Calculate the area of the rectangle
Area = length * width
# TODO: Print the result
print ('Area = ' + str(Area))
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print('What is the temperture?')
tempC = float(input ("Celcius:"))
user_temp = tempC
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Fahrenheit = (tempC * 9/5) + 32 

# TODO: Print the result rounded to two decimal places
print(f'Degree in Fahrenheit =  {round( Fahrenheit ,2)}')