"""reseeeee"""

days = int(input())
months = int(input())

change_days = [
 20, #เดือน1
 19, #เดือน2
 21, #เดือน3
 20, #เดือน4
 21, #เดือน5
 22, #เดือน6
 23, #เดือน7
 23, #เดือน8
 23, #เดือน9
 24, #เดือน10
 22, #เดือน11
 22 #เดือน12
]

before = [
    "capricorn",
    "aquarius",
    "pisces",
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius"

]

after = [
    "aquarius",
    "pisces",
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn"
]
#ถ้าวันเปลี่ยนในตำแหน่งนี้มีค่า มากกว่า วันที่ใส่ไป
if change_days[months - 1] > days:
    #ถ้าใช่(คือวันมันยังไม่ถึงวันที่ต้องเปลี่ยน)แสดงว่ามันยังไม่เปลี่ยนราศี
    print(before[months - 1])
else:
    #ถ้าไม่ใช่(คือวันที่ผู้ใช้กรอก ถึงหรือเลยวันเปลี่ยนราศีแล้ว)เปลี่ยนจ้า
    print(after[months - 1])
