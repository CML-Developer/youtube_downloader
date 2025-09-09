### Guía de Inicio Rápido: Descargador de Videos de YouTube

Esta guía te ayudará a configurar y usar la aplicación para descargar videos de YouTube directamente a tu computadora.

#### Paso 1: Requisitos
Asegúrate de tener instalados **Python** y **live-server** en tu sistema.
-   **Python:** Si no lo tienes, puedes descargarlo de https://www.python.org/
-   **live-server:** Es un servidor de desarrollo simple para archivos estáticos. Si no lo tienes, ábre una terminal y ejecuta:
    ```bash
    npm install -g live-server
    ```
    (Necesitas tener Node.js y npm instalados para esto. Si no, puedes usar `python -m http.server` en su lugar).

#### Paso 2: Descarga los Archivos
Asegúrate de tener los siguientes 3 archivos en una misma carpeta en tu computadora:
1.  `requirements.txt`
2.  `app.py`
3.  `youtube_downloader.html`

#### Paso 3: Instalar las dependencias de Python
Abre una terminal y navega hasta la carpeta donde guardaste los archivos requirements.txt. Ejecuta el siguiente comando para instalar todo lo que necesitas:
```bash
pip install -r requirements.txt

### Paso 4: Instalar FFmpeg para audio
- Descomprime el archivo .zip en un lugar fácil de recordar, como C:\Program Files\ffmpeg.

- Ahora, necesitas agregar la carpeta bin de FFmpeg a las variables de entorno de tu sistema (esto le dice a Windows dónde encontrar el programa).

- Busca "editar variables de entorno del sistema" en el menú de inicio y ábrelo.

- Haz clic en "Variables de entorno...".

- En la sección de "Variables de usuario", busca la variable Path y haz clic en "Editar...".

- Haz clic en "Nuevo" y agrega la ruta a la carpeta bin que creaste. Por ejemplo: C:\Program Files\ffmpeg\bin.

- Haz clic en "Aceptar" en todas las ventanas para guardar los cambios.

- Cierra todas las terminales que tengas abiertas y abre una nueva. Esto es importante para que el nuevo Path se active.

- En la nueva terminal, ejecuta ffmpeg -version. Si ves los detalles de la versión, ¡lo has instalado correctamente!

### Paso 5: Iniciar script de python
- Abre una terminal y navega hasta la carpeta py en donde se encutra el script de python llamado app.py

- Ejecuta el siguiente comando: python app.py

### Paso 6: Iniciar servidor local
- Navega en otra terminal hasta la carpeta donde se encuentra el archivo youtube_downloader.html

- Ejecuta el comando: live-server

- Se abrira una ventana donde podras pegar el link y se descargara en la carpeta videos_guardados, si no se abre la ventana, abre tu navegador y escribe ttp://127.0.0.1:8080
