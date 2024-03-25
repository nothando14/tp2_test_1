import pandas as pd

def update_voter_into():
    #Dictionares
    info = {"voter_id":"name", "voting_district":"has_voted"}   
    
    while True:
        vote = input("Enter voter's info: ")

        if vote==info:
            print("Already voted.")

        else:
            ("Enter the voter,s info: ")
            update_voter_into()
