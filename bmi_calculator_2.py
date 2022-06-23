#import pandas as pd
#import numpy as np
#print("How much do you weigh in kg?", end= ' ')
weight = float(input("How much do you weigh in kg?"))
#print("What is your height in meters?", end= ' ')
height = float(input("What is your height in meters?"))
#bmi = weight / (np.square(height))
bmi = weight / (height**2)
print(f"So, your BMI is {bmi}")
if 25.0 < bmi < 29.9:
    print("You are overweight")
elif 18.5 < bmi < 24.9:
    print("You're a healthy weight")
elif 30.0 < bmi < 39.9:
    print("You're obese")
elif bmi >= 40:
    print("You're severly obese")
