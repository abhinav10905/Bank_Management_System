def delete_account(dict):
    a=int(input("Enter your account number:"))
    if a not in dict:
        print("Account not found")
    else:
        del dict[a]
        print("Account deleted successfully")
