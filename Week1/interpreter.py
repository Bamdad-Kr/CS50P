x, y, z = input("Enter your Expression: ").strip().split(" ")
if y == '+':
    a = float(x) + float(z)
elif y == '-':
    a = float(x) - float(z)
elif y == "*":
    a = float(x) * float(z)
elif y == "/":
    a = float(x) / float(z)
print(f"{a:.1f}")
