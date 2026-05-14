# 📝 Mi Blog - Proyecto Final Django

Un blog personal moderno, completo y responsive desarrollado con Django y Bootstrap. Permite crear, editar, eliminar y visualizar posts, con un sistema completo de autenticación y mensajería privada.

## 🌟 Características

### Funcionalidades Principales

- **📰 Gestión de Posts**
  - Crear, editar, eliminar y ver posts
  - Editor de contenido enriquecido (CKEditor)
  - Soporte para imágenes
  - Sistema de fechas automático

- **👤 Sistema de Usuarios**
  - Registro y autenticación segura
  - Perfiles de usuario personalizados
  - Avatar de perfil
  - Biografía y fecha de nacimiento
  - Cambio de contraseña

- **💬 Mensajería Privada**
  - Enviar mensajes directos entre usuarios
  - Conversaciones organizadas
  - Historial de mensajes
  - Notificación de mensajes no leídos

- **🎨 Interfaz Moderna**
  - Bootstrap 5 responsive
  - Diseño profesional y moderno
  - Navbar dinámico según autenticación
  - Animaciones y transiciones suaves
  - Footer informativo

### Seguridad

- ✅ LoginRequiredMixin para vistas protegidas
- ✅ Decoradores @login_required en funciones
- ✅ Validación de formularios
- ✅ CSRF protection
- ✅ Contraseñas hasheadas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.14+, Django 6.0.5
- **Base de Datos**: SQLite (desarrollo)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Editor de Contenido**: CKEditor
- **Procesamiento de Imágenes**: Pillow

## 📋 Requisitos

- Python 3.10+
- pip

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/proyecto-final-blog.git
cd proyecto-final-blog
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

Accede a `http://127.0.0.1:8000/` en tu navegador.

## 📁 Estructura del Proyecto

```
proyecto_final_py/
├── blog/                    # App para los posts
│   ├── models.py           # Modelo Post
│   ├── views.py            # Vistas del blog
│   ├── urls.py             # URLs del blog
│   └── admin.py            # Admin personalizado
├── accounts/               # App para autenticación y perfiles
│   ├── models.py           # Modelo Profile
│   ├── views.py            # Vistas de autenticación
│   ├── forms.py            # Formularios de usuario y perfil
│   ├── signals.py          # Señales para crear perfil automático
│   └── admin.py            # Admin de perfiles
├── messaging/              # App para mensajería
│   ├── models.py           # Modelos Conversacion y Mensaje
│   ├── views.py            # Vistas de mensajería
│   ├── forms.py            # Formularios de mensajes
│   ├── urls.py             # URLs de mensajería
│   └── admin.py            # Admin de mensajería
├── templates/              # Templates HTML
│   ├── base.html           # Template base con navbar
│   ├── home.html           # Página de inicio
│   ├── about.html          # Página de información
│   ├── pages.html          # Listado de posts
│   ├── post_detail.html    # Detalle de post
│   ├── post_form.html      # Formulario de crear/editar post
│   ├── post_confirm_delete.html  # Confirmación de eliminación
│   ├── profile.html        # Perfil de usuario
│   ├── edit_profile.html   # Editar perfil
│   ├── password_change.html        # Cambiar contraseña
│   ├── password_change_done.html   # Confirmación de cambio
│   ├── accounts/
│   │   ├── login.html      # Página de login
│   │   └── signup.html     # Página de registro
│   └── messaging/
│       ├── inbox.html      # Inbox de mensajes
│       ├── conversacion_detalle.html  # Chat
│       └── nuevo_mensaje.html   # Nuevo mensaje
├── media/                  # Archivos subidos (avatares, imágenes de posts)
├── playground/             # Configuración del proyecto
│   ├── settings.py         # Configuración
│   ├── urls.py             # URLs principales
│   └── wsgi.py
├── manage.py               # Gestión de Django
├── requirements.txt        # Dependencias
├── .gitignore             # Archivos ignorados por Git
├── README.md              # Este archivo
└── db.sqlite3             # Base de datos (no versionado)
```

## 🌐 Rutas Principales

