#Integrante 1: Juan Felipe Ruiz 2359397-2724
# Integrante 2: Jhorman Loaiza 2359710-2724
#Docente: Luis German Toro Pareja
#Matematicas Discretas 2
#Grupo51
#Laboratorio 5
import re

#Funcion para abrir t leer el archivo txt
def abrir_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

#Esta funcion identifica las palabras que contiene las 5 vocales
def contiene_cinco_vocales(palabra):
    vocales = set('aeiou')
    return vocales.issubset(set(palabra.lower()))

#Aqui estan los scripts para identificar las caracterisiticas del texto
def encontrar_patrones(texto):
    #Script para preguntas en ingles y españo ¿?
    patron_preguntas = r'[\w\s]+[\?¿]'
    
    #Script para exclamasiones en ingles y español !¡
    patron_exclamaciones = r'[\w\s]+[!¡]'
    
    #Script para abreviaciones mas comunes de ambos lenguajes
    patron_abreviaciones = r"\b(?:i'm|he's|it's|we're|i've|don't|Jr\.|dr\.|sr\.|sra\.|Ud\.|dpto\.|Pág\.)\b"

    
    #Patron para encontrar las palabras
    patron_palabras = r'\b\w+\b'
    
    #Aqui se buscan los patrones de los textos
    preguntas = re.findall(patron_preguntas, texto)
    exclamaciones = re.findall(patron_exclamaciones, texto)
    abreviaciones = re.findall(patron_abreviaciones, texto)
    palabras = re.findall(patron_palabras, texto)
    
    #Este ciclo llama la funcion que identifica las 5 vocales y las filtra
    palabras_cinco_vocales = [palabra for palabra in palabras if contiene_cinco_vocales(palabra)]
    
    return preguntas, exclamaciones, abreviaciones, palabras_cinco_vocales

ruta_archivo = 'C:/Users/juanr/OneDrive/Escritorio/lector de texto/Archivo.txt'
#El texto usado fue :A Smart Bomb with a Language Parser
contenido = abrir_archivo(ruta_archivo)

#los patrones del texto llaman la funcion para encontrar los patrones y los filtra
preguntas, exclamaciones, abreviaciones, palabras_cinco_vocales = encontrar_patrones(contenido)

#Resultado de las funciones y los filtros 
print("Preguntas encontradas:")
for pregunta in preguntas:
    print(pregunta)

print("\nExclamaciones encontradas:")
for exclamacion in exclamaciones:
    print(exclamacion)

print("\nAbreviaciones encontradas:")
for abreviacion in abreviaciones:
    print(abreviacion)

print("\nPalabras que contienen las 5 vocales:")
for palabra in palabras_cinco_vocales:
    print(palabra)