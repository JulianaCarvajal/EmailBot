# EmailBot 📧

Envío de correos electrónicos mediante Gmail con manejo seguro de credenciales y opción para adjuntar archivos.

---

## 🚀 Características

- Envío de correos a través de Gmail (SMTP)
- Configuración mediante archivo `.env` (sin exponer credenciales)
- Permite personalización del mensaje en `email_content.py`
- Permite adjuntar archivos (opcional)
- Test básico con `pytest` para validar comportamiento del sistema
- Programación automática del envío utilizando el Programador de Tareas de Windows

---

## 🔧 Instalación

1. Clonar este repositorio:
    ```bash
   git clone https://github.com/JulianaCarvajal/EmailBot.git
   cd EmailBot
2. Crear y activar un entorno virtual
    ````bash
   python -m venv .venv
   # PowerShell
   .\.venv\Scripts\Activate.ps1
   # Git Bash
   source .venv/Scripts/activate
3. Instalar dependencias:
    ```bash
   pip install -r requirements.txt
4. Crear un archivo `.env` con tus credenciales
    ```env
   EMAIL_ADDRESS=tu_email@gmail.com
   EMAIL_RECEIVER=destinatario@example.com
   EMAIL_PASS=tu_contraseña_de_aplicación
5. Crear un archivo `email_content.py` con el asunto y cuerpo del mensaje. Si deseas adjuntar archivos también debes 
especificarlos aquí en forma de lista
   > Puedes usar `email_content.example.py` como plantilla.

---

## ▶️ Uso

Ejecutar el archivo principal:
```
python main.py
```
Esto enviará el correo con las credenciales y contenido configurados.

---

## ⏰ Programar el envío automático

Puedes programar el envío automático utilizando el Programador de tareas.

### En Windows

1. Abrir el Programador de tareas.
2. Crear una nueva tarea básica.
3. Configurar:
   - **Desencadenador**:
     - Seleccionar fecha y hora de ejecución (y si es necesario, repetir diariamente, semanalmente o mensualmente).
     - Activar: "Ejecutar tarea lo antes posible si no hubo inicio programado" (muy importante si el equipo puede estar apagado).
   - **Acción**:
     - Programa o script: Ruta al ejecutable de Python de tu entorno virtual, por ejemplo:
       ```
       C:\Users\TuUsuario\EmailBot\.venv\Scripts\python.exe
       ```
     - Agregar argumentos: Nombre del archivo principal:
       ```
       main.py
       ```
     - Iniciar en: Ruta de tu proyecto donde está `main.py`, por ejemplo:
       ```
       C:\Users\TuUsuario\EmailBot
       ```
   - **Condiciones**:
     - Opcional: Activar "Activar el equipo para ejecutar esta tarea" si deseas que despierte de suspensión.

4. Guardar y activar la tarea.

### En otros sistemas operativos

- **Linux/MacOS**:  
  Puedes lograr la misma funcionalidad usando Cron Jobs.  
  El proceso sería programar una tarea `cron` que ejecute el comando `python main.py` en la fecha/hora deseadas.

- **Servicios en la nube** (avanzado):  
  Alternativamente, podrías desplegar este proyecto en un servicio como **AWS Lambda**, **Google Cloud Functions** o un pequeño servidor para asegurar que esté siempre disponible sin depender de un equipo personal.

---

## 🧪 Testeo

Puedes ejecutar los tests con:
```
# PowerShell
$env:PYTHONPATH="."
pytest

# Git Bash / Linux / Mac
PYTHONPATH=. pytest
```

---

## 📂 Estructura del proyecto

```
EmailBot/
│
├── main.py
├── .gitignore
├── .env                      # Ignorado por Git
├── requirements.txt
├── README.md
├── email_content.py          # Ignorado por Git
├── email_content_example.py
├── tests/
│   └── test_main.py
```

