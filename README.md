## Python Testing

Este repositorio está diseñado para ser usado en conjunto con el taller de testing en python de open webinars, no obstante sientete libre
de utilizarlo si ves que puede servirte de de ayuda.

Se compone de dos proyectos principales:
- calculadora: Este proyecto es una calculadora, que transforma operaciones matemáticas sencillas de forma escrita, a operaciones matemáticas.
- jokes: Este proyecto sirve para pasarte un buen rato, ataca a una API Rest de bromas, y recupera las bromas que tú quieras cuanod te haga falta.

Para probar cualquiera de las aplicaciones solo tienes:

```bash
python -m calculadora.main add 1 1
python -m jokes.main
```

Para ver algunas de sus opciones o como funcionan añade el parámetro -h.

Todos los tests están en la carpeta tests de las aplicaciones, para correrlos solo tienes que:

```bash
python -m unittest
```