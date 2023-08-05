# ista-python-curso2023
**Nombre del estudiante:** Andrés Sebastián Ullauri Vallejo

**Poyecto para curso:** Introducción a Python - Usos en Servicios Web

## Instalar dependencias:
```py
pip install -r requirements.txt
```

## Ejecutar el proyecto:
```py
flask run
```
## Obtener lista de estudiantes ordenada ascendentemente (JSON):

```json
[
  {
    "cedula": "1100405040",
    "primer_apellido": "Castro",
    "segundo_apellido": "Costa",
    "primer_nombre": "Andrea",
    "segundo_nombre": "María"
  },
  {
    "cedula": "1120303040",
    "primer_apellido": "Correa",
    "segundo_apellido": "Lasso",
    "primer_nombre": "Rafael",
    "segundo_nombre": "Guillermo"
  },
  {
    "cedula": "1150203440",
    "primer_apellido": "Ortega",
    "segundo_apellido": "Montaño",
    "primer_nombre": "Karen",
    "segundo_nombre": "Paulina"
  },
  {
    "cedula": "1100203040",
    "primer_apellido": "Ramírez",
    "segundo_apellido": "Arévalo",
    "primer_nombre": "David",
    "segundo_nombre": "Alejandro"
  },
  {
    "cedula": "0105813877",
    "primer_apellido": "Ullauri",
    "segundo_apellido": "Vallejo",
    "primer_nombre": "Andrés",
    "segundo_nombre": "Sebastián"
  }
]
```
<u>-DataSource: Archivo (CSV)</u>
*GET*
http://127.0.0.1:5000/lista-estudiantes

<u>-DataSource: base de datos (PostrgreSQL)</u>
*GET*
http://127.0.0.1:5000/lista-estudiantes?in_database=1

## Obtener lista de estudiantes ordenada ascendentemente (Tabla HTML ):

<img src="https://khkysohlylavihvzpybj.supabase.co/storage/v1/object/public/ista-python-curso-2023/students_list_html.webp?t=2023-08-05T00%3A19%3A51.805Z" />

<u>-DataSource: archivo (CSV)</u>
*GET*
http://127.0.0.1:5000/lista-estudiantes?in_html=1

<u>-DataSource: base de datos (PostrgreSQL)</u>
*GET*
http://127.0.0.1:5000/lista-estudiantes?in_html=1&?in_database=1

## Registrar una asistencia:

<img src="https://khkysohlylavihvzpybj.supabase.co/storage/v1/object/public/ista-python-curso-2023/register_attendance_api_call.webp" />

<u>-DataSource: archivo (CSV)</u>
*POST*
http://127.0.0.1:5000//registro-asistencia

<u>-DataSource: base de datos (PostrgreSQL)</u>
*POST*
http://127.0.0.1:5000//registro-asistencia?in_database=1

## Consultar total de asistencias:

<img src="https://khkysohlylavihvzpybj.supabase.co/storage/v1/object/public/ista-python-curso-2023/total_attendance_student_api_call.webp?t=2023-08-05T00%3A28%3A15.070Z" />

<u>-DataSource: archivo (CSV)</u>
*GET*
http://127.0.0.1:5000/total-asistencias?cedula_estudiante=0105813877&nombre_materia=python

<u>-DataSource: base de datos (PostrgreSQL)</u>
*GET*
http://127.0.0.1:5000/total-asistencias?cedula_estudiante=0105813877&nombre_materia=python&in_database=1

## Ejecutar los tests:
```py
pytest
```
## Log de chequeos para tests con Github Actions:
https://github.com/AndresUV7/ista-python-curso2023/actions
