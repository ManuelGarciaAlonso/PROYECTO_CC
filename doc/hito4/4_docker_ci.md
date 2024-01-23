## Aprovechamiento del Contenedor de Docker en CI

### Uso del Contenedor Docker en GitHub Actions y Jenkins


#### Implementación:
- Utilización del contenedor Docker creado en el Hito 3 para ejecutar pruebas en ambos sistemas de CI.
- Configuración en `.github/workflows/ci.yml` y en el trabajo de Jenkins para construir y utilizar el contenedor.

#### Adaptaciones Realizadas:
- Ajustes en el Dockerfile para incluir herramientas de CI.
- Asegurar que el entorno del contenedor sea fiel al de producción.
