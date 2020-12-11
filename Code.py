import sys
import math

print( "\033[35m Kapitonova Daria IU5-54B")

def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def printRoots(roots):
    if len(roots) > 0:
        print(" Корни уравнения: {}".format(roots))
    else:
        print("     Уравнение не имеет корней:(")

coefficients = {}

# ввод коэф-ов
if (len(sys.argv) > 1):
    for i in range(3):
        try:
            coefficients.update({ chr(65+i): float(sys.argv[i+1])})
        except IndexError:
            coefficients.update({ chr(65+i): 0})
        except ValueError:
            coefficients.update({ chr(65+i): 0})
else:
   for i in range(3):
        userArg = input(" Пожалуйста, введите аргумент {}: ".format(chr(65+i)))
        while not isNumber(userArg):
            userArg = input("Введите аргумент повторно {}: ".format(chr(65+i)))
        coefficients.update({ chr(65+i): float(userArg)})

#решение уравнения
roots = []
discriminant = coefficients.get('B') ** 2 - 4 * coefficients.get('A') * coefficients.get('C')

if coefficients.get('A') == 0 and coefficients.get('B') == 0 and coefficients.get('C') == 0:
    print("Уравнение имеет бесконечное количество корней0")
elif coefficients.get('A') == 0 and coefficients.get('B') == 0:
    printRoots(roots)
elif coefficients.get('A') == 0:
    squareRoots = -coefficients.get('C') / coefficients.get('B')
    if squareRoots >= 0:
        roots.append(math.sqrt(squareRoots))
        if squareRoots != 0:
            roots.append(-math.sqrt(squareRoots))
    printRoots(roots)
else:
    if discriminant >= 0:
        squareRoots = (-coefficients.get('B') - math.sqrt(discriminant)) / (2 * coefficients.get('A'))
        if squareRoots >= 0:
            roots.append(math.sqrt(squareRoots))
            if squareRoots != 0:
                roots.append(-math.sqrt(squareRoots))
        if discriminant != 0:
            squareRoots = (-coefficients.get('B') + math.sqrt(discriminant)) / (2 * coefficients.get('A'))
            if squareRoots >= 0:
                roots.append(math.sqrt(squareRoots))
                if squareRoots != 0:
                    roots.append(-math.sqrt(squareRoots))
    printRoots(roots)

