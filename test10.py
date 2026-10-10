"""test"""

word = input()
new = word.lower()
found_b = False
current_u = 0
max_u = 0
for i in new:
    if i == "b":
        found_b = True
        current_u = 0
    elif i == "u":
        if found_b is True:
            current_u += 1
            if current_u >= 2:
                max_u = max(max_u, current_u)
        else:
            current_u = 0
if max_u >= 2:
    print(f"Yes {max_u}")
else:
    find_b  = new.find("b")
    len_u = len(new) - find_b - 1
    result = word[:find_b + 1]
    if found_b is True:
        print(f"{result}{'U' * len_u}")
    else:
        print(("BUU" * len(word))[:len(word)])
