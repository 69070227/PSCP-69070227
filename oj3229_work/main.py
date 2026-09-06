"""test"""

mainquest = int(input())
bonus = int(input())
daysplayed = int(input())
RAHAS = ""
RAHAS_SPECIAL = ""
multi = 1
if daysplayed > 3:
    multi = 1.5

total = int((mainquest + bonus) * multi)

if total >= 1500:
    RAHAS = "5"
    if daysplayed >= 7:
        RAHAS_SPECIAL ="99"
    else:
        RAHAS_SPECIAL = "0"

elif total >= 1000:
    RAHAS = "4"
    if bonus > 300:
        RAHAS_SPECIAL = "88"
    else:
        RAHAS_SPECIAL = "0"

elif total >= 500:
    RAHAS = "3"
    RAHAS_SPECIAL = "0"
elif total >= 200:
    RAHAS = "2"
    RAHAS_SPECIAL = "0"
elif total < 200:
    RAHAS = "1"
    RAHAS_SPECIAL = "0"


print(total)
print(RAHAS)
print(RAHAS_SPECIAL)
