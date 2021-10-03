"""
Las condiciones de los datos de entrada deben ser las siguientes:
-Texto de no menos de 30 palabras que incluya correos electrónicos y opiniones de 
    un servicio o producto. Ejemplo text = "producto excelente, ssalazarf@gmail.com, 
    el servicio ofrecido es malo, ve que tan bacano el servicio, joselitor@udistrital.edu.co, 
    servicio muy bueno, bla bla bla, producto cumple muy bien”

Las condiciones de los datos de salida deben ser las siguientes:
-Impresión en pantalla de la palabra “bueno” cada vez que aparezca un comentario bueno e 
    imprimir cuantas veces aparece un comentario bueno.
-Impresión en pantalla de todo el texto cambiando cada palabra sinónima de bueno por 
    la palabra “bueno”.
-Impresión en pantalla de todos los correos electrónicos encontrados en el texto.

Bono: exportar los datos de salida a un .csv
"""
import re
import csv  

text = ("Es de buena calidad la verdad muy bueno no me decepcionó para nada, "
        + "No es lo que esperaba pensaba que era mejor no quede satisfecho, "
        + "billgates@microsoft.com, nespejobern@uniminuto.edu.co, javi55@gmail.com, "
        + "Es bueno no se traba funciona bien, "
        + "No puedes exigirle que cumpla lo mismo que uno más caro. Me pareció muy bueno, "
        + "No podría gustarme más llego a saber su gran calidad y rendimiento es útil, " 
        + "Las fotos son de otra galaxia. Es servible jamás se ha colgado en 8 meses de uso, "
        + "Muy oportuno, " 
        + "No me gustó es pésimo")

synonyms = ["bueno", "útil", "conveniente", "oportuno", "adecuado", "provechoso", "beneficioso", 
            "favorable", "servible", "ventajoso", "saludable"]        

countComments = 0
changedToSynonym = text

with open('comments.csv', mode='w', newline='') as csv_file:
    fieldnames = ['word', 'matches']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for synonym in synonyms:
        #Set the pattern to synonym to search and change
        pattern = re.compile(r'\b'+synonym+r'\b')
        findAll = pattern.findall(text)
        #If find a match
        if (findAll):
            count = len(findAll)
            countComments += count
            writer.writerow({'word': synonym, 
                            'matches': count})
            print(findAll , "\tEncontrados: ", count)

        patternToChange = re.compile(r'\b('+synonym[:1].upper()+r'|'+synonym[:1]+')'
                                    +synonym[1:]+r'\b')
        changedToSynonym = patternToChange.sub("bueno", changedToSynonym)                        

print('Comentarios buenos encontrados: ', countComments)
print('\nTexto alterado:\n', changedToSynonym)

patternMail = re.compile(r' \b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', re.X)
print('\nE-mails encontrados:\n', patternMail.findall(text))