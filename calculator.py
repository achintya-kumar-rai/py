arth=0
while arth!=5:
    n_of_number=int (input('''enter the number of the operante
                           min 2
                           max 3'''))
    a1=int(input ("enter the first number "))
    a2=int (input ("enter the second number"))
    if n_of_number==3:
        a3=int(input("enter the third number"))
        print('''enter  1 for addition 
        2 for multiplication
        3 to close the calculator''')
        arth=int(input ('''enter the operation'''))
        if arth ==1:
            print("sum of the two number is ",a1+a2+a3)

        elif arth==2:
            print ("multiplation of the two number is ",a1*a2*a3)

        elif arth==3:
            print("thank you and have a nice day bye bye ")
            break


    else:
        print('''enter  1 for addition 
        2 for substraction
        3 for multiplication 
        4 for divison
        5 to close the calculator''')
        arth=int(input ('''enter the operation'''))
        if arth ==1:
            print("sum of the two number is ",a1+a2)

        elif arth==2:
            print ("first number minus second number is  ",a1-a2)

        elif arth==3:
            print ("multiplation of the two number is ",a1*a2)

        elif arth==4:
            print ("first number divided by second number is ",a1/a2)

        elif arth==5:
            print("thank you and have a nice day bye bye ")
            break