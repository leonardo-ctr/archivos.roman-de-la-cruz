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


