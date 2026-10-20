"""Filter"""
import json

data = json.loads(input())
filterr = float(input())
found = False
for studentID in sorted(data):
    #วัดคะแนน
    if data[studentID] >= filterr:
        print(f"{studentID}\t{data[studentID]:.2f}")
        found = True
if not found:
    print("Nope")
