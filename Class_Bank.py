#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from Class_Account import *
from Class_Customer import *

import json

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customer_list = []
        self.current_customer = None
        self.bank_dictionary_list = []
        
    def online(self): #en variabel som ska innehålla inloggad kund, vissa funk ska endast fungera ifall kund är inloggad
        if self.current_customer != None:
            return True
        return False
    
    def add_account(self, balance = 0): #ska hitta rätt kund och sedan anv. add_acc från den customern
        if self.online():
            return self.current_customer.add_account(balance)
        else:
            return print("User not online.")
        
    def get_customers(self): #lista alla kunder
        for customer in self.customer_list:
            print(customer)
        
    def add_customer(self, username, password):
        if self.get_customer(username) == False:
            self.customer_list.append(Customer(username, password))
        else:
            return print("Username already exist.")
    
    def get_customer(self, sought_username):#hämta en kund via användarnamn
        for customer in self.customer_list:
            if customer.username == sought_username:
                return customer
        return False
                
    def change_customer_password(self, username, new_password): #loopa igenom användare, när dem hittat den vi letar efter sätter vi password == new_password
        if self.online():
            for customer in self.customer_list:
                if customer.username == username:
                    customer.password = new_password
                    print("Password successfully changed.")
                    return customer.password
                else: 
                    return print("Could not change password.")
        else:
            return print("User not logged in.")
    
    def remove_customer(self, username):
        for customer in self.customer_list:
            if customer.username == username:
                self.customer_list.remove(customer)
                print("Customer removed.")
    
    def login(self, username, password):
        for user in self.customer_list:        
            if username == user.username and password == user.password:
                self.current_customer = user
                print("User logged in.")
         
    def logout(self): #ta bort nuvarande anv från inloggade variabeln
        self.current_customer = None
        print("User logged out.")
    
    def get_accounts(self): #hämta alla konton som tillhör anv. som just nu är inloggad
        if self.online():
            return self.get_customer(self.current_customer.username).account_list
        else: 
            return print("User not online.")
    
    def remove_account(self, account_number): #ta bort ett konto för den kund som är inloggad
        if self.online():
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    self.current_customer.account_list.remove(account)
                    return print("Success!")
                return print("Not a valid number.")
        else:
            return print("User not online.")
               
    
    def get_account(self, account_number):
        if self.online():
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    return account
                return False
        else:
            return print("User not online.")
        
        
    def deposit(self, account_number, amount): #loopa igenom customer accounts
        if amount < 0:
            print("Can't be a negative number.")
            return
        if self.online() == True:
            for account in self.current_customer.account_list:
                if account.account_number == account_number:
                    account.change_balance(amount)
                    return print("Deposit succeeded.")
                return print(f"Account {account_number} could not be found.") 
        else:
            return print("User not online.")
    
    def withdraw(self, account_number, amount):
        if amount < 0:
            return print("Can't be a negative number.")
            if self.online():
                for account in self.current_customer.account_list:
                    if account.account_number == account_number:
                        if account.balance < amount:
                            return print("Insufficent funds.")
                    account.change_balance(- amount)
                    return print("Withdraw succeeded.")
            print(f"Account {account_number} could not be found.")
        else:
            return print("User not online.")
        
      
    def save_customer(self):
        file = open("bank.json", "w")
        for customer in self.customer_list:
            self.bank_dictionary_list.append(customer.make_dictionary_customer())
        json_string = json.dumps(self.bank_dictionary_list, indent = 2)
        file.write(json_string)
        file.close()
        self.customer_list.clear()
        self.bank_dictionary_list.clear()
        
    def load_customer(self):
        self.customer_list.clear()
        with open("bank.json", "r") as file:
            dictionary = json.load(file)
        for customer_dictionary in dictionary:
            customer = Customer(customer_dictionary["username"], customer_dictionary["password"])
            self.customer_list.append(customer)
            for account_dictionary in customer_dictionary["account_list"]:
                account = Account(account_dictionary["account_number"], account_dictionary["balance"])
                customer.account_list.append(account)
        for customer in self.customer_list:
            print(f"Customer: {customer.username}, Password: {customer.password}")
            for account in customer.account_list:
                print(f"Account: {account.account_number}, Balance: {account.balance}")
        file.close()      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

