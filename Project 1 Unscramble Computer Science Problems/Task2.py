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

new_dict = {}
for i in range(0,len(calls)):
    if calls[i][0] not in new_dict:
        new_dict.update({calls[i][0]:int(calls[i][3])})
    else:
        new_dict[calls[i][0]] += int(calls[i][3]) 
    if calls[i][1] not in new_dict:
        new_dict.update({calls[i][1]:int(calls[i][3])})
    else:
        new_dict[calls[i][1]] += int(calls[i][3])
        
max_time = 0
for phone_number in new_dict:
    if max_time < new_dict[phone_number]:
        max_time = new_dict[phone_number]
        max_time_number = phone_number

print(max_time_number,"spent the longest time ", max_time," seconds, on the phone during September 2016.")