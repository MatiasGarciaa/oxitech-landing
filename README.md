# Óxitech — App Django

Landing page del software de gestión anticorrosiva Óxitech.

## Instalación

### 1. Copiar la app al proyecto

Copia la carpeta completa `oxitech/` a la raíz de tu proyecto Django (al mismo nivel que `manage.py`).

### 2. Registrar la app en `settings.py`

```python
INSTALLED_APPS = [
    # ... apps existentes
    'oxitech',
]
```

### 3. Incluir las URLs en el proyecto raíz

En el `urls.py` del proyecto (no de la app), agregar:

```python
from django.urls import path, include

urlpatterns = [
    # ... rutas existentes
    path('oxitech/', include('oxitech.urls', namespace='oxitech')),
]
```

Si quieres que la landing sea la **página principal** del proyecto:

```python
urlpatterns = [
    path('', include('oxitech.urls', namespace='oxitech')),
    # ...
]
```

### 4. Verificar que `STATICFILES_DIRS` y `TEMPLATES` estén configurados

En `settings.py` asegúrate de tener:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # IMPORTANTE
        # ...
    },
]

STATIC_URL = '/static/'
```

### 5. Correr el servidor

```bash
python manage.py runserver
```

La landing estará disponible en `http://127.0.0.1:8000/oxitech/` (o en `/` si configuraste la ruta raíz).

## Estructura de archivos

```
oxitech/
├── __init__.py
├── apps.py
├── admin.py
├── models.py           # vacío por ahora
├── views.py            # vista única: landing()
├── urls.py             # namespace 'oxitech'
├── templates/
│   └── oxitech/
│       └── landing.html
└── static/
    └── oxitech/
        ├── css/
        │   └── landing.css
        ├── js/
        │   └── landing.js
        └── img/         # para imágenes futuras
```

## Personalización

- **Colores:** editar las variables CSS en `static/oxitech/css/landing.css` (bloque `:root`).
- **Tipografías:** Fraunces (display serif) + Inter (sans-serif body), cargadas desde Google Fonts.
- **Contenido:** todo el texto vive en `templates/oxitech/landing.html`.

## Próximos pasos

- Conectar formulario de contacto con backend.
- Agregar vista de login/signup para administradores.
- Construir el dashboard interno una vez validada la propuesta.
