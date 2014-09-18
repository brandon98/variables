money=int(input("please enter your amount of money:"))

twenties=money//20
remainder=money%20

tens=remainder//10
remainder=remainder%10

fives=remainder//5
remainder=remainder%5

twos=remainder//2
remainder=remainder%2

ones=remainder//1
remainder=remainder%1

print("£20 notes:{0}   £10 notes:{1}   £5 notes:{2}   £2 coins: {3}   £1 coins:{4}".format(twenties, tens, fives, twos, ones))
