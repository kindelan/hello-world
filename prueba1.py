#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
    Programa: Prueba1
    Fecha   : 18/01/2017
    Prgramador: Ignacio Perez
    Descripción: Obtener el ciclista ganador de:
    - La vuelta completa
    - Una etapa concreta
    - De cada etapa 
"""

#defición de funciones
def ganador_vuelta(ciclista,tiempo,):
    """Devuelve el ganador de la vuelta a partir de la lista de ciclistas y la matriz de los tiempos
       Parametros: -Ciclista: Lista de ciclistas participantes
                   -Tiempo: Matriz de tiempos por ciclista y etapa 
       Retorno: Ciclista gnadar de la vuelta            
    """
    tiempos = []
    for i in range(0, len(tiempo)):
        suma = 0
        for j in range(0, len(tiempo[i])):
            suma = suma + tiempo[i][j]
        tiempos.append(suma)    
    minimo = None
    for i in range(0,len(tiempos)):
        if minimo is None or tiempos[i] < minimo:
            minimo = tiempos[i]
            quien = i 
    return ciclista[quien]

def ganador_etapa(ciclista, tiempo, etapa):
    """devuelve el ganador de la etapa indicada
       Parametros: -Ciclista: Lista de ciclistas participantes
                   -Tiempo: Matriz de tiempos por ciclista y etapa 
                   -Numero de etapa: - Numero de etapa de la que se quiere conocer el ganador
                   Sie el valor es None, devuelve el ganador de cada etapa en una lista
        Retorno: Ciclista ganador de la etapa           
    """
    minimo = None
    for i in range(0,len(tiempo)):
         if minimo is None or tiempo[i][etapa] < minimo:
            minimo = tiempo[i][etapa]
            quien = i 
    return ciclista[quien]
                    
def get_etapa():
    while True:
        num_etapa_a = raw_input("numero de etapa de la que quiere conocer el ganador")
        try:
            num_etapa = int(num_etapa_a)
        except:
            print"numero de etapa no valido"
            continue
        if num_etapa < 1 or num_etapa > 5:
            print"numero de etapa no valido"
            continue
        break
    return  num_etapa
       
#proceso principal del programa

#Lista de ciclistas y matriz de tiempos
ciclista = ['Pere_Porcar', 'Joan_Beltran', 'Lledó_Fabra']
tiempo = [[10092.0, 12473.1, 13732.3, 10232.1, 10332.3],
          [11726.2, 11161.2, 12272.1, 11292.0, 12534.0],
          [10193.4, 10292.1, 11712.9, 10133.4, 11632.0]]

while True:
    opcion_a = raw_input("opciones:\n 0-Fin programa\n 1-obtener ganador de la vuelta\n 2-obtener ganador de una etapa\n 3-obtener gnador de cada etapa")
    try: 
        opcion = int(opcion_a)
    except:
        print "Opcion no valida"
        continue
    if opcion == 0:
        break
    elif opcion == 1:
        print ganador_vuelta(ciclista,tiempo)
    elif opcion == 2:
        etapa = get_etapa()
        print ganador_etapa(ciclista,tiempo,etapa-1)
    elif opcion == 3:
        for i in range(0,5):
            print ganador_etapa(ciclista,tiempo,i)
        
    else:
         print"opcion introducida no valida"   
        
        