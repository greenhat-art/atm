class Atm:

    #constructor for pin and card number
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    #balance
    def check_balance(self):
        print("Your balance is 100000000000")
    #new amount
    def withdrawl(self,amount):
        new_amount = 100000000000 - amount
        print("you have withdrawn "+str(amount) +" dollars .Your remaining balance is: "+str(new_amount)+" dollars")

#main function
def main():
    Card_number = input("Please enter your your card number: ")
    pin_number  = input("Please enter your pin: ")
    

    print("Choose your query: ")
    print("1.Balance  2.withdrawl")
    query = int(input("enter query number :- "))


    if (query == 1):
        new_user.check_balance()
    elif (query == 2):
        amount = int(input("enter the amount to be withdrawn:- "))
        new_user.withdrawl(amount)
    else:
        print("Please enter 1 for knowing your balance, or 2 for withdrawing money from your card")

if __name__ == "__main__":
    main()