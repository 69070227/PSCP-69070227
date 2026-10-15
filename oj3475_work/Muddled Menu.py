"""Muddled Menu"""

menu = []

while True:
    inp = input()

    if inp == "DONE":
        break
    if inp == "SOMETHING'S WRONG":
        menu.clear()
    elif inp == "CLOSED":
        menu.clear()
        break
    elif inp.startswith("Can't do: "):
        item = inp[10:]
        if item in menu:
            menu.remove(item)
    else:
        #N ให้ต่อท้ายสุดของเมนูในขณะนั้น
        name, num = inp.rsplit(" #", 1)
        if num == "N":
            menu.append(name)
        else:
            # insert(ตำแหน่ง, ของ)
            menu.insert(int(num) - 1, name)

print(f"Full Course: {menu} Reversed: {menu[::-1]}")
