# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
rem_yrs = 100 - age_int
rem_days = (100 - age_int) * 365
rem_weeks = rem_yrs * 52
rem_days = rem_yrs * 365
rem_mnths = rem_yrs * 12

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_mnths} months left. ")
