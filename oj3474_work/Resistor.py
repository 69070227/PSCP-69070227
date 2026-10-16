"""helppppppppppp"""
colors = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
    "Yellow": 4, "Green": 5, "Blue": 6, "Purple": 7,
    "Grey": 8, "White": 9
}

multiplier = {
    "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000,
    "Yellow": 10000, "Green": 100000, "Blue": 1000000,
    "Purple": 10000000, "Gold": 0.1, "Silver": 0.01
}

tolerance = {
    "Brown": 0.01, "Red": 0.02, "Green": 0.005,
    "Blue": 0.0025, "Purple": 0.001, "Grey": 0.0005,
    "Gold": 0.05, "Silver": 0.10
}

c1 = input()
c2 = input()
c3 = input()
c4 = input()

if c1 not in colors or c2 not in colors or c3 not in multiplier or c4 not in tolerance:
    print("Error")
else:
    value = (colors[c1] * 10 + colors[c2]) * multiplier[c3]
    lower = value * (1 - tolerance[c4])
    upper = value * (1 + tolerance[c4])

    print(f"{lower:.4f}")
    print(f"{upper:.4f}")
