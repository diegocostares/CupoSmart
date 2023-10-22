<h1 align="center">
  <img src="CupoSmart_logo.jpeg" width="150px">
  <br>
  <a href=# name="readme-top">CupoSmart</a>
</h1>

## Introducción

## Requisitos

### Backend

- [Python](https://www.python.org/downloads/) >= 3.10 (idealmente 3.11)
- [Docker](https://www.docker.com/).
- [Poetry](https://python-poetry.org/) para la gestión de paquetes y entornos de Python.
- `ruff` + `black` para el formateo y linting de Python.

### Frontend

- Node.js (con npm)

### Datos
- [quota.csv](https://onedrive.live.com/download?resid=461550F0C2C01195%21591027&authkey=!AHJRWqVhzqsb-IM)

## Desarrollo

### Backend

Utilizamos un gestor de dependencias llamado [poetry](https://python-poetry.org/docs/) que sirve para crear entornos virtuales y manejar las dependencias del proyecto.

1. Instala las dependencias:

```shell
poetry install
```

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
