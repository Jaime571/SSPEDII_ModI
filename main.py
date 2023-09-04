from polarData import polarData, toPolarData
from decimal import Decimal
import os

flag = 0

firstMagnitude = float(input('Ingrese la magnitud del primer vector: '))
secondMagnitude = float(input('Ingrese la magnitud del segundo vector: '))

while flag == 0:
    firstDir = float(input('Ingrese la direccion en grados del primer vector: '))
    secondDir = float(input('Ingrese la direccion en grados del segundo vector: '))
    if((firstDir >= -180 and firstDir <= 180) and (secondDir >= -180 and secondDir <=180)):
        flag = 1
    else:
        os.system('cls')
        print('Los valores de angulo solo se pueden leer dentro de este rango -180 <= x° <= 180')

firstVector = polarData(firstMagnitude, firstDir)
secondVector = polarData(secondMagnitude, secondDir)

firstRectangularData = firstVector.toRectangularData()
secondRectangularData = secondVector.toRectangularData()

result = {
    'x': firstRectangularData[0] + secondRectangularData[0],
    'y': firstRectangularData[1] + secondRectangularData[1]
}

polar = toPolarData(result)

print('La magnitud resultante es de: ' + str(round(polar[0], 2)) + '\nLa direccion resultante es de: ' + str(round(polar[1], 2)) + '°')