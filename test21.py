"""test"""
import json

inp = json.loads(input())
filter = int(input())

box = {}
for key in sorted(inp):
    if key > filter:
        box = inp[key]