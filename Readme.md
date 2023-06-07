# Instrucciones para ejecutar el código
Para ejecutar el código correctamente, debes tener instalado Python en tu sistema y tener acceso a Internet. A continuación, te proporciono los pasos necesarios:

## 1. Instalar Python
Si aún no tienes Python instalado, puedes descargarlo desde el sitio web oficial de Python (https://www.python.org) e instalar la versión adecuada para tu sistema operativo.

## 2. Instalar las dependencias
El código utiliza las bibliotecas requests y pandas. Puedes instalarlas ejecutando los siguientes comandos en tu terminal:

bash
Copy code
* pip install requests
* pip install pandas
## 3. Configurar proxies (opcional)
Si estás detrás de un servidor proxy, puedes descomentar las líneas de código que definen los proxies y proporcionar la información correcta de tu servidor proxy en el archivo nombre_archivo.py.

python
Copy code
# Configuración de los proxies
proxies = {
    'http': 'http://usuario:contraseña@servidor_proxy:puerto',
    'https': 'https://usuario:contraseña@servidor_proxy:puerto'
}
Reemplaza "usuario", "contraseña", "servidor_proxy" y "puerto" con los valores correspondientes de tu servidor proxy.

## 4. Ejecutar el código
Puedes ejecutar el código en un entorno de desarrollo de Python o desde la línea de comandos. Asegúrate de que estás en el directorio correcto donde se encuentra el archivo de código. Ejecuta el siguiente comando:

bash
Copy code
* python nombre_archivo.py
Reemplaza "nombre_archivo.py" con el nombre real del archivo en el que guardaste el código.

## 5. Esperar a que se complete la ejecución
El código realizará solicitudes a la API de Hiper Libertad para obtener información de productos. Dependiendo de la cantidad de productos y la velocidad de tu conexión a Internet, puede llevar algún tiempo completar la ejecución.

## 6. Archivo CSV generado
Una vez que se completa la ejecución, se generará un archivo CSV llamado "productos_hiperlibertad.csv" en el directorio especificado en la variable "ubicacion_archivo". Este archivo contendrá los datos de los productos obtenidos.

Recuerda que, en el archivo "nombre_archivo.py", debes reemplazar "nombre_archivo" con el nombre real del archivo en el que guardaste el código.

Si tienes alguna pregunta o problema al ejecutar el código, no dudes en contactarme.

### faltantes incluyen:
por cuenstiones de tiempo hay cosas que no se pudieron completar en forma:
como la implementacion automatica de las categorias de los productos de forma automatica utilizando Scrapy o Selenium

tambien falto la utilizacion de programamcion orientada a objetos y modularizacion del codigo


- /* aqunque el codigo es corto y se puede entender si esta escrito de forma secuencial 

##### Si tienes alguna pregunta o problema al ejecutar el código, no dudes en contactarme.


