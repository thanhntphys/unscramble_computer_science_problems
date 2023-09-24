"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_telephone_number = []
calls_dict = {}
for call in calls:
    if call[0] not in calls_dict:
        calls_dict[call[0]] = int(call[3])
    else:
        calls_dict[call[0]] += int(call[3])

    if call[1] not in calls_dict:
        calls_dict[call[1]] = int(call[3])
    else:
        calls_dict[call[1]] += int(call[3])
max_time = max(calls_dict.values())
phone_max = (list(calls_dict.keys())[list(calls_dict.values()).index(max_time)])
print(f"{phone_max} spent the longest time, {max_time} seconds, on the phone during September 2016.")