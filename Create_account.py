def create_account(dict):
    a=input("Enter your name:")
    b=int(input("Enter your age:"))
    c=float(input("Enter initial deposit amount:"))
    d=[a,b,c]
    e=len(dict)+1
    dict[e]=d
    print("Account created successfully! Your account number is:",e)
    
            
