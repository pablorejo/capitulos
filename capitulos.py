import math # Para redondear a la baja

from datetime import datetime,timedelta

def calcular_dias(capitulos_acutales,periodo_de_salida,vistos_dia):
    return math.floor( capitulos_acutales/ (vistos_dia - (1/periodo_de_salida) ))

if __name__ == '__main__':
    capitulos_acutales = int(input("Hola, introduce la cantidad de capitulos que tiene tu serie actualmente: "))
    periodo_de_salida = int(input("Cada cuantos dias sale tu episodio: "))
    vistos_dia = int(input("Cuantos capitulos ves al dia: "))
    dias = calcular_dias(capitulos_acutales,periodo_de_salida,vistos_dia)
    fecha_inicio = datetime.now()
    format_inicio = fecha_inicio.strftime('%d-%m-%Y')

    fecha_fin = fecha_inicio + timedelta(days=dias)
    format_fin = fecha_fin.strftime('%d-%m-%Y')

    print("Hoy es " + format_inicio + " terminaras de verlo el " + format_fin + " Tardaras " + str(dias) + " dias en terminar de verlo." )
        