### Blog
- `/` - Inicio
- `/about/` - Página de información
- `/pages/` - Listado de posts
- `/pages/create/` - Crear nuevo post
- `/pages/<id>/` - Detalle del post
- `/pages/<id>/edit/` - Editar post
- `/pages/<id>/delete/` - Eliminar post

### Autenticación
- `/accounts/login/` - Iniciar sesión
- `/accounts/signup/` - Registro
- `/accounts/logout/` - Cerrar sesión
- `/accounts/profile/` - Ver perfil
- `/accounts/profile/edit/` - Editar perfil
- `/accounts/password-change/` - Cambiar contraseña

### Mensajería
- `/messaging/inbox/` - Bandeja de entrada
- `/messaging/conversacion/<id>/` - Ver conversación
- `/messaging/nuevo/<user_id>/` - Enviar mensaje a usuario
- `/messaging/iniciar/<user_id>/` - Iniciar conversación

### Admin
- `/admin/` - Panel de administración

## 📊 Modelos de Datos

### Post
```python
- titulo: CharField(max_length=100)
- subtitulo: CharField(max_length=100)
- contenido: RichTextField (CKEditor)
- imagen: ImageField
- fecha: DateField (auto_now_add=True)
```

### Profile
```python
- user: OneToOneField(User)
- avatar: ImageField
- bio: TextField
- fecha_nacimiento: DateField
```

### Conversacion
```python
- participantes: ManyToManyField(User)
- fecha_creacion: DateTimeField (auto_now_add=True)
- fecha_actualizacion: DateTimeField (auto_now=True)
```

### Mensaje
```python
- conversacion: ForeignKey(Conversacion)
- remitente: ForeignKey(User)
- contenido: TextField
- fecha_envio: DateTimeField (auto_now_add=True)
- leido: BooleanField (default=False)
```

## 🔐 Seguridad y Buenas Prácticas

- ✅ Contraseñas hasheadas con algoritmos modernos
- ✅ CSRF protection en todos los formularios
- ✅ SQL injection prevention (ORM Django)
- ✅ XSS protection
- ✅ Validación de formularios tanto en cliente como servidor
- ✅ Acceso restringido a vistas según autenticación
- ✅ Señales automáticas para crear perfiles

## 🎯 Casos de Uso Implementados

### Para Usuarios No Autenticados
- Ver página de inicio
- Ver información del sitio
- Leer posts y sus detalles
- Iniciar sesión
- Registrarse

### Para Usuarios Autenticados
- Crear nuevos posts
- Editar sus propios posts
- Eliminar sus propios posts
- Ver y editar su perfil
- Cambiar su contraseña
- Enviar y recibir mensajes privados
- Ver historial de conversaciones

## 🧪 Pruebas Recomendadas

1. **Crear usuario**: Registrarse con un nuevo usuario
2. **Crear post**: Crear un post con imagen
3. **Editar post**: Modificar un post existente
4. **Eliminar post**: Confirmar eliminación
5. **Editar perfil**: Cambiar avatar y biografía
6. **Cambiar contraseña**: Verificar que funcione
7. **Enviar mensaje**: Enviar mensaje a otro usuario
8. **Ver conversación**: Verificar historial de mensajes
9. **Logout**: Cerrar sesión y verificar acceso restringido
10. **Admin**: Verificar que todos los modelos se vean

## 📝 Notas Importantes

- Las imágenes se guardan en la carpeta `/media/`
- El CKEditor permite contenido HTML enriquecido
- Los mensajes se cargan dinámicamente en la conversación
- El navbar se adapta según el estado de autenticación
- Los avatares se redondean automáticamente

## 🚀 Próximas Mejoras Posibles

- [ ] Sistema de comentarios en posts
- [ ] Likes/Favoritos en posts
- [ ] Búsqueda de posts
- [ ] Paginación de posts
- [ ] Notificaciones en tiempo real
- [ ] Subida de múltiples imágenes
- [ ] Integración con redes sociales
- [ ] Temas personalizables
- [ ] API REST
- [ ] Deployment en producción

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

**Tu Nombre**
- Email: tu@email.com
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes, abre un issue primero para discutir los cambios propuestos.

## ❓ Soporte

Si tienes preguntas o problemas, abre un issue en el repositorio.

---

**Hecho con ❤️ usando Django y Bootstrap**
