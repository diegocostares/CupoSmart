## **Problema**

La inscripción de ramos es un proceso complicado. Los estudiantes deben inscribir cursos en distintas etapas. Debido a que cada curso tiene un número variable de vacantes y de estudiantes interesados, es difícil determinar el orden óptimo para inscribirse en todos los ramos deseados. Por lo tanto, es necesario desarrollar una solución que proporcione el orden adecuado para la inscripción de los cursos o que minimice la probabilidad de perder un curso en las etapas siguientes.

## **Reglas de la Toma de Ramos**

- Se asume que un estudiante puede inscribir un máximo de 60 créditos.
- Un curso puede equivaler a 10 o 5 créditos. Generalmente, 50 créditos corresponden a 5 ramos.
- El proceso de inscripción de ramos se divide en 4 etapas.
- Cada etapa dura 2 días.
- La hora a la que los estudiantes toman ramos está dividida en 16 banners a lo largo de dos días que van desde las 8:00 a 19:50.
- La cantidad de personas en cada banner es la misma.
- Es posible retirar un ramo durante cada una de las etapas.
- A cada estudiante se le asigna un unico grupo o banner en el que tiene que tomar ramos.

### **Etapas de Inscripción:**

1. **Primera Etapa:**

   - Se pueden inscribir hasta 30 créditos.
   - No es posible inscribir más de una sección del mismo curso.

2. **Segunda Etapa:**

   - Se pueden inscribir 30 créditos adicionales, llegando a un total de 60 créditos o según lo que indique el plan de estudio.

3. **Primer Ajuste de Inscripción:**

   - Al finalizar la inscripción, las unidades académicas liberan las vacantes no ocupadas.

4. **Segundo Ajuste de Inscripción:**
   - Las unidades académicas liberan nuevamente las vacantes que no fueron ocupadas en la segunda etapa.

## **Grupos Banner**

Generalmente, por cada una de las 4 etapas, se tienen las siguientes distribuciones de grupos:
(Aunque en el primer ajuste de Inscripción se suele invertir los grupos. Lamentablemente no tenemos el dato exacto de cada banner y hay años que cambia.)

### **Día Uno - Primera Etapa:**

```
| Grupo | Horario       |
| ----- | ------------- |
| 1     | 8:00 - 9:20   |
| 2     | 9:30 - 10:50  |
| 3     | 11:00 - 12:20 |
| 4     | 12:30 - 13:50 |
| 5     | 14:00 - 15:20 |
| 6     | 15:30 - 16:50 |
| 7     | 17:00 - 18:20 |
| 8     | 18:30 - 19:50 |
```

### **Día Dos - Primera Etapa:**

```
| Grupo | Horario       |
| ----- | ------------- |
| 9     | 8:00 - 9:20   |
| 10    | 9:30 - 10:50  |
| 11    | 11:00 - 12:20 |
| 12    | 12:30 - 13:50 |
| 13    | 14:00 - 15:20 |
| 14    | 15:30 - 16:50 |
| 15    | 17:00 - 18:20 |
| 16    | 18:30 - 19:50 |
```

# Información que se posee

Mediante scraping del buscacursos se tienen las siguientes dos tablas con información de los ramos.

## Tabla de sections.csv

```
id,period,section,nrc,teachers,schedule,format,campus,is_english,is_removable,is_special,available_quota,total_quota,course_id,initials,name,credits,req,con,restr,school,area,category
6631,2019-2,1,19552,Patricio Rodriguez,"M:4,5<>CLAS<>SEM3<><>",Presencial,Oriente,f,t,f,5,9,30,ACT105C,"Experiencia Estética, Recepción y Teatralidad",10,No tiene,No tiene,No tiene,Actuación,,
6632,2019-2,1,20279,Ana Sedano,"W:2,3<>CLAS<>R-4<><>",Presencial,Oriente,f,t,f,1,5,31,ACT105D,Estudios Teatrales de la Vida Social,10,No tiene,No tiene,No tiene,Actuación,,Aprendizaje Servicio
```

## Tabla de quota.csv

```
id,date,category,quota,banner,section_id,initials
4335060,2021-01-30 20:04:55.907763+00,04 - Ingeniería,4.0,0,24405,IIQ3643
4335061,2021-01-30 20:04:56.148198+00,Vacantes libres,1.0,0,24406,IIQ3663
4335062,2021-01-30 20:04:56.148198+00,04 - Ingeniería,11.0,0,24406,IIQ3663
```

