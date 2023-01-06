
import re
import string
from datetime import datetime, timezone
import json
import pandas as pd
import random
import shutil
import os
from more_itertools import chunked

#Jimmy del futuro, recuerda que el texto debe ser correcto tal y como esta en el ejemplo
# print("\n UN EJEMPLO \n\nQuestion\nCloud Kicks generates leads for its different product categories (shoes, apparel, and accessories) \nHow should the administrator configure Salesforce to meet this requirement?\nA. Create business processes and record types for each of the three product categories.\nB. Create a page layout for each category and filter the Lead Source field based on category.\nAnswer: B C D\nQuestion\nrel, and accessories) How should the administrator configure Salesforce to meet this requirement?\nA. Create b for each of the three product categories.\nB. Create a paged filter the Lead Source field based on category.\nAnswer: A")
#Puedes hacer un print y te saldra, recuerda instalar todas las librerias y solo tienes que cambiar estas rutas nada mas, dejare el programa del examen dentro del googledrive :)

#OJO no intentes entender el codigo que esta realmente jodido xd
##################################
Archivo_con_preguntas_txt = r"C:\Users\jtonato\Music\Salesforce.txt"

destino_a_guardar = r"C:\Users\jtonato\Music"

numero_examen = ' ADM 201'

tecnologia = 'SALESFORCE'

numero_de_preguntas_por_examen = 65

numero_de_variaciones_de_test = 5
#############################################

def sacar_pregunta_respuesta_por_separado():

    with open(Archivo_con_preguntas_txt, encoding='utf-8') as f:
        text = f.read()
    questions = []
    current_question = ""
    lines = text.split("\n")

    for line in lines:
        if line == "Question":
            if current_question:
                questions.append(current_question)
            current_question = ""
        else:
            current_question += line + "\n"
    questions.append(current_question)
    return questions


def convertir_en_diccionario_preguntas_opciones_respuestas(Lista_preguntas):
    resultados = []
    letras = string.ascii_uppercase

    for elemento in Lista_preguntas:

        pregunta = elemento.split('\nAnswer:')[0]
        pregunta = pregunta.split('A.')[0]
        pregunta = pregunta.replace('\n', ' ')
        opciones = elemento.split('\nAnswer:')[0]
        opciones = re.split("\n[A-Z]\. ", opciones)[1:]
        respuesta = elemento.split('\nAnswer:')[1].strip()
        opciones_diccionario = {}
        for i, opcion in enumerate(opciones):
            clave = letras[i]
            valor = opcion.replace('\n', ' ')
            opciones_diccionario[clave] = valor
        resultado = {'pregunta': pregunta, 'opciones': opciones_diccionario,
                     'respuesta': [opciones_diccionario[r] for r in respuesta.split()]}
        resultados.append(resultado)
    return resultados

def inital_JSON(nombre_fichero, numero_preguntas):
    now = datetime.now(timezone.utc).isoformat()
    print(now)
    json_final_test = \
        {"createdAt": now,
         "title": "TEST "+tecnologia+ numero_examen + nombre_fichero,
         "description": "Demo Exam to show the  list order questions as well as explanations.",
         "code": "000-000s",
         "pass": 65,
         "time": 120,
         "image": "https://i.pinimg.com/originals/a6/25/88/a62588dc61ca87e10f1f0cd052123314.png",
         "author": {
             "id": ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
             "name": "Test Salesforce",
             "image": "https://yt3.ggpht.com/-9Q_OGPy0Reg/AAAAAAAAAAI/AAAAAAAAAAA/a-GWCV9iwcA/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"
         },
         "cover": [
             {"variant": 2, "text": "EXAM PRACTICE"},
             {"variant": 2, "text": " ¡¡ SUERTE !!"},
             {
                 "variant": 0,
                 "text": "https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/6/slack-innovations-dreamforce.jpg?d=500x500&f=inside"
             },
             {"variant": 2, "text": "Dispone de 2 horas para realizar el examen."},
             {"variant": 2, "text": "La puntuación mínima es del 65%."},
             {"variant": 2, "text": "Este examen consta de "+numero_preguntas+" preguntas."}
         ],
         "test": []
         }
    return json_final_test

