from math import *


# test if int or float not string.
def testzahl(zahl):
    try:
        a = 1212 + float(zahl)
        return True
    except:
        print("please only type end or a number")
        return False


# test & puts values in lists. deleted not used chars from input.
def inputdeguF(instr, listadd):
    x = input(instr)
    if "N" in x:
        x = x.split("N")[0]
    if "°" in x:
        x = x.split("°")[0]
    if "end" in x:
        return "end"
    elif testzahl(x):
        listadd.append(float(x))
    else:
        return inputdeguF(instr, listadd)


Force = []
degre = []
Forcex = []
Forcey = []
i = 0
Frx = 0
Fry = 0
print("decomposition of forces\nplease add the necessary forces(F) and angles(° counted from the positive y axis to the right)\nTo get your end result type end")
# main loop for the input.
while (1 == 1):
    end = inputdeguF("F" + str(i + 1) + " = ", Force)
    if end == "end":
        break
    end = inputdeguF("D°" + str(i + 1) + " = ", degre)
    if end == "end":
        break
    Forcex.append(Force[i] * cos(degre[i] * (pi / 180)))
    Forcey.append(Force[i] * sin(degre[i] * (pi / 180)))
    print("F" + str(i+1) + "x = " + str(Forcex[i]) + "N")
    print("F" + str(i+1) + "y = " + str(Forcey[i]) + "N")
    i += 1
# calculation of frx/fry and end
i = 0
while i < len(Forcex):
    Frx += Forcex[i]
    i += 1
print("Frx = " + str(Frx))
i = 0
while i < len(Forcey):
    Fry += Forcey[i]
    i += 1
print("Fry = " + str(Fry))
