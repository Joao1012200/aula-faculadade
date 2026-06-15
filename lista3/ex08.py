a = float(input("digite o lado A: "))
b = float(input("digite o lado B: "))
c = float(input("digite o lado C: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Os lados formam um triangulo equilatero")
    elif a == b or a == c or b == c:
        print("Os lados formam um triangulo isosceles")
    elif a != b and a != c and b != c:
        print("Os lados formam um triangulo escaleno")
else:
    print("Os lados não formam um triangulo")