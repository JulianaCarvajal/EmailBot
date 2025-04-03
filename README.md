# EmailBot 📧

Envío de correos electrónicos mediante Gmail con manejo seguro de credenciales y opción para adjuntar archivos.

---

## 🚀 Características

- Envío de correos a través de Gmail (SMTP)
- Configuración mediante archivo `.env` (sin exponer credenciales)
- Permite personalización del mensaje en `email_content.py`
- Permite adjuntar archivos (opcional)
- Test básico con `pytest` para validar comportamiento del sistema

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

