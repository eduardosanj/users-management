# Pull de la imagen base oficial
FROM python:3.9.6-alpine


# setup del directorio de trabajo
WORKDIR /code

# Configuración de las variables de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Actualizamos pip a la versión más reciento
RUN pip install --upgrade pip

# Copiamos el fichero a /code dentro del contenedor
COPY requirements.txt /code/

# Instala todas las dependencias
RUN pip install -r requirements.txt

COPY . ./code/

ENTRYPOINT python main.py