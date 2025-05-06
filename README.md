# Reddit Insights — MVP

Este proyecto busca identificar oportunidades de negocio analizando publicaciones de Reddit mediante LLMs. El sistema se estructura como un pipeline modular y limpio, listo para escalar.

---

## 📁 Estructura del Proyecto

```
reddit_insights/
├── app/
│   ├── config/           # Configuración general (.env, settings)
│   ├── reddit/           # Cliente y lógica para conectarse a Reddit
│   ├── llm/              # Cliente de LLM y lógica de análisis
│   ├── db/               # Modelos y acceso a base de datos
│   ├── pipeline/         # Orquestación principal del flujo
│   └── utils/            # Utilidades como logging, helpers
├── scripts/              # Entrada principal para ejecutar el pipeline
├── tests/                # Pruebas unitarias del sistema
├── .env                  # Variables de entorno
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## 🔍 Descripción de Módulos

### `app/config/settings.py`

Carga y organiza las variables de entorno necesarias para el proyecto (claves de API, configuración de DB, etc.).

### `app/reddit/`

* `client.py`: Conexión con la API de Reddit (por ejemplo, usando `praw`).
* `fetcher.py`: Lógica para obtener publicaciones recientes de subreddits configurados.

### `app/llm/`

* `prompt_builder.py`: Construye el prompt adecuado para enviar al LLM.
* `analyzer.py`: Envía el post al modelo (OpenAI, Gemini, etc.) y obtiene el análisis estructurado.

### `app/db/`

* `models.py`: Define las tablas de la base de datos con SQLAlchemy.
* `crud.py`: Funciones de acceso y manipulación de datos (insertar post, filtrar duplicados, guardar análisis...).

### `app/pipeline/runner.py`

Orquesta el flujo de todo el pipeline:

1. Ingesta desde Reddit
2. Filtrado de ya existentes
3. Análisis con LLM
4. Persistencia en base de datos

### `app/utils/logger.py`

Define un logger común para el proyecto usando `loguru` o `logging`.

---

## 🚀 `scripts/run_pipeline.py`

Script principal para ejecutar todo el proceso de forma secuencial y modular. Ideal para lanzarlo por cronjob o desde un notebook.

---

## 🧪 `tests/`

Contiene las pruebas unitarias para cada módulo del sistema. A medida que crezca el sistema, este directorio se expandirá.

---

## ✅ Objetivo del MVP

* Detectar si un post representa una oportunidad de negocio.
* Extraer problema, solución, mercado, competencia, etc.
* Guardar la información estructurada en una base de datos.
* Hacerlo de forma modular, extensible y preparada para escalar.

---

## ⚙️ Requisitos

* Python 3.10+
* SQLite para pruebas (puede migrarse a PostgreSQL fácilmente)
* `praw`, `openai`, `sqlalchemy`, `dotenv`, `loguru`, etc.
