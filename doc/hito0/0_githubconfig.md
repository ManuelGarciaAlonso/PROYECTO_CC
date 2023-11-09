## Configuración de usuario y repositorio
### Edición del perfil
Para que la identificación del perfil sea mejor, se ha establecido una imagen de perfil junto con una serie de datos personales:
![Edición del perfil](img/edit_perfil.png)

### Activación del segundo factor de autenticación
Para la autenticación en dos pasos se ha necesitado de un dispositivo auxiliar. En esta imagen se puede ver el mensaje de confirmación que nos asegura que el proceso se ha completado de manera correcta. Con esta función, se solicitará una doble confirmación de identidad cada vez que se inicie sesión en un nuevo dispositivo.
![Autenticación en dos pasos](img/auth_2pasos.png)

### Creación de claves
En la siguiente imagen podemos ver cómo generar las claves pública y privada del protocolo SSH desde nuestro ordenador local:
![Configuración SSH 1](img/ssh1.png)

En esta imagen podemos ver las dos claves generadas y el contenido de la  clave pública que debemos usar para introducir en nuestro GitHub:
![Configuración SSH 2](img/ssh2.png)

Una vez hemos añadido nuestra clave pública a GitHub vemos cómo la conexion se ha establecido correctamente:
![Configuración SSH 3](img/ssh3.png)

Finalmente podemos ver cómo se incluye la carpeta de fotos para esta sección desde la línea de comandos:
![Prueba conexión SSH](img/subir_folder.png)