# Lluvia de ideas y proceso creativo

Para resolver el problema fuimos pensando varias ideas.

- **Regresión Polinomial**: Ajustar una regresión polinomial de segundo grado para modelar la relación entre la hora y la disponibilidad del curso. Luego, para cada curso, se calcula el valor de la función en cada uno de los banners y se ordenan los cursos según el valor de la función.
- **Predicción de Disponibilidad con IA**: Modelo que pueda predecir la disponibilidad de un curso en las próximas etapas basándose en datos históricos.

- **Algoritmo Greedy (Optimización con heurísticas)**: Elegir los cursos que tengan la mayor demanda o menor disponibilidad en las primeras etapas.

- **Simulación de pasos de tiempo**: Simular cada banner como un paso de tiempo y ver cómo cambia la disponibilidad de los cursos con cada paso.

- **Simular el comportamiento de los estudiantes**: Simular cómo los estudiantes eligen los cursos.

- **Solución basada en la teoría de juegos**: Utilizando la teoría de juegos y modelando a cada estudiante como un agente estratégico, habria que hacer un algoritmo que optimiza la inscripción en cursos universitarios al considerar las preferencias individuales, la demanda histórica de cursos y la disponibilidad en tiempo real, buscando alcanzar un equilibrio que minimice la probabilidad de perder un curso en la etapa siguiente. Usamos de referencia [The Parking Problem: A Game-Theoretic Solution](https://arxiv.org/abs/2204.01395).

- **Clustering con ML**: Usar algún modelo de Machine Learning (ML) para clusterisar cúmulos de cursos mas demandados y luego con nlp solo recomendar basado en clases

# Problemas durante el desarrollo

- Hay cursos que tienen distintas disponibilidades en distintas secciones y en distintos semestres. En un semestre puede tener 50 cupos y el siguiente solo 30. Eso podría afectar lo que tememos, Por el momento se ignoró este problema.

# Ideas que fueron surgiendo

- Calcular el porcentaje de cupos restantes en vez de la cantidad. Y luego hacer scrapping de la cantidad de cupos antes de la toma de ramos.

# Obtención de datos

Se buscaron datos de dos fuentes, la primera es de la pagina del profesor [Hernán Valdivieso](https://hernan4444.github.io/cupos-banner) y la segunda es de la base de datos que maneja [ramos-uc](https://github.com/open-source-uc/ramos-uc).

# Comentarios luego del desarrollo

No tomamos cursos en el reajuste (de momento). Solo tomamos en la primera y segunda toma

Solo tenemos 921 cursos registrados (Es facil agregar el resto, simplemente necesitamos hacer scrapping de los datos para entrenar el resto de los cursos)

De muestra, utilizamos ['IIC2133', 'IBM2101', 'IBM2992', 'EYP1025', 'IMT2565', 'FIS1514'] y banner 2. Lo que nos da un resultado de:
Primer día:
['IIC2133', 'IBM2101', 'FIS1514']
Segundo día:
['IBM2992', 'EYP1025', 'IMT2565']

To-Do:

- Utilizar un scaler global
- Utilizar un periodo de toma de ramos de 4 días en vez de 1 semana

## Modelo de Red Neuronal:

1. _Arquitectura:_

   - Tipo: Modelo Secuencial (Sequential) de TensorFlow Keras.
   - Capas:
     1. Capa Densa: 7 neuronas, activación ReLU, forma de entrada (1,).
     2. Capa Densa: 7 neuronas, activación ReLU.
     3. Capa Densa (Salida): 1 neurona, activación lineal.

2. _Compilación:_

   - Optimizador: Adam.
   - Función de Pérdida: Error Cuadrático Medio (Mean Squared Error, MSE).

3. _Early Stopping:_

   - Monitorización: Pérdida (loss) durante el entrenamiento.
   - Paciencia: 20 épocas.
   - Restauración de Mejores Pesos: Activada.

4. _Entrenamiento:_

   - Épocas: 1000.
   - Verbose: 0 (sin salida de entrenamiento).

5. _Datos:_
   - Entrada: `x_values_normalized`.
   - Salida: `y_values_normalized`.
