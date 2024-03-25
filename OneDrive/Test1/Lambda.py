import pandas as pd

#Lambda function
found = []
extract = lambda x,y : x if x == found else y
registered_voters =[]
foundVoter = list(filter(lambda x:x==found, registered_voters))
print(registered_voters)

