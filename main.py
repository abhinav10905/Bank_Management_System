import Create_account
import Deposit_amount
import Withdraw_amount
import Display_account
import Delete_account

z='y'
dict={}
while z=='y':
    print()
    print("1:Create")
    print("2:Deposit")
    print("3:Withdraw")
    print("4:Display")
    print("5:Delete")
    print("6:Exit")
    a=int(input("Enter your choice:"))
    if a==1:
        Create_account.create_account(dict)
    elif a==2:
        Deposit_amount.deposit_amount(dict)
    elif a==3:
        Withdraw_amount.withdraw_amount(dict)
    elif a==4:
        Display_account.display_account(dict)
    elif a==5:
        Delete_account.delete_account(dict)
    elif a==6:
        z='n'
        print("Bank management system exited")
        print("Thank you for using bank management system")
    else:
        print("Invalid choice")
    
