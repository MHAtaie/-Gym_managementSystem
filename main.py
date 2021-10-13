#In the Name of God
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import time
names = []
date = []
month = []
mostPay = []
print("\033[92m {}\033[00m" .format("Ruz ro vared kon:"))
today_date = int(input())
print("\033[92m {}\033[00m" .format("Mah ro vered kon:"))
today_month = int(input())
print("\033[94m {}\033[00m" .format("************************************************"))
print("List bedehkaran:")
with open('list.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        names.append(row[0])
        date.append(row[2])
        mostPay.append(row[3])
        month.append(row[4])
    total = len(date)
    for i in range(1,total):
        if int(mostPay[i]) < 160:
            bedehi = 160 - int(mostPay[i]) 
            print("\033[93m {}\033[00m" .format(names[i] + "  meghdar bedhi:  " + str(bedehi)))
    print("\033[94m {}\033[00m" .format("************************************************"))
    print("Kasanike mohlateshun tamum shode:")
    for j in range(1,total):
        expiration_month = 1 + int(month[j])
        if int(date[j]) <= today_date and today_month == expiration_month:
            print("\033[91m {}\033[00m" .format(names[j]))
    print("\033[94m {}\033[00m" .format("************************************************"))
input("Press enter to close program")
# expiration_date = 31-date
# expiration_month = 1 + month
# if expiration date < today_date && ex_month <= today_month
#   print(name)

