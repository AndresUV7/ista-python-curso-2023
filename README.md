# ista-python-curso2023
Nombre del estudiante: Andrés Sebastián Ullauri Vallejo

Poyecto para curso: Introducción a Python - Usos en Servicios Web

Endpoints:

Obtener lista de estudiantes ordenada ascendentemente (JSON)

    -DataSource: Archivo (CSV)
    *GET
    http://127.0.0.1:5000/lista-estudiantes
    -DataSource: base de datos (PostrgreSQL):
    *GET
    http://127.0.0.1:5000/lista-estudiantes?in_database=1

Obtener lista de estudiantes ordenada ascendentemente (Tabla HTML ):

    -DataSource: archivo (CSV)
    *GET
    http://127.0.0.1:5000/lista-estudiantes?in_html=1
    -DataSource: base de datos (PostrgreSQL):
    *GET
    http://127.0.0.1:5000/lista-estudiantes?in_html=1&?in_database=1

Registrar una asistencia:

    -DataSource: archivo (CSV)
    *POST
    http://127.0.0.1:5000//registro-asistencia
    -DataSource: base de datos (PostrgreSQL):
    *POST
    http://127.0.0.1:5000//registro-asistencia?in_database=1

Consultar total de asistencias:
    
    -DataSource: archivo (CSV)
    *GET
    http://127.0.0.1:5000/total-asistencias?cedula_estudiante=0105813877&nombre_materia=python
    -DataSource: base de datos (PostrgreSQL):
    *GET
    http://127.0.0.1:5000/total-asistencias?cedula_estudiante=0105813877&nombre_materia=python&in_database=1

