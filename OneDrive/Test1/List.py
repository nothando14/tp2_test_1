import pandas as pd

#list comprehension
parties = ['ASC', 'ATM', 'ASSD', 'ANC', 'AGANG SA', 'ALJAMA', 'ATA', 'AZOPO', 'APC', 'BRA','BLF', 'ZACP','CPM','CSA','COPE', 'DA', 'DLC','ECOFORUM', 'EFF','F4SD','FREE DEMS']
less = filter([x for x in parties if x<1000])
print(less)

#Normal list
parties1 = ['ASC', 'ATM', 'ASSD', 'ANC', 'AGANG SA', 'ALJAMA', 'ATA', 'AZOPO', 'APC', 'BRA','BLF', 'ZACP','CPM','CSA','COPE', 'DA', 'DLC','ECOFORUM', 'EFF','F4SD','FREE DEMS']
less1 = []
for x in parties1:
    if filter((x<1000)):
        less1.append(x)
print(less1)

