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
