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







