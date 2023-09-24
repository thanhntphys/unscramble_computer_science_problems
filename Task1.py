"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_number = []
for item in texts:
    telephone_number.append(item[0])
    telephone_number.append(item[1])
for item in calls:
    telephone_number.append(item[0])
    telephone_number.append(item[1])
diff_num = len(set(telephone_number))
print(f"There are {diff_num} different telephone numbers in the records.")
