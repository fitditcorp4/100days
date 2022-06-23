P = float(input ("What is your Principal?"))
#r = float(input("The nominal interest rate as a decimal"))
R = float(input("What is the annual nominal interest rate as a percent. If compounding is done monthly for example this will become the interest rate x 12?"))
r = R/100
n = float(input("What is the number of compounding periods per unit of time. Usually once annually?"))
t = float(input("What is the time in decimal years; e.g.6 months is calculated as 0.5 years and 18 months is 18/12=1.5?"))
nt = n*t
A = P*(1 + r/n)**nt
print(f"Your accrued amount after{t}years is {A}")
