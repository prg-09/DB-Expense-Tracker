import os 
import sqlite3

with sqlite3.connect("expenses.db") as conn:
    cursor = conn.cursor()

#Create table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount FLOAT NOT NULL,
        description TEXT 
    ) 
    """
)
conn.commit()


def add():
    print("Add your expenses here")
    while True:
        
        category = input("Enter the category of your expense: ")
        while True:
            try:
                amount = float(input("Enter the amount of your expense: "))
                break
            except ValueError:
                print("Enter valid amount:")
        description = input("Enter a description for your expense: ")
        expense = (category, amount, description)
        
        #insert in the table
        cursor.execute("""
                        INSERT INTO expenses(category,amount,description)
                        VALUES(?,?,?)
                        """,expense)
        conn.commit()
        
        choice = input("Do you want to add more expense?(yes/no)")
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            print("Add another expense")
        else:
            print("Enter either 'yes' or 'no'")

    
    

def view():
    print("Your expenses are:")
    db_expenses = cursor.execute("SELECT * FROM expenses")
    for i in db_expenses:
        print (i)


def delete():
    
    while True:
        view()
        while True:
            try:
                del_num = int(input("Enter the expense id you want to delete: "))
                break
            except ValueError:
                print("Please enter an integer as an expense id")
                
        cursor.execute("SELECT * FROM expenses WHERE id = ?",(del_num,))
       
        del_expense = cursor.fetchone()
        if not del_expense:
            print("Expense ID not found")
            return
        cursor.execute("DELETE FROM expenses WHERE id = ?",(del_num,))
        conn.commit()
        
        print(f"Deleted expense {del_num} successfully")
        
        choice = input("Do you want to delete more expenses?(yes/no): ")
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            print("Delete another expense")
        else:
            print("Enter either yes or no") 


def edit():
    while True:
        view()

        while True:
            try:
                edit_num = int(input("Enter the expense id you want to edit: "))
                break
            except ValueError:
                print("Enter a valid integer")

        cursor.execute("SELECT * FROM expenses WHERE id = ? ", (edit_num,))
      
        edit_expense = cursor.fetchone()
        if not edit_expense:
            print("Expense ID not found")
            return
    
        new_category = input("Category: ")

        while True:
            try:
                new_amount = float(input("Amount: "))
                break
            except ValueError:
                print("Enter a valid amount")

        new_description = input("Description: ")

        cursor.execute(
            """
            UPDATE expenses
            SET category = ?, amount = ?, description = ?
            WHERE id = ?
            """,
            (new_category, new_amount, new_description, edit_num)
        )

        conn.commit()

        print(f"Updated expense {edit_num} successsfully")
        while True:
            choice = input("Do you want to update more expenses? (yes/no): ")

            if choice.lower() == "yes":
                break 

            elif choice.lower() == "no":
                return  

            else:
                print("Enter either 'yes' or 'no'")

print("Choose what you want to perform:")
while True:
    try:
        choice = int(input("\n1.Add expense\n2.View expense.\n3.Edit expense\n4.Delete expense\n5.Exit\n"))
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            edit()
        elif choice == 4:
            delete()
        elif choice == 5:
            print ("Successfully exited. Thank you!")
            break  
        else:
            print("Enter your choice from 1 to 4")
    except ValueError:
        print("Enter valid choice\n")