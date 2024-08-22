# Flask SQLAlchemy Docker

## Descripción de la aplicación
Esta aplicación es un microservicio desarrollado con Flask que permite leer y escribir en una base de datos usando SQLAlchemy.

## Funcionamiento de la aplicación
La aplicación expone una API RESTful con los siguientes endpoints:
- `GET /items`: Obtiene todos los elementos de la base de datos.
- `POST /items`: Crea un nuevo elemento en la base de datos.

## Requisitos para hacerla funcionar
- Docker
- Docker Compose

## Instrucciones para ejecutarla en local
1. Clona el repositorio: `git clone https://github.com/tu-usuario/flask-sqlalchemy-docker.git`
2. Navega al directorio del proyecto: `cd flask-sqlalchemy-docker`
3. Construye y ejecuta los contenedores: `docker-compose up --build`
4. La aplicación estará disponible en `http://localhost:5000`

## Configuración
La aplicación puede ser configurada mediante variables de entorno:
- `DB_HOST`: Host de la base de datos.
- `DB_PORT`: Puerto de la base de datos.
- `DB_USER`: Usuario de la base de datos.
- `DB_PASSWORD`: Contraseña de la base de datos.
- `DB_NAME`: Nombre de la base de datos.
