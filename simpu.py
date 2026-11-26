import sys

if len(sys.argv) == 4:
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)