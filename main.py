
from datetime import datetime

Experimentos = []

def agregarExperimento(experimento):
    nombre = input('ingrese un nombre para el experimento ')
    Experimentos.append(nombre)
    fecha = input('ingrese la fecha de realizacion "DD/MM/AAAA" ')
    Experimentos.append(fecha)
    tipoExperimento = input('ingrese el tipo de experimento (Quimica-Biologia-Fisica) ')
    Experimentos.append(tipoExperimento)
    resultadosEsperimento = input('cual fue el resultado del experimento Ejem:(24,48,56)')
    Experimentos.append(resultadosEsperimento)
    

def visualizarExperimento():
    pass

def calcularExperimento():
    pass

def compararExperimento():
    pass

def generarInforme():
    pass

def generarTxt():
    pass


def menu():
    

    while True:
        print('\n SELECIONA LO QUE DESEAS HACER ')
        print('\n 1. AGREGAR EXPERIMENTO ')
        print('\n 2. VISUALIZAR EXPERIMENTO ')
        print('\n 3. CALCULAR EXPERIMENTO ')
        print('\n 4. COMPARAR EXPERIMENTO ')
        print('\n 5. GENERAR INFORME EN PANTALLA ')
        print('\n 6. DESCARGAR INFORME ')
        print('\n 7. SALIR  ')

        opcion = input('SELECCIONE UNA OPCION  ')

        if opcion == '1':
            agregarExperimento(Experimentos)
        elif opcion == '2':
            visualizarExperimento()
        elif opcion == '3':
            calcularExperimento()
        elif opcion == '4':
            compararExperimento()
        elif opcion == '5':
            generarInforme()
        elif opcion == '6':
            generarTxt()
        elif opcion == '7':
            print (' Gracias por utilizar nuestro programa , !hasta pronto¡')
            break
        else:
            print(' opcion invalida ')

menu()