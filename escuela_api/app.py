from flask import Flask, jsonify, redirect, render_template, request
import csv
import json
from escuela_api.database.store import (
    student_list_ascending_order_from_database,
    get_student_total_attendance_by_course_from_database,
    create_student_attendance_record_in_database
)

app = Flask(__name__)

ATTENDANCE_RECORD_FIELDS = ['cedula', 'materia', 'fecha_año', 'fecha_mes', 'fecha_dia']

ATTENDANCE_FILE_PATH = 'escuela_api/datos/asistencia.csv'

def ends_with_newline(file_path):
    with open(file_path, 'rb') as f:
        f.seek(-1, 2)
        return f.read() == b'\n'

@app.route('/')
def redirect_to_student_list_in_html():
    return redirect('/lista-estudiantes?in_html=1')

@app.route('/lista-estudiantes', methods=['GET'])
def get_student_list_ascending_order():
    in_database = request.args.get('in_database')
    in_html = request.args.get('in_html')
    with open('escuela_api/datos/estudiante.csv', 'r', encoding='utf-8') as student_csv_file:
        students = csv.DictReader(student_csv_file)
        student_list = list(students)
        student_list_ascending_order = sorted(student_list,
                                                     key=lambda 
                                                     x: (x['primer_apellido'],
                                                          x['segundo_apellido'],
                                                          x['primer_nombre'],
                                                          x['segundo_nombre'],))
    if in_html == "1":
        sorted_student_list = student_list_ascending_order_from_database if in_database == "1" else student_list_ascending_order
        return render_template('student_list.html', student_list=sorted_student_list)
    else:
        return json.dumps(student_list_ascending_order_from_database) if in_database == "1" else json.dumps(student_list_ascending_order) 


@app.route('/registro-asistencia', methods=['POST'])
def create_student_attendance_record():
    attendance = request.get_json()
    in_database = request.args.get('in_database')
    if attendance and all(key in attendance for key in ATTENDANCE_RECORD_FIELDS):
        if (in_database == "1"):
            create_student_attendance_record_in_database(attendance)
        else:
            with open(ATTENDANCE_FILE_PATH, 'a', newline='') as attendance_file:
                writer = csv.writer(attendance_file)
                if not ends_with_newline(ATTENDANCE_FILE_PATH):
                    attendance_file.write('\n') 
                writer.writerow([attendance[ATTENDANCE_RECORD_FIELDS[0]],
                                  attendance[ATTENDANCE_RECORD_FIELDS[1]],
                                  attendance[ATTENDANCE_RECORD_FIELDS[2]],
                                  attendance[ATTENDANCE_RECORD_FIELDS[3]],
                                  attendance[ATTENDANCE_RECORD_FIELDS[4]]])
        return jsonify({'message': 'Asistencia registrada exitosamente!.'}), 201
    else:
        return jsonify({'error': 'Datos incompletos o mal formados en la solicitud.'}), 400


@app.route('/total-asistencias', methods=['GET'])
def get_student_total_attendance_by_course():
    id = request.args.get('cedula_estudiante')
    course = request.args.get('nombre_curso')
    in_database = request.args.get('in_database')
    if not id or not course:
        return jsonify({'error': 'Parámetros faltantes en la solicitud!'}), 400
    total_attendance = 0
    if (in_database == "1"):
        total_attendance = get_student_total_attendance_by_course_from_database(id, course)
    else:
        with open(ATTENDANCE_FILE_PATH, 'r') as attendance_file:
            for row in csv.DictReader(attendance_file):
                if row['cedula'] == id and row['materia'] == course:
                    total_attendance += 1
    return (jsonify({'total_asistencias': total_attendance}), 200) if total_attendance>0 \
          else (jsonify({'error': 'El estudiante o la materia requerida no existen'}), 404)
          #El error 404 "Not Found" se muestra cuando no se encuentra un recurso en línea


if __name__ == '__main__':
    app.run()
