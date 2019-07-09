# iteration (loops) with counting
    
again = True
while again:
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
        print "You are probably out of high school now?"

    for a in range(1,age+1):
        print "Happy birthday number ", a
        
    answer = raw_input("Again (y/n)?")
    if answer != 'y':
        again = False


    
        
    

