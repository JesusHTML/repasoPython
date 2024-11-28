import json

#Pregunta 1: 

def cargar_datos(fichero):
    try:
        with open(fichero,"r")as archivo:
            return print(json.load(archivo))
    except FileNotFoundError:
        print("El fichero no existe")


def guardar_datos(fichero , datos):
        with open(fichero, "w")as archivo:
            json.dump(datos, archivo , indent=4)



datos = [
    {"nombre": "Pedro", "edad": 30, "ciudad": "Sevilla"},
    {"nombre": "Juan", "edad": 33, "ciudad": "Sevilla"},
    {"nombre": "Manolo", "edad": 35, "ciudad": "Teruel"}
]

cargar_datos("datos.json") 


guardar_datos("datos_nuevos.json", datos)


cargar_datos("datos_nuevos.json")

#Pregunta 2:

class Persona:
     
    def __init__(self, nombre , edad , ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def es_mayor_de_edad(self):
        return self.edad >=18
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"
        

persona = Persona("Jesus", 19 , "Sevilla")
print(persona)
print(persona.es_mayor_de_edad())

#Pregunta 3:

productos = [
    {"nombre": "manzana", "precio": 0.5, "cantidad": 50},
    {"nombre": "naranja", "precio": 0.8, "cantidad": 30},
    {"nombre": "pera", "precio": 0.75, "cantidad": 20},
    {"nombre": "platano", "precio": 0.4, "cantidad": 60}
]

def total_inventario(productos):
    return sum(producto["precio"] * producto["cantidad"] for producto in productos)

def producto_mas_caro(productos):
    producto_caro = max(productos, key=lambda producto: producto["precio"])
            #El dicionario  #La clave lamba  #argumento    #expresion del argumento
    return producto_caro ["nombre"] #Para que se muestre solo la fruta
 
print(total_inventario(productos))
print(producto_mas_caro(productos))

#Pregunta 4:

calificaciones = {
    "Ana": [90, 80, 85],
    "Carlos": [70, 75, 65],
    "Lucia": [88, 92, 84]
}

def promedio_calificaciones(calificaciones):
    promedios={}
    for estudiante , notas in calificaciones.items():
        promedios[estudiante] = sum(notas) / len(notas)   # Recuerda lo de las tildes
    return promedios

def mejor_promedio(calificaciones):
    promedios= promedio_calificaciones(calificaciones)
    mayor_media = max(promedios, key=promedios.get)

    return mayor_media

def añadir_estudiante(calificaciones,nombre,notas):
    calificaciones[nombre]= notas  # Recuerda lo de las tildes

def borrar_estudiante(calificaciones, nombre):
    if nombre in calificaciones:
        del calificaciones[nombre]  # Recuerda lo de las tildes
    else:
        print("Ese estudiante no existe")

def buscar_estudiante(calificaciones , nombre ):
    if nombre in calificaciones:
        return calificaciones[nombre]
    else:
        print(f"El nombre {nombre} no esta en la lista")



print(promedio_calificaciones(calificaciones))  # {'Ana': 85.0, 'Carlos': 70.0, 'Lucia': 88.0}
print(mejor_promedio(calificaciones))  # 'Lucia'
añadir_estudiante(calificaciones, "Jorge", [75, 80, 78])
print(calificaciones)  # Debería incluir a "Jorge" con sus notas
borrar_estudiante(calificaciones, "Carlos")
print(calificaciones)  # Debería haber eliminado a "Carlos"
print(buscar_estudiante(calificaciones, "Ana"))  # Debería mostrar la lista de calificaciones de Ana
print(buscar_estudiante(calificaciones, "Carlos"))  # Debería mostrar un mensaje indicando que no existe


    
         