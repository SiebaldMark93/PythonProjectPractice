#if/else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You are welcome to ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age <= 18:
#     print("Please pay $8")
#   else:
#     print("Please pay $16")
# else:
#   print("sorry you are not tall enough to ride this ride...")

#elif statements are used if there are more than 2 conditions

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You are welcome to ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $8")
  else:
    print("Please pay $16")
else:
  print("sorry you are not tall enough to ride this ride...")


print("Hey I need your help.")
answer = input("Can you help me? Yes or No? ")
if answer == "No":
  print("YOU SUCK")
else:
  print("Thank you")

#Check if number is odd or even
print("Lets check if a number is odd or even.")
number = int(input("What number do you want to check? "))
if number % 2:
  print("This number is odd.")
else:
  print("This number is even")
#OR
# if number % 2 == 0: #this means that if a number is divisible by 2 with 0 remainders, it is even
#   print("This number is even")
# else:
#   print("This number is odd")

#BMI Calculator 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clincally obese.")

#Leap year
#on every year that is evenly divisble by 4, except every year that is evenly divisible by 100, unless the year is also evenly divisible by 400

year = int(input("which year do you want to check"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It's a leap year!")
    else:
      print("Not a leap year.")
  else:
    print("It's a leap year!")
else:
  print("Not leap year.")
    