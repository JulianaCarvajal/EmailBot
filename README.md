# EmailBot 📧

Envío de correos electrónicos mediante Gmail con manejo seguro de credenciales.

## 🚀 Características

- Envío de correos a través de Gmail
- Configuración mediante archivo `.env` (sin exponer credenciales)
- Test básico con `pytest` para validar comportamiento del sistema

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

## ▶️ Uso

Ejecutar el archivo principal:
```
python main.py
```
Esto enviará un correo utilizando los datos cargados desde `.env`. El asunto y contenido pueden personalizarse dentro del script.

## 🧪 Testeo

```
# PowerShell
$env:PYTHONPATH="."
pytest

# Git Bash / Linux / Mac
PYTHONPATH=. pytest
```

## 📂 Estructura del proyecto

```
EmailBot/
│
├── main.py
├── .gitignore
├── .env              # Ignorado por Git
├── requirements.txt
├── README.md
├── tests/
│   └── test_main.py
```

