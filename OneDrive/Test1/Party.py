import pandas as pd

#Create a function that take list of parties
def register_party():
    party = {"party_name":[], "reg_number":[], "member_count":[]}

#Check if the nes party has accepted number od members
    if members<1000:
        members = input("Enter the number of members: ") 
        party["member_count"].append(members)

#How function will be executed
    party_name = ["MK"]
    member_count = [5300]
    myCount = [x for x in member_count if x+1]
    print(myCount)

    df = pd.DataFrame(party)
    print(df)

    
    






            