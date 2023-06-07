import requests
import pandas as pd

# Definición de las categorías y subcategorías
categorias = {
    'tecnologia': ['tv-y-video', 'audio', 'informatica', 'celulares-y-tablet', 'videojuegos-y-smartwatch'],
    'Electrodomesticos': ['climatisacion', 'pequeños-electrodomedistocos', 'lavados', 'cocina-y-horno', 'heladera-y-freezer', 'hogar-y-limpieza', 'cuidado-personal-y-salud', 'termotaque-y-calefones'],
    'Hogar': ['muebles-de-interior', 'coina-y-comedor', 'baño', 'organizacion', 'iluminacion', 'dormitorio', 'herraientas-y-mantenimieto', 'deco'],
    'Bebidas': ['aperitivos', 'aervezas', 'gaseosas', 'jugos', 'aguas', 'vinos-y-espumantes', 'izotonicas-y-energisantes', 'bebidas-blancas-y-licores'],
    'Almacen': ['aceites-y-vinagres', 'aceitunas-y-encurtidos', 'aderezos', 'arros-y-legumbres', 'caldos,-sopas-y-pure', 'conservas', 'desayuno-y-merienda', 'golosinas-y-chocolates', 'harinas', 'sin-tacc', 'panificados', 'para-preparar', 'pastas-secas-y-salsas', 'sal,-pimienta-y-especias', 'snacks'],
    'Lacteos': ['dulce-de-leche', 'leches', 'cremas', 'yogures', 'mantecas-y-margarinas', 'postres', 'flanes'],
    'Quesos-y-Fiambres': ['quesos', 'fiambres', 'salchichas'],
    'Carnes': ['carne-vacuna', 'carne-de-cerdo', 'carne-de-pollo', 'enbutidos', 'pezcados', 'maricos'],
    'Frutas-y-verduras': ['frutas', 'verduras', 'huevos', 'legumbres-y-semillas', 'hiebas-aromaticas', 'leña-y-carbon'],
    'taeq': ['almacen-taeq', 'frutas-y-verduras-taeq', 'congelados-taeq'],
    'congelados': ['frutas-congeladas', 'verduras-congeladas', 'papas-congeladas', 'comidas-preparadas', 'prefritos-congelados', 'helados-y-postres', 'carnes-y-pollo', 'hamburguesas-y-milanesas'],
    'pastas-frescas-y-tapas': ['levaduras-y-grasas', 'fideos-y-ñoquis', 'pas-rellenas', 'tapas'],
    'limpieza': ['accesorios-de-limpieza', 'calzados', 'cuidado-de-ropa', 'desodorantes-de-ambiente', 'insecticidas', 'lavandinas', 'limpiezas-de-baño', 'limpieza-de-cocina', 'limpieza-de-pisos-y-muebles', 'papeles'],
    'perfumeria': ['cuidado-capilar', 'cuidado-oral', 'cuidado-personal', 'cuidado-de-la-piel', 'proteccion-femenina', 'proteccion-para-adultos', 'farmacia'],
    'bebes-y-niños': ['higiene-y-salud', 'lactancia-y-alimentacion', 'seguridad-del-bebe', 'paseo-del-bebe', 'veiculos-intatiles', 'jugueteria', 'accesorios', 'pañales-y-toallitas-humedas'],
    'vehiculos': ['accesorio-poara-automovile', 'accesorio-para-motos', 'neumaticos'],
    'mascotas': ['aliementos', 'accesorios-para-mascotas'],
    'aire-libre-y-jardin': ['camping', 'piletas', 'cuidado-del-jardin', 'muebles-de-exterior', 'asador', 'iluminacion'],
    'libreria': ['libreria-y-papeleria'],
    'deportes': ['fitness', 'bicicletas', 'accesorios-deportivos', 'patinaje']
}
productos = []  # Lista para almacenar los productos obtenidos

# Configuración de los proxies
#proxies = {
#    'http': 'http://usuario:contraseña@servidor_proxy:puerto',
#    'https': 'https://usuario:contraseña@servidor_proxy:puerto'
#}
   
    

sucursales = {
    "Cordoba hipermercado Lgones": 1,
    "Cordoba hipermercado Rivera": 2,
    "Cordoba hipermercado Jacinto Rios": 3,
    "Cordoba hipermercado Ruta 9": 4,
    "Mendoza hipermercado Godoy Cruz": 5,
    "Mendoza tinda digital Capital": 5,
    "Tucuman hipermercado tucuman 1": 6,
    "Tucuman hipermercado tucuman 2": 7,
    "Misiones hipermercado Posadas": 8,
    "Chacho hipermercado chaco": 9,
    "Santa Fe hipermercado Rosario": 10,
    "santa Fe hipermercado Rafaela": 11,
    "Santiago del Estero Supermercado": 12,
    "San Juan hipermercado san juan": 13,
    "Salta hipermercado Salta": 14
} 
     
sucursal = sucursales['Santiago del Estero Supermercado']
    
# Recorremos las categorías y subcategorías
   
for cat, sub_cat in categorias.items():
    categoria = cat
    for sub in sub_cat:
        sub_categoria = sub
        pagina = 0

        while True:
            try:
                # Construcción de la URL de la API
                url_api = 'https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/' + categoria + '/' + sub_categoria + '?O=OrderByTopSaleDESC&_from=' + str(pagina) + '&_to=' + str(pagina + 23) + '&ft&sc='+ str(sucursal)

                # Realizamos una solicitud GET a la API no utilizando proxies
                response = requests.get(url_api)

                # Parseamos la respuesta JSON
                data = response.json()

                contador = 0
                for producto in data:
                    try:
                        # Extraemos los datos relevantes de cada producto y los agregamos a la lista
                        productos.append({
                            "Nombre": producto['productName'],
                            "Precio": producto['items'][0]['sellers'][0]['commertialOffer']['Price'],
                            "Precio_lista": producto['items'][0]['sellers'][0]['commertialOffer']['ListPrice'],
                            "Categoria": producto['categories'],
                            "Stock": producto['items'][0]['sellers'][0]['commertialOffer']['AvailableQuantity'],
                            "Link": producto['link']
                        })
                        contador += 1
                    except KeyError:
                        print("Error al obtener información del producto:", producto)

                if contador > 23:
                    pagina += 23  # Aumentamos el valor de la página para obtener el siguiente lote de productos
                else:
                    break  # Salimos del bucle si ya no hay más productos

            except requests.exceptions.RequestException as e:
                print("Error de conexión:", str(e))

            except ValueError as e:
                print("Error al procesar la respuesta JSON:", str(e))

            except Exception as e:
                print("Error desconocido:", str(e))

        print(sub_categoria)  # Imprimimos la subcategoría actual

# Crear un DataFrame a partir de la lista de productos
df = pd.DataFrame(productos)

# Configuración del nombre y la ubicación del archivo CSV
nombre_archivo = "productos_hiperlibertad.csv"
ubicacion_archivo = r"C:\Users\Nacho\jupyter" + nombre_archivo

# Guardar el DataFrame como archivo CSV
df.to_csv(ubicacion_archivo, index=False)

print("Archivo CSV guardado correctamente en:", ubicacion_archivo)