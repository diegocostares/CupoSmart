<h1 align="center">
  <img src="CupoSmart_logo.jpeg" width="150px">
  <br>
  <a href=# name="readme-top">CupoSmart</a>
</h1>

## Introducción

Este proyecto está diseñado para simplificar y optimizar el proceso de decidir el orden de inscripción de cursos en la Pontifica Universidad Católica de Chile. El proyecto consta de una API utilizando FastAPI que se encuentra en la carpeta `backend/`. La API procesa datos históricos y realiza predicciones para obtener un orden de cursos óptimo.

Para una interacción amigable y accesible, se ha creado una interfaz de usuario ubicada en la carpeta `frontend/`. Esta interfaz permite a los estudiantes obtener una mejor visualización de los datos y una experiencia más agradable.

El desarrollo y proceso creativo esta documentado en el archivo [Creative_Process.md](Creative_Process.md).

## Requisitos

Se configuro con [Docker](https://www.docker.com/) para facilitar el despliegue y desarrollo del proyecto con el uso de `docker-compose`. Pero no es necesario utilizarlo, ya que se puede ejecutar el proyecto sin Docker siguiendo los pasos de la sección de [desarrollo](#desarrollo).

### Backend

- [Python](https://www.python.org/downloads/) >= 3.10 (idealmente 3.11)
- [Poetry](https://python-poetry.org/) para la gestión de paquetes y entornos de Python.
- `ruff` + `black` para el formateo y linting de Python.

### Frontend

- Node.js (con npm)

## Desarrollo

### Backend

Utilizamos un gestor de dependencias llamado [poetry](https://python-poetry.org/docs/) que sirve para crear entornos virtuales y manejar las dependencias del proyecto.

1. Instala las dependencias:

```shell
poetry install
```

_Es posible que hayan problemas con tensorflow, si ocurre instalar manualmente con `poetry run pip install tensorflow[add-cuda]`_

2. Inicia una sesión shell con el nuevo entorno:

```shell
poetry shell
```

3. Ejecuta la API:

```shell
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en [localhost:8000](http://localhost:8000) y la documentación en [localhost:8000/docs](http://localhost:8000/docs).

#### Agregar dependencias

Para agregar nuevas dependencias, utiliza:

```shell
poetry add <nombre-del-paquete>
```

Y para actualizar las dependencias existentes:

```shell
poetry update
```

### Frontend

Se utiliza `npm` como gestor de paquetes. Para instalar las dependencias y ejecutar el programa:

```
npm install

pnm run dev
```
### Colaboradores

- Vasco Varas Nuñez. - [Vasco-Varas](https://github.com/Vasco-Varas)
- Diego Costa R. - [diegocostares](https://github.com/diegocostares)
- Manuel Blanco Contreras  - [MBlancoC](https://github.com/MBlancoC)
