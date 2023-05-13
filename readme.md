- [Capitulos](#capitulos)
  - [calcular\_dias()](#calcular_dias)
    - [Calculo](#calculo)
# Capitulos
Para calcular los capitulos que faltan seguiremos una sencilla [función](#calcular_dias).
El programa deberá mostrarnos una vez finalizado algo como esto:

```bash
Hola, introduce la cantidad de capitulos que tiene tu serie actualmente: 1000
Cada cuantos dias sale tu episodio: 7
Cuantos capitulos ves al dia: 2
Hoy es 13-05-2023 terminaras de verlo el 01-11-2024 Tardaras 538 dias en terminar de verlo.
```

## calcular_dias()
Esta función devuelve los dias que te faltan por ver una serie y le tienes que pasar los siguiente parámetros.
- `capitulos_acutales`: Capitulos totales que tiene el anime hasta el momento.
- `periodo_de_salida`:  Tiempo en dias en que tarda en salir un epidodio.
- `vistos_dia`: Cuantos capitulos ves cada día


### Calculo
El calculo que realiza es el siguiente.
Siendo: 
- Capitulos totales: `Ct`
- Tiempo que tarda en salir cada capitulo: `Ttc`
- Cuantos capitulos se ve cada día: `Cd`
- Dias totales que faltan para ver toda la seria: `D`

$$
D = \frac{Ct}{Ttc - \frac{1}{Cd}}
$$
