"""Pad Thai"""

recipe = ("Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
          "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts")
taste = ("Sweet", "Sour", "Salty")

ingre = []
while True:
    inp_in = input().strip()
    if inp_in == "Cook":
        break
    ingre.append(inp_in)

flavor = []
while True:
    inp_fla = input().strip()
    if inp_fla == "End":
        break
    flavor.append(inp_fla)

outsider_stuff = False
for thing in ingre:
    if thing not in recipe:
        outsider_stuff = True

outsider_flavor = False
for fla in flavor:
    if fla not in taste:
        outsider_flavor = True

complete_recipe = True
for item in recipe:
    if item not in ingre:
        complete_recipe = False

complete_flavor = True
for t in taste:
    if t not in flavor:
        complete_flavor = False

if outsider_stuff:
    print("This is not Pad Thai!!!")
elif not complete_recipe:
    print("This is bad!")
elif complete_flavor and not outsider_flavor:
    print("Delicious!")
else:
    print("Not Bad...")