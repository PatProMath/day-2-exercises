"""Data Types"""

# String
"Hello"[0]
string = "22-09-2022"
the_year = int(string[-4:]) # Substring by negative index.
print("Hello"[0])
print("123" + "456")
num_of_char = len("Joyous")

print(num_of_char)
# Integer

print(123 + 456)
print(236_859)

# Float

print(472_950.680)

"""
Type Checking
1. type() function: Outputs  <class 'type/base/object'>
""" 

print(type(472_950.68))

"""
Type Conversion
TypeError coming at you! Python can't concatenate integer(int) to string(str) The second line of code below will not run:

num_of_char = len(input("What is your best food? "))
print("This meal has "+num_of_char+" courses.")

But consider the following block of code:
"""

num_char = len(input("What is your best food? "))
print(type(num_char))
# 👆🏽Above, putting the input statement inside another function doesn't prevent it from being run. Try code out in Thonny. 
str_num_char = str(num_char)
print(type(str_num_char))

""" Now, we can concatenate """
print("This meal has "+str_num_char+" courses.")

print(70+float("103.6")) # Adds the integer 70 to the floating point number, 103.6 to give another floating point number as a result.
print(str(50)+str(40)) # Concatenates the string, "50" and the string "40" to give "5040"
print(int(4.9)) # Integer Type Conversion function, int(). It also rounds down a float number to the next lowest integer.
"""
Order of Operations

PEMDASL-R = P E MD AS L-R
()
**
* / Prioritized from Left to Right for multiplication and division

+ - Prioritized from Left to Right for addition and subtraction

"""

print(3 * 3 + 3 / 3 - 3) # 7

print(3 * (3 + 3) / 3 - 3) # 3

"""
Building a BMI (body mass index) Calculator

The formula is: weight (kg) / (height**2 (m**2)
"""
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)

print("Your BMI value is: "+str(bmi_as_int))

# Give some extra feedback to the user.
if bmi >=12 and bmi < 18.5:
  print("You are underweight. Consider a healthier lifestyle. You can do this.")
elif bmi >= 18.5 and bmi <= 24.9 :
  print("You have a healthy weight. Good work!")
elif bmi >= 25 and bmi <= 29.9 :
  print("You are overweight. Consider some exercises. You can do this.")
elif bmi >=30 and bmi < 40 :
  print("You are obese. A healthy diet and good exercise is key. Get on a plan, you can do it.")
elif bmi >= 40:
  print("You are extremely obese, but start today towards a healthy lifestyle. You can do this!")
else :
  print("Value is outside BMI range. Enter a valid measurement for height and weight.")

"""
Using the Python round() function
It rounds off the number. 
0 - 4: rounds down
5 - 9  rounds up
"""
print(round(1 / 4))
print(type(round(1 / 4))) # The type of the round function's output changes depending on what is the result gotten.
print(round(8 / 3,3))
print(type(round(8 / 3,3)))
print(round(8 / 3,0)) # Still a float.
print(type(round(8 / 3,0)))
# If one wants to get an int or integer value returned from a round function, don't bother with the second argument.

"""
Using a negative number makes the result less significant, that is, have less significant figures.

Find out more here: https://www.scaler.com/topics/round-function-in-python/
"""
print(round(20 / 3, -1)) # Rounds the result, 6.666... to 10.0 (a 1-significant figure number). The number's type is still float though.

""" Division, / 
The type of the result from any division is always a float or a floating-point number. Even the ones that have no reminders or decimals.
"""
print(2 / 1)
print(type(2 / 1))

""" Floor Division, //
The result it returns is an integer that has been rounded down. Works just like the floor function in Mathematics. The data type is automatically converted to int, or integer.
"""
print(8 // 3)
print(4 // 2)

""" f-Strings """
name = "Patricia"
age = 21
aChristian = True
# This is an 'f-String'. It allows us to put other data types inside the brackets.
f"Your name is {name}" 

print(f"My name is {name}. I am {age} years old. It is {aChristian} that I am a Christian.")

