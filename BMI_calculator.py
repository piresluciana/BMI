from sys import argv

script, user_name = argv

print("Do you want to calculate your BMI?")
print("if you don't want that, hit CTRL-C.")
print("If you want that, hit RETURN")

input(">")

print("what is your weight in Kg {} ?".format(user_name))
weight = float(input(">"))

print("what is your height in metres {} ".format(user_name))
height = float(input(">"))

BMI = weight / (height*height)

print(round(BMI, 2))

if BMI < 18.5:
    print("Your BMI is {} which means you are underweight".format(round(BMI, 2)))
elif BMI >= 18.5 and BMI < 25:
    print("Your BMI is {} which means you are normal".format(round(BMI, 2)))
elif BMI >= 25 and BMI < 30:
    print("Your BMI is {} which means you are overweight".format(round(BMI, 2)))
elif BMI >= 30:
    print("Your BMI is {} which means you are obese".format(round(BMI, 2)))
else:
    print("there is an error with your input")

