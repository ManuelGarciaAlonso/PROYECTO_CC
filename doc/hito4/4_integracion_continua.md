## Integración Continua Funcionando y Correcta Justificación

### Sistema Elegido: GitHub Actions

#### Justificación:
- **Integración con GitHub**: Ofrece integración directa y eficiente con GitHub, facilitando la configuración y el seguimiento de la CI.
- **Facilidad de Uso y Flexibilidad**: Permite personalizar flujos de trabajo y es fácil de configurar a través de archivos YAML.
- **Soporte y Comunidad Amplia**: Acceso a una extensa biblioteca de acciones y soporte comunitario.

### Configuración:
- Archivo `.github/workflows/ci.yml` para definir los pasos de CI.
- Activación automática en cada `push` y `pull request`.


Elección y justificación de sistema de integración continua 
Para el proyecto se ha decidido hacer uso de Jenkins ya que nos proporciona diferentes ventajas:
1. Flexibilidad y personalización:
2. Robustez y uso de herramientas:
3. Escalabilidad:
4. Comunidad y soporte:

- Instalación de Jenkins en un servidor o uso de un servicio en la nube.

Para usar Jenkins debemos descargar el programa desde su página oficial. En el proceso de instalación debemos escoger tanto el puerto como el tipo de servidor a usar, en nuestro caso 8080 en localhost. Una vez hemos hecho estas configuraciones previas introducimos tanto el usuario como una contraseña de administrador.

![](/./img/4_jenkins_login.png)
![](/./img/4_jenkins_login2.png)

Ya configurado el entorno podemos ver el panel de control de jenkins
![](/./img/4_jenkins_initial_look.png)
 