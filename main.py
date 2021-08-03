
seat=[1,2,3,4,5,6,7,8,9,10]

def  list_Empty():

    for i in seat:
        print(i,end="\t")
    main()

def book(seatnum):

         if seatnum in seat:
             print("You have succesfuly reserved a seat number " + str(seatnum))
             seat.remove(seatnum)


         elif seatnum not in seat and seatnum<len(seat):
             print("The seat has been occupied")
         elif seatnum not in seat:
             print("Out of range")
         else:
             print("try again")

         list_Empty()
         main()

def cancelled():
    inpp=int(input("Enter the seat number you want to cancelled "))
    if inpp not in seat and inpp<=len(seat):
        print("You have succesfully cancelled seat number " + str(inpp))
        seat.append(inpp)
        seat.sort()
        list_Empty()
    elif inpp>len(seat):
        print("Cannot cancelled the number because its out of range")




def main():
    print("\nwhat do you want to performed")
    print("\n1.List empty seat\n2.Book a seat\n3.cancelled a seat")

    choice = input("Enter your Choice :")
    if choice == '1':
        list_Empty()
    elif choice == '2':
        x=int(input("Enter the seat number you want to booked: "))
        book(x)
    elif choice =='3':
        cancelled()
main()
