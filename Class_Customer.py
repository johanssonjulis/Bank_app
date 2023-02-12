#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from Class_Account import *

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_list = []
        self.account_number = 1
        
    def make_dictionary_customer(self):
        dictionary = {}
        dictionary["username"] = self.username
        dictionary["password"] = self.password
        dictionary["account_list"] = []
        for account in self.account_list:
            dictionary["account_list"].append(account.make_dictionary_account())
        return dictionary
        
    def print_info(self):
        print(self.username, self.account_list)
        
    def check_password(self, password):
        if self.password == password:
            print("Right password.")
            return True
        print("Incorrect password.")
        return False
        
    def add_account(self, balance): #ska lägga till accounts till min privata lista
        self.account_number += 1
        self.account_list.append(Account(self.account_number, balance))
        print("Account added.")
        
    def __str__(self):
        return f"{self.username}, {self.password}"
    
    def __repr__(self):
        return f"username: {self.username}, password: {self.password}"

