**Project title**

Bank Management System(BMS)

**Overview of the Project**

A BMS is basically an integrated enterprise-wide information system that does not rely on manual paper-based processes for data maintenance, thus providing a secure and efficient interface, friendly to end-users--both bank personnel and customers.

**Features**

The system executes the following major banking activities:

Account Creation (Create_account): This shall allow the new user to be created, including the details required to open the account, generate a unique account number, and persistently store it in a file or simple database.

Deposit Funds: Deposit_amount-This allows a user to deposit funds into an already existing account number, upon proper verification of the account number.

Withdraw Amount: This will allow the user to draw funds from an account. It includes the logic to check for minimum balance and adequate funds.

display_account - Displays Account Details: This fetches and then presents the current balance and account information for any given account number.

Delete Account: This will irreversibly remove an account from the system once confirmed.

Main Menu - main.py: This contains a simple, interactive, console-based menu to navigate through major functionalities.

**Testing Instructions**

Start the application using the command python main.py.

Test 1: Create Account: Enter choice 1 to select Create_account. Give inputs for initial details. Note down the generated Account Number.

Test 2 Deposit Select option 2 Deposit_amount Enter account number from test 1 and deposit amount.

Test 3: Display: Select option 4 (Display_account). If the deposited amount is reflected in the balance, input the account number.

Test 4 - Withdrawal (Successful): Select option 3, Withdraw_amount. Withdraw an amount smaller than the balance. Verify the new balance using option 4.

Test 5: Withdrawal (Failure): Select option 3, try to withdraw more than the balance and see the insufficient funds message.

Test 6: Account Delete: Select option 5: Delete_account. Click on account number. Provide confirmation for deletion.

Test 7: Verification Attempt to display the deleted account (option 4) and check if "Account not found" is displayed.
