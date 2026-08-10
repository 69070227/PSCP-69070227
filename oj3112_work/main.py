"""ชานมไข่มุก"""

def function_kaimook(type_kaimook,amount_kaimook):
    """KAIMOOOOKK"""
    CAL = 0
    if type_kaimook == "H":
        CAL = 5 * amount_kaimook

    elif type_kaimook == "O":
        CAL = 3 * amount_kaimook

    elif type_kaimook == "J":
        CAL = 2 * amount_kaimook
    return CAL

def functioncha(type_cha,sweet,amount_cha):
    """CHAAAAAAAAAAAAA"""
    #ปริมาณคูณความหวาน
    SOLU_CHA = 0
    if type_cha == "R":
        if sweet =="1":
            SOLU_CHA = 12 * amount_cha
        elif sweet =="2":
            SOLU_CHA = 18 * amount_cha
        elif sweet =="3":
            SOLU_CHA = 25 * amount_cha

    elif type_cha == "T":
        if sweet =="1":
            SOLU_CHA = 15 * amount_cha
        elif sweet =="2":
            SOLU_CHA = 20 * amount_cha
        elif sweet =="3":
            SOLU_CHA = 30 * amount_cha

    elif type_cha == "M":
        if sweet =="1":
            SOLU_CHA = 10 * amount_cha
        elif sweet =="2":
            SOLU_CHA = 15 * amount_cha
        elif sweet =="3":
            SOLU_CHA = 20 * amount_cha
    return SOLU_CHA

in_kai, inamount_K = input().upper().split()
inamount_K = float(inamount_K)

in_cha, in_sweet, inamount_C = input().upper().split()
inamount_C = float(inamount_C)

result_kai = function_kaimook(in_kai,inamount_K)
result_cha = functioncha(in_cha,in_sweet,inamount_C)

total = result_kai + result_cha
print(f"{total:g}")
