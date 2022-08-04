# practicing getting input with if else statements

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you cant ride the rollercoaster")


# 3.1 Write a program that works out whether if a given number is an odd or even number.
# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# 3.2 Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# 🚨 Don't change the code below 👇
import math

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# bmi = round(weight / (height ** 2))
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# 3.3 Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# leap = False
#
# if year%4 == 0:
#     leap = True
#     if year%100 == 0:
#         leap = False
#     if year%400 == 0:
#         leap = True
# else:
#     leap = False
#
# if leap == True:
#     print("Leap year.")
# else:
#     print("Not leap year.")
