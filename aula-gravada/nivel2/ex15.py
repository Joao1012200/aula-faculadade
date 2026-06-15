a = float(input("digite o lado A: "))
b = float(input("digite o lado B: "))
c = float(input("digite o lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Os lados formam um triangulo")
else:
    print("Os lados não formam um triangulo")