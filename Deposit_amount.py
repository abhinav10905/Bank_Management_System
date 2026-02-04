def deposit_amount(dict):
    a=int(input("Enter your account number:"))
    if a not in dict:
        print("Account not found")
    else:
        b=float(input("Enter amount to deposit:"))
        dict[a][2]+=b
        print("Amount deposit successful")
