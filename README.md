# Junosty
Servicio web de gestión escolar que permite el acceso al plantel mediante códigos QR y una aplicación móvil. 

### Guía de instalación.

#### Clona el proyecto.
```
git clone https://github.com/omarsalazar/Junosty
cd Junosty
```

#### Entorno virtual

Instalación del entorno.
```
pip install python-virtualenv
```
Creación del entorno virtual.
```
virtualenv -p python3 myvenv
```
Activación.
```
source myvenv/bin/activate
```

#### Instalación de dependencias.
```
pip install -r requirements.txt
```
### Ejecuta el proyecto.
```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
