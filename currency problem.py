#Brandon Dickson
#Currency Problem
#18-09-2014

money=int(input("please enter the amount of money:"))

twenties= money//20
remainder= money%20

tens=remainder//10
remainder= remainder%10

fives=remainder//5
remainder=remainder%5

twos=remainder//2
remainder=remainder%2

ones=remainder//1
remainder=remainder%1

print("£20 notes:{0} £10 notes:{1}".format(twenties, tens))

print("£10 notes:{0}".format (tens))

print("£5 notes:{0}".format (fives))

print("£2 coins:{0}".format (twos))

print("£1 coins:{0}".format (ones))


