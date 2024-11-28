
from datetime import datetime
import statistics


class  AlmExperimento:
    def __init__(self,nombre,fecha,tipoExperimento,resultadosExperimento):
        self.nombre = nombre
        self.fecha = fecha
        self.tipoExperimento = tipoExperimento
        self.resultadosExperimento = resultadosExperimento

def agregarExperimento(Experimentos):

    nombre = input('ingrese un nombre para el experimento ')
    fecha_str = input('ingrese la fecha de realizacion "DD/MM/AAAA" ')
    try:
        fecha = datetime.strptime(fecha_str,"%d/%m/%Y")
    except ValueError:
        print('**** Fecha no valida **** ')
        return
        
    tipoExperimento = input('ingrese el tipo de experimento (Quimica-Biologia-Fisica) ')
    resultadosExperimento_str = input('cual fue el resultado del experimento Ejem:(24,48,56)')
    try:
        resultadosExperimento = list(map(float,resultadosExperimento_str.split(',')))
    except ValueError:
        print('**** Formato de Resultado de Experimento Invalido **** ')
        return
    


    # se crea objeto para agregar a la lista de experimentos
    experimentos = AlmExperimento(nombre,fecha,tipoExperimento,resultadosExperimento)

    Experimentos.append(experimentos)
    print(' ----- el experimento se agrego exitosamente ---- ')

    

def visualizarExperimento(Experimentos):
    if not Experimentos:
        print('Lista de Experimentos Vacia')
        return
    for i,  experimentos in enumerate(Experimentos,start=1):
        print('\n **** Experimentos ****')
        print(f'Nombre: { experimentos.nombre}')
        print(f'Fecha: { experimentos.fecha.strftime("%d/%m/%Y")}')
        print(f'Tipo de Experimento: { experimentos.tipoExperimento}')
        print(f'Resultados: { experimentos.resultadosExperimento}')

def compararExperimento(Experimentos):
    visualizarExperimento(Experimentos)
    if not Experimentos:
        print('Lista de Experimentos Vacía')
        return
    
    # Solicitar los nombres de los experimentos a comparar
    nombresComparar = input(
        'De los experimentos almacenados,\n'
        'digite el nombre de los que desea comparar (separados por comas): Ejemplo: Quimica,Fisica: '
    ).lower()
    nombresComparar = [nombre.strip() for nombre in nombresComparar.split(",")]

    compararResultados = []

    for nombreActual in nombresComparar:
        # Buscar el experimento por nombre
        encontrado = next((exp for exp in Experimentos if exp.nombre.lower() == nombreActual), None)
        if encontrado:
            # Calcular el promedio de resultados del experimento
            promedio = sum(encontrado.resultadosExperimento) / len(encontrado.resultadosExperimento) if encontrado.resultadosExperimento else 0
            compararResultados.append((encontrado.nombre, promedio))
        else:
            print(f'Nombre "{nombreActual}" no existe')

    # Ordenar los resultados por promedio
    compararResultados.sort(key=lambda x: x[1], reverse=True)

    # Mostrar los resultados comparados
    print('Resultados comparados:')
    for i, (nombre, promedio) in enumerate(compararResultados, start=1):
        print(f'{i}. {nombre} - Promedio: {promedio:.2f}')


    
# funcion para analizar resultados 

def calcularExperimento(Experimentos):
    if not Experimentos:
        print('Lista de Experimentos Vacia')
        return
    for experimentos in Experimentos:
        promedio = statistics.mean(experimentos.resultadosExperimento)
        maximo = max(experimentos.resultadosExperimento)
        minimo = min(experimentos.resultadosExperimento)
        print(f'\n **** Analisis de Experimentos **** {experimentos.nombre}')
        print(f'Promedio de los valores obtenidos: {promedio}')
        print(f'Valor maximo: {maximo}')
        print(f'Valor minimo: {minimo}')

 




    
  

    

def generarInforme(Experimentos):
    if not Experimentos:
        print('Lista de Experimentos Vacia')
        return
# se abre un archivo txt para escribir el informe
    with open("informe_experimentos.txt","w") as archivo:
    # escribimos los detalles a relacionar en el archivo 
        for experimentos in Experimentos:
            archivo.write(f'Nombre: {experimentos.nombre}\n')
            archivo.write(f'Fecha: {experimentos.fecha}\n')
            archivo.write(f'Tipo: {experimentos.tipoExperimento}\n')
            archivo.write(f'Resultados: {experimentos.resultadosExperimento}\n')
            archivo.write('\n')
    print('informe generado como: "informe_experimentos.txt" ')
        


    pass

def menu():
    Experimentos=[]

    while True:
        print('\n SELECIONA LO QUE DESEAS HACER ')
        print('\n 1. AGREGAR EXPERIMENTO ')
        print('\n 2. VISUALIZAR EXPERIMENTO ')
        print('\n 3. CALCULAR EXPERIMENTO ')
        print('\n 4. COMPARAR EXPERIMENTO ')
        print('\n 5. GENERAR INFORME ')
        print('\n 6. SALIR ')
      

        opcion = input('\n SELECCIONE UNA OPCION  ')

        if opcion == '1':
            agregarExperimento(Experimentos)
        elif opcion == '2':
            visualizarExperimento(Experimentos)
        elif opcion == '3':
            calcularExperimento(Experimentos)
        elif opcion == '4':
            compararExperimento(Experimentos)
        elif opcion == '5':
            generarInforme(Experimentos)
        
        elif opcion == '6':
            print (' Gracias por utilizar nuestro programa , !hasta pronto¡')
            break
        else:
            print(' opcion invalida ')
if __name__=="__main__":

    menu()
