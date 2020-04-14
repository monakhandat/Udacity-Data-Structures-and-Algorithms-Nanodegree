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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

new_list=[]
new_list_calls = []
new_list_texts = []


for i in range(0,len(calls)):
    if calls[i][0] not in new_list:
        new_list.append(calls[i][0])
    if calls[i][1] not in new_list_calls:
        new_list_calls.append(calls[i][1])
for i in range(0,len(texts)):
    if texts[i][0] not in new_list_texts:
        new_list_texts.append(texts[i][0])
    if texts[i][1] not in new_list_texts:
        new_list_texts.append(texts[i][1])

output_list=[]
for i in range(0,len(new_list)):
    if new_list[i] not in new_list_calls and new_list[i] not in new_list_texts:
        output_list.append(new_list[i])
output_list.sort()
print("These numbers could be telemarketers: ")
print(*output_list,sep="\n")

