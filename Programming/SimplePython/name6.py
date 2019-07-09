# modules (functions)

age = 0

def checkAge():
    if age>=5 and age<16:
        print "you are still at school"
    elif age < 5:
        print "you have not started school yet?"
    elif age > 20:
        print "you are probably working now?"
    
again = 1
while again:
    name = raw_input("what is your name? ")
    print "hello", name
    age = int(raw_input("How old are you? "))
    newage = age + 1
    print "next year you will be ", newage
    checkAge()

    answer = raw_input("another go?")
    if answer != 'y':
        again = 0

