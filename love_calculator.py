# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name = name1 + name2
namex = name.lower()
print (namex)
print(type(namex))
print(type(namex.count("e")))

true = str(namex.count("t") + namex.count("r") + namex.count("u") + namex.count("e"))


love = str(namex.count("l") + namex.count("o") + namex.count("v") + namex.count("e"))

true_love = true + love
print(true_love)
love_score = int(true_love)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")

elif (love_score >= 40) and (love_score <=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
