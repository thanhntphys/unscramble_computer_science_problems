"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extract_area_code(calls):
    blr_dialed_areas = set()
    for call in calls:
        if re.search(r'\(\w+\)', call):
            area_code = call.split(sep=')')[0] + ')'
            blr_dialed_areas.add(area_code)
        elif re.search(r'(^[7|8|9])', call):
            area_code = call[:4]
            blr_dialed_areas.add(area_code)
        elif re.search(r'^140', call):
            area_code = call[:3]
            blr_dialed_areas.add(area_code)
    return blr_dialed_areas


if __name__ == '__main__':
    ###################### Part A ######################

    bangalore_call = [call for call in calls if call[0].startswith('(080)')]
    bangalore_dialed = [call[1] for call in bangalore_call]
    blr_dialed_areas = extract_area_code(bangalore_dialed)
    print("The numbers called by people in Bangalore have codes:")
    for blr_dialed_area in sorted(list(blr_dialed_areas)):
        print(blr_dialed_area)

    ###################### Part B ######################
    blr_dialed_blr = [call for call in bangalore_dialed if call.startswith('(080)')]
    percentage = round((len(blr_dialed_blr) / len(bangalore_dialed) * 100), 2)  # O(1)

    print('%s percent of calls from fixed lines in Bangalore are calls '
          'to other fixed lines in Bangalore.' % percentage)
