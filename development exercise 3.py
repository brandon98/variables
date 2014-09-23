#Brandon Dickson
#Development Exercise 3
#23-09-2014

height_inches=int(input("Please enter your height in inches:"))
weight_stone=int(input("Please enter your weight in stones:"))

height_cm= height_inches*2.54
weight_kg= weight_stone*6.364

print("Height in cm:{0}  Weight in kg:{1}".format(height_cm,weight_kg))
