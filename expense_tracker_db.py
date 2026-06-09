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
        
        choice = input("Do you want to add more expense?(yes/no)")
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            print("Add another expense")
        else:
            print("Enter either 'yes' or 'no'")

    #insert in the table
    cursor.execute("""
                    INSERT INTO expenses(category,amount,description)
                    VALUES(?,?,?)
                    """,expense)
    conn.commit()
    

def view():
    print("Your expenses are:")
    db_expenses = cursor.execute("SELECT * FROM expenses")
    for i in db_expenses:
        print (i)


def delete():
    
    while True:
        view()
        del_num = int(input("Enter the expense id you want to delete: "))
        cursor.execute("DELETE FROM expenses WHERE id = ?",(del_num,))
        conn.commit()
        print(f"Successfully deleted expense {del_num}")
        choice = input("Do you want to delete more expenses?(yes/no): ")
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            print("Delete another expense")
        else:
            print("Enter either yes or no") 


def edit():
    
    view()
    edit_num = int(input("Enter the expense id you want to edit"))
    new_category = input("Category: ")
    new_amount = float(input("amount: "))
    new_description = input("description: ")

    cursor.execute(" UPDATE expenses SET category = ?,amount = ?, description =?  WHERE id = ?", (new_category,new_amount,new_description,edit_num))
    conn.commit()


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