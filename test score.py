#Brandon Dickson
#Test score exercise
#25-09-2014

test_score =int(input("Please enter your test score: "))

if test_score >= 40 and test_score < 50:
    print("E grade.")
elif test_score >= 50 and test_score < 60 :
    print("D grade.")
elif test_score >= 60:
    print("C Grade.")
elif test_score >= 70:
    print("B Grade.")
elif test_score >= 80:
    print("A grade.")
else:
    print("Fail.")
