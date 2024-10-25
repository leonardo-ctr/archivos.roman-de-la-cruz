# archivos.roman-de-la-cruz
prueba de envio de codigo y de screenshot

Abrir un archivo en el servidor
Supongamos que tenemos el siguiente archivo, ubicado en la misma carpeta que Python:

archivo de demostración.txt
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
![image](https://github.com/user-attachments/assets/5e0a5ed7-5c08-4a66-a146-90b5288e6175)
![image](https://github.com/user-attachments/assets/744f32d6-3a32-496b-ae66-5bfd67758f1b)

2
Para abrir el archivo, utilice la función incorporada open().
La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:
EjemploObtenga su propio servidor Python
f = open("demofile.txt", "r")
print(f.read())
![image](https://github.com/user-attachments/assets/9c0ce1b7-de3a-4c20-a5f0-ea2b29b58a1d)
![image](https://github.com/user-attachments/assets/720a61ec-1839-4fa0-bf76-d5e6f2c05bd4)


3
Si el archivo se encuentra en una ubicación diferente, deberá especificar la ruta del archivo, de esta manera:
Ejemplo
Abrir un archivo en una ubicación diferente:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
![image](https://github.com/user-attachments/assets/a93d571e-511f-46a4-b6a2-861b66b70d7c)
![image](https://github.com/user-attachments/assets/f55b555b-31f1-4544-9372-d42e157e1527)

4
Leer solo partes del archivo
De forma predeterminada, el read()método devuelve el texto completo, pero también puedes especificar cuántos caracteres quieres devolver:
Ejemplo
Devuelve los 5 primeros caracteres del archivo:
f = open("demofile.txt", "r")
print(f.read())
![image](https://github.com/user-attachments/assets/6d179430-c400-4313-907c-888acd0a1cea)
![image](https://github.com/user-attachments/assets/c24c1d78-65b5-41c7-8e9a-be8358e3d184)

5
Escritura de archivos en Python
❮ AnteriorPróximo ❯Escribir en un archivo existente
Para escribir en un archivo existente, debe agregar un parámetro a la open()función:
"a"- Anexar - se agregará al final del archivo
"w"- Escribir: sobrescribirá cualquier contenido existente

Ejemplo:
Abra el archivo "demofile2.txt" y agregue contenido al archivo:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
![image](https://github.com/user-attachments/assets/e1f2164a-483f-46d9-b16d-3811705be6a1)
![image](https://github.com/user-attachments/assets/de5c5681-2a43-4f9a-8fe4-30a47ee7727c)

6
Ejemplo
Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
![image](https://github.com/user-attachments/assets/734ef6b6-7a84-4aef-9cfb-fad8b8f0f9cc)
![image](https://github.com/user-attachments/assets/1ba3f1a2-f177-4d98-8ef0-580b5bb548aa)


7
liminar archivo de Python
❮ AnteriorPróximo ❯Eliminar un archivo
Para eliminar un archivo, debes importar el módulo del sistema operativo y ejecutar su os.remove()función:
Ejemplo
Eliminar el archivo "demofile.txt":
import os
os.remove("demofile.txt")
![image](https://github.com/user-attachments/assets/39bb4b94-a673-46c3-bfa1-8a2842dd484e)
![image](https://github.com/user-attachments/assets/d04685f3-4c2f-4d3c-a3cc-efa7b9704a9b)

8
Comprobar si el archivo existe:
Para evitar obtener un error, es posible que desees verificar si el archivo existe antes de intentar eliminarlo:
Ejemplo
Comprueba si el archivo existe  elimínalo:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
![image](https://github.com/user-attachments/assets/567a4d9d-875a-40ec-a56d-2ac79cf00768)
![image](https://github.com/user-attachments/assets/184fd5b5-a15e-44a7-9114-674d1ddb4b9a)

9
Eliminar carpeta
Para eliminar una carpeta entera, utilice el os.rmdir()método:
Ejemplo
Eliminar la carpeta "myfolder":
import os
os.rmdir("myfolder")

![image](https://github.com/user-attachments/assets/94fc3dc4-3c1d-4879-b361-6f88f5d135da)
![image](https://github.com/user-attachments/assets/6ec5e913-7a68-4c9c-947a-af191e40305a)


eh, no se si este esta bien profe



