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
n_texts = len(texts)
n_calls = len(calls)

new_set = set(())
for i in range(0, n_texts):
    new_set.add(texts[i][0])
    new_set.add(texts[i][1])
    
for i in range(0,n_calls):
    new_set.add(calls[i][0])
    new_set.add(calls[i][1])

print("There are ",len(new_set)," different telephone numbers in the records.")