### Tiago Gomes - 2375703
### COP 1000 - #1284

### Pseudocode
### PROMPT the user to enter their total FSA Contribution for the year. Declare MAX: 3,200
### STORE this value in a variable called totalFSA
### CREATE variables for the running balance, and for the expense count.
### IMPLEMENT a WHILE loop to prompt the user to enter each FSA-Approved Expense.
### Within the While loop, increment the balance variable by the expense variable.
### INCREMENT the expense count, as long as the expense does not equal zero.
### If the user enters 0, end the while loop.
### After the loop ends, PRINT the total count of expenses, the total $ amount,
### as well as a message detailing whether their Expenses were At, Above, or Below their total contribution for that year.

def main () :
    totalFSA = int(input("Enter your FSA contribution for the year as a whole number (MAX-3200): "))
    
    balance = 0
    expenseCount = 0
    
    while totalFSA <= 3200:
        expense = int(input("Enter the FSA expenditure as a whole number (enter 0 to finish): "))

        balance += expense
        if expense != 0:
            expenseCount += 1
        
        if expense == 0:
            print(f'You have a count of {expenseCount} FSA expenditures for the year.')
            print(f'You have accumulated a total of ${balance:,} for the year.')
            if balance == totalFSA:
                print("Your expenditure total is the same as your FSA contribution.")
            elif balance > totalFSA:
                print("Your expenditure total is over your FSA contribution.")
            else :
                print("Your expenditure total is under your FSA contribution.")

        totalFSA = 0
        balance = 0
        expenseCount = 0

        
        
    
main ()
