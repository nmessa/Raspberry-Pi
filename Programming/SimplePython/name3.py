# selection (making decisions)

name = raw_input("What is your name? ")
print "Hello", name
age = int(raw_input("How old are you? "))
newage = age + 1
print "Next year you will be ", newage

if age>=5 and age<19:
    print "You are still in school"
elif age < 5:
    print "You have not started school yet?"
elif age >= 19:
    print "You are probably out of school now?"


