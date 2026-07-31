"""temp"""

def tempa(old, newone, t):
    """smt"""
    if old == "C"and newone == "K":
        t = t +273.15
    elif old == "C"and newone == "F":
        t = t*9/5+32
    elif old == "C"and newone == "R":
        t = (t+273.15) * 9/5
    elif old == "K"and newone == "C":
        t = t - 273.15
    elif old == "F"and newone == "C":
        t = (t-32)*5/9
    elif old == "R"and newone == "C":
        t = (t*5/9) - 273.15
    return t



temp =float(input())
og = input()
new = input()
if "C" not in (og,new):
    temp = tempa(og,"C",temp)
    temp = tempa("C",new,temp)
    print(f"{temp:.2f}")

else:
    temp =tempa(og,new,temp)
    print(f"{temp:.2f}")