def insertar_datos_JSON(plantilla_inicial, preguntas, nombre_carpeta, nombre_fichero):
    letras = string.ascii_uppercase
    for pre in preguntas:

        temp = {"answer": [], "question": [{"variant": 1, "text":pre['pregunta'] }], "explanation": [],
                "variant": (1 if len(pre['respuesta']) > 1 else 0), "choices": []}
        opciones = list(pre['opciones'].items())
        random.shuffle(opciones)
        opciones = dict(opciones)

        for i, opci in enumerate(opciones):
            temp['choices'].append({"label": letras[i], "text": opciones[opci]})
            temp['answer'].append((True if opciones[opci] in pre['respuesta'] else False))
        plantilla_inicial['test'].append(temp)
    with open(nombre_carpeta+"\TEST "+nombre_fichero+".json", "w") as f:
        json.dump(plantilla_inicial, f, indent=2)


def examen_completo(Lista_preguntas):
    nombre_fichero = tecnologia+ numero_examen +' COMPLETO'
    nombre_carpeta = "EXAMENES "+tecnologia+ numero_examen + "/EXAMEN COMPLETO DE " + str(len(Lista_preguntas)) + " PREGUNTAS"
    os.makedirs(nombre_carpeta)
    for i in range(2):
        preguntas_con_su_respuesta_parseadas = convertir_en_diccionario_preguntas_opciones_respuestas(Lista_preguntas)
        JSON_EXAM = inital_JSON(nombre_fichero, str(len(Lista_preguntas)))
        insertar_datos_JSON(JSON_EXAM, preguntas_con_su_respuesta_parseadas, nombre_carpeta, nombre_fichero)
        nombre_fichero = tecnologia+ numero_examen+ ' COMPLETO DESORDENADO'
        random.shuffle(Lista_preguntas)
        random.shuffle(Lista_preguntas)


def examen_por_versiones(nombre_fichero, Lista_preguntas, nombre_carpeta):

    preguntas_con_su_respuesta_parseadas = convertir_en_diccionario_preguntas_opciones_respuestas(Lista_preguntas)
    JSON_EXAM = inital_JSON(nombre_fichero, str(len(Lista_preguntas)))
    insertar_datos_JSON(JSON_EXAM, preguntas_con_su_respuesta_parseadas, nombre_carpeta, nombre_fichero)


def print_hi():
    #try:
    os.chdir(destino_a_guardar)
    if os.path.exists("EXAMENES "+tecnologia+ numero_examen):
        shutil.rmtree("EXAMENES "+tecnologia+ numero_examen)
    os.mkdir("EXAMENES "+tecnologia+ numero_examen)


    Lista_preguntas = sacar_pregunta_respuesta_por_separado()

    examen_completo(Lista_preguntas)

    groups = chunked(Lista_preguntas, numero_de_preguntas_por_examen)
    os.makedirs("EXAMENES " + tecnologia + numero_examen + "/EXAMENES POR PARTES")
    for i, group in enumerate(groups):
        nombre_carperta = "EXAMENES " + tecnologia + numero_examen + "/EXAMENES POR PARTES/PARTE " + str(i + 1)
        os.makedirs(nombre_carperta)
        for n in range(numero_de_variaciones_de_test):
            random.shuffle(group)
            examen_por_versiones(" Version "+str(i+1)+"."+str(n+1), group, nombre_carperta)
    #except:
        #print("EL TEXTO INSERTADO ES INCORRECTO O EL DESTINO DE DONDE QUIERES QUE SE GUARDE\n UN EJEMPLO \n\nQuestion\nCloud Kicks generates leads for its different product categories (shoes, apparel, and accessories) \nHow should the administrator configure Salesforce to meet this requirement?\nA. Create business processes and record types for each of the three product categories.\nB. Create a page layout for each category and filter the Lead Source field based on category.\nAnswer: B C D\nQuestion\nrel, and accessories) How should the administrator configure Salesforce to meet this requirement?\nA. Create b for each of the three product categories.\nB. Create a paged filter the Lead Source field based on category.\nAnswer: A")


if __name__ == '__main__':

    print_hi()

