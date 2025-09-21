import csv

# Define a class for the customer
class Customer:
    def __init__(self, id, first_name, last_name, password, checking="False", savings="False", active="True", overdraft_count="0"):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = checking
        self.savings = savings
        self.active = active
        self.overdraft_count = overdraft_count

    # Return customer info as a list (row) to save in the csv file
    def to_list(self):
        return [
            self.id,
            self.first_name,
            self.last_name,
            self.password,
            self.checking,
            self.savings,
            self.active,
            self.overdraft_count
        ]

