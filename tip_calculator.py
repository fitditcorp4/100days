#Welcome to the tip calculator
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input("How many people will split the bill? "))

#total_bill_and_tip = (total_bill + (((total_bill * tip) /100)) / no_of_people)
total_bill_and_tip = ((total_bill + (total_bill * tip)/100) /no_of_people)

each_person_share = "{:.2f}".format(total_bill_and_tip)

print(f"Each person should pay ${each_person_share}")
