# Test-Generator-To-Study

Este script Python tiene como objetivo parsear un archivo de texto en formato JSON para que pueda ser utilizado por un programa de test dejo en este enlace el programa (es muy basico )  [LINK DESCARGA](https://drive.google.com/drive/folders/1DWobaLTSAhOpK-CZOR48NfPOyMgHSJl-?usp=sharing)
El formato esperado por el script del archivo de texto es el siguiente:.

```
Question
User at Cloud Kicks want to see information more useful for their role on the Case page.
How should an administrator make the pages more dynamic and easier to use?
A. Add Component visibility filters to the Components.
B. Remove fields from the record details component.
C. Delete the extra component from the page.
D. Include more tab components with filters.
Answer: A
Question
An administrator has assigned a permission set group with the two-factor authentication for
User Interface Logins permissions and the two-factor authentication for API Logins permission to a group of
users.
Which two prompts will happen when one of the users attempts to log in to Data Loader?
Choose 2 answers
A. Users need to connect an authenticator app to their Salesforce account.
B. Users need to get a security token from a trusted network using Reset My Security Token.
C. Users need to download and install an authenticator app on their mobile device.
D. Users need to enter a verification code from email or SMS, whichever has higher priority.
Answer: A C
```

Para mejorar la dificultad de los test, el script reordena de forma aleatoria las preguntas y opciones de respuesta del archivo de texto. Aunque el código podría ser mejorado, cumple con su función.

Es importante que tengas en cuenta que es necesario importar y añadir algunos datos al interior del script antes de poder utilizarlo.

Archivo_con_preguntas_txt = r""

destino_a_guardar = r""

numero_examen = ''

tecnologia = ''

numero_de_preguntas_por_examen = 

numero_de_variaciones_de_test = 

