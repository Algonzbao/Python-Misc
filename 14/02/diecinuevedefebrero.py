
def numerosYsuma(x, y, op):
    if(op == "suma"):
        resultado = x + y
    if (op == "resta"):
        resultado = x - y
    if (op == "multiplicacion"):
        resultado = x * y
    if (op == "division"):
        try:
            x/y
        except ZeroDivisionError:
            print("No se puede hacer esa division")
            return(print("Operacion Erronea"))

        resultado = x % y
    return resultado
print("Introduce los 2 valores que quieres operar")
x = float(input())
try:
    x == " "
except ValueError:
    print("El valore debe ser numerico")
y = float(input())
try:
    y == " "
except ValueError:
    print("El valore debe ser numerico")

print("Ahora di que tipo de operacion quieres hacer")
print("suma/resta/multiplicacion/division")
op = input()
print(numerosYsuma(x,y,op))