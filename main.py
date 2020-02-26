import os

with os.scandir('./tests') as entries:
    for entry in entries:
        with open(entry, 'r') as file:
            data = file.readlines()
            print(data[0])


