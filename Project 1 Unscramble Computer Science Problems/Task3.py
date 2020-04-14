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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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

bangalore_callers = []
calls_from_bangalore = []
for i in range(0,len(calls)):
    if calls[i][0][0] == '(' and calls[i][0][1] == '0' and calls[i][0][2] == '8' and calls[i][0][3] == '0' and calls[i][0][4] == ')':
            if calls[i][0] not in bangalore_callers:
                bangalore_callers.append(calls[i][0])
            if calls[i][1] not in calls_from_bangalore:
                calls_from_bangalore.append(calls[i][1])

                
area_code=[]
for i in range(0,len(calls_from_bangalore)):
    temp = ''
    if calls_from_bangalore[i][0] == '(':
        j = 1
        while(calls_from_bangalore[i][j] != ')'):
            temp+=calls_from_bangalore[i][j]
            j+=1
    elif calls_from_bangalore[i][0] == 1 and calls_from_bangalore[i][1] == 4 and calls_from_bangalore[i][2] == 0:
        temp = '140'
    else:
        j=0
        for j in range(0,4):
            temp+=calls_from_bangalore[i][j]
    if temp not in area_code:
        area_code.append(temp)
        
area_code.sort()

print("The numbers called by people in Bangalore have codes:")
print(*area_code,sep="\n")

no_bangalore_callers=0
no_calls_from_bangalore=0
for i in range(0,len(calls)):
    if calls[i][0][0] == '(' and calls[i][0][1] == '0' and calls[i][0][2] == '8' and calls[i][0][3] == '0' and calls[i][0][4] == ')':
            no_bangalore_callers+=1
            if calls[i][1][0] == '(' and calls[i][1][1] == '0' and calls[i][1][2] == '8' and calls[i][1][3] == '0' and calls[i][1][4] == ')':
                no_calls_from_bangalore+=1
percentage = round((no_calls_from_bangalore*100/no_bangalore_callers),2)
print(percentage," percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")