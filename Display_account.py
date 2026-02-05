def display_account(dict):
    a=int(input("Enter your account number:"))
    if a not in dict:
        print("Account not found:")
    else:
        print("Name : ",dict[a][0])
        print("Age : ",dict[a][1])
        print("Amount : ",dict[a][2])
    print("Account displayed successfully")
