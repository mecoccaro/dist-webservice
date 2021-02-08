# Webservice Sistemas Distribuidos

## Requisitos
* Python 3 o superior
* Ambiente virtual
* Django 3.1 o superior
* Django REST Framework
* Django REST Swagger

## Instrucciones para su uso
* Descargue el proyecto
* Ubíquese en la carpeta del proyecto 
* Ingrese a su ambiente virtual 
  * Linux o MacOS:  ``` $source venv/bin/activate ```
  * Para Windows: ```  $ venv\Scripts\activate.bat ```

* Ejecute los siguientes comandos para la base de datos
  * ```  python manage.py makemigrations ```
  * ```  python manage.py migrate ```
  
* Para ejecutar el proyecto realice el siguiente comando
```python manage.py runserver```
## Documentación

*Se utilizo Django REST Swagger para la documentación, para ello ejecute el proyecto e ir a la siguiente ruta:
```/api/documentation```

*Es posible que de un error, ya que el Swagger lo han dejado de desarrollar, si da un error con un "load staticfile" se puede solucionar de la siguiente manera:*
Ir a la ruta que indica normalmente la siguiente
``Python\Python39\Lib\site-packages\rest_framework_swagger\templates\rest_framework_swagger\index.html``
En ese HTML el segundo tag```{% load staticfile %}``` se debe cambiar al siguiente
```{% load static %}```
Asi el swagger no da el error.

* Se tiene habilitada tambien la documentación de Django REST Framework, para ver las vistas, en un navegador use las rutas de cada endpoint y ahi vera la documentación.
## Endpoints disponibles

* Listar Escuelas.
```GET /api/school```

* Crear Escuelas
```POST /api/school```
```Body:
{
    "name": string,
    "description": string,
    "faculty_fk": integer
}
```

* Actualizar Escuelas
```PUT /api/school-detail/:id```
```Body:
{
    "name": string,
    "description": string,
    "faculty_fk": integer
}
```

* Eliminar Escuela
```DELETE /api/school-delete/:id```

* Obtener Escuela
```GET /api/school-detail/:id```

* Listar Secciones.
```GET /api/section```

* Crear Secciones
```POST /api/section```
```Body:
{
    "name": string,
    "description": string,
    "uc": integer,
    "semester": integer,
    "type": M or E,
    "ht": integer,
    "hp": integer,
    "hl": integer,
    "school_fk": integer
}
```
* Actualizar Secciones
```PUT /api/section-details/:id```
```Body:
{
    "name": string,
    "description": string,
    "uc": integer,
    "semester": integer,
    "type": M or E,
    "ht": integer,
    "hp": integer,
    "hl": integer,
    "school_fk": integer
}
```
* Eliminar Secciones
```DELETE /api/section-delete/:id```

* Obtener Secciones
```GET /api/section-detail/:id```

* Listar Personas.
```GET /api/person```

* Crear Personas
```POST /api/person```
```Body:
{
    "first_name": String,
    "last_name": String,
    "cedula": integer
}
```
* Actualizar Personas
```PUT /api/person-details/:id```
```Body:
{
    "first_name": String,
    "last_name": String,
    "cedula": integer
}
```
* Eliminar Personas
```DELETE /api/person-delete/:id```

* Obtener Personas
```GET /api/person-detail/:id```

* Inscribir en sección
```POST /api/enrollsect```
```Body:
{
    "section_fk": integer,
    "enrollment_fk": integer
}
```

* Eliminar persona de seccion
```DELETE /api/enrollsect-delete/:id```

* Listar los estudiantes de una sección
```GET /api/student-section/:student-id```

* Listar los profesores de una sección
```GET /api/teacher-section/:teacher-id```