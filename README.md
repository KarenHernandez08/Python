# Python
 
 Para comenzar a trabajar con `Django` en  `Python` vamos a installar django en nuestro proyecto

  Primero vamos a instalar Pyenv
```
pip install pyenv-win --target $HOME\\.pyenv
pip install pyenv-win --target %USERPROFILE%\.pyenv

```
Vamos a crear una parpeta llamada `python` en la terminal nos ubicaremos en ese directorio con el comando `cd`
Ya que estamos en la carpeta vamos a colocar los siguientes comandos para instalar la versión de python con la que trabajaremos en nuetsro proyecto

```
pyenv install 3.8.8
```
Como instalamos la versión de python ahora podemos trabajar localmente en una versión de python

```
pyenv local 3.8.8

```
Installamos pipenv 

```
pip install pipenv
```
Instalamos paquetes de pipenv

```
pipenv install
```
Podemos observar con el comando `ls` que se nos crearon dos archivos 

```
Pipfile         Pipfile.lock
```
Ahora instalaremos nuestro framework 

```
py -m pip install django

```

Es hora de crear nuestro proyecto `skills`

```
django-admin startproject skills
```

Es hora de abrir nuestro IDE y nuestros archivos se veran así:

![](https://github.com/KarenHernandez08/Python/blob/main/imagenes/py.PNG)

ahora para correrlo, regresarnos al cmd y colocar este comando, debido a que no hemos colocado nada, necesitamos hacer migraciones primero 

```
// este es para migrar
python manage.py migrate
// este ya es oara que corra en nuestro localhost
python manage.py runserver 0.0.0.0:3000

```
En nuestro buscador de internet colocaremos `localhost:3000`
![](https://github.com/KarenHernandez08/Python/blob/main/imagenes/local.PNG)

Ahora vamos a `localhost:3000/admin`
![](https://github.com/KarenHernandez08/Python/blob/main/imagenes/admin.PNG)

Vamos a crear el administrador, para eso nos vamos al cmd 

```
python manage.py createsuperuser
```

Nos va a pedir 
 - Usuario 
 - Correo
 - Contraseña
 - Validazión de contraseña

Volvemos a correr nuestro pruyecto con `python manage.py runserver 0.0.0.0:3000`, nos vamos a nueestro buscador y colocamos `localhost:3000/admin` ahora colocaremos el username y el password que le colocamos en el cmd 

![](https://github.com/KarenHernandez08/Python/blob/main/imagenes/admins.PNG)

por ultimo para crear una aplicación dentro de nuestro proyecto vamos al cmd y ponemos:

```
python manage.py startapp nombre_app
```
A la hora de abrir nuestro proyecto en el IDE ahora se veran también las aplicaciones creadas
![](https://github.com/KarenHernandez08/Python/blob/main/imagenes/app.PNG)





