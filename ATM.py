cb = 0.0
x = 1000
for i in range(x):
    print(" Welcome to a SBI ATM")
    print(" Chouse your Option as per their Number")
    print("  1.Withdraw \n  2.Deposite \n  3.Current Balance \n")

    o = input(" Enter Your Option : ")
    if o == "1" :
        wid = float (input("\n Enter Amount that you Wirhdraw : "))
        cb = float (cb - wid)
        print("\n Your Current Balence is ",cb)
    elif o == "2" :
        dep = float (input(" Enter how many Amount you Deposite : "))
        cb = float (cb + dep)
        print("\n Your Current Balance is ",cb)
    elif o == "3" :
        print(" Your Current Balance is ",cb)
    else:
        print(" Improper choice \n Please Retry Again")
    print(" Thank You for Chosing SBI \n")