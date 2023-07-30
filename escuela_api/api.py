from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

ATTENDANCE_RECORD_FIELDS = ['cedula', 'materia', 'fecha_año', 'fecha_mes', 'fecha_dia']

ATTENDANCE_FILE_PATH = 'datos/asistencia.csv'

def ends_with_newline(file_path):
    with open(file_path, 'rb') as f:
        f.seek(-1, 2)
        return f.read() == b'\n'


@app.route('/lista-estudiantes', methods=['GET'])
def get_student_list_ascending_order():
    with open('datos/estudiante.csv', 'r', encoding='utf-8') as student_csv_file:
        students = csv.DictReader(student_csv_file)
        student_list = list(students)
        student_list_ascending_order = sorted(student_list,
                                                     key=lambda 
                                                     x: (x['primer_apellido'],
                                                          x['segundo_apellido'],
                                                          x['primer_nombre'],
                                                          x['segundo_nombre'],))
    return jsonify(student_list_ascending_order)


@app.route('/registro-asistencia', methods=['POST'])
def attendance_record():
    attendance = request.get_json()
    if attendance and all(key in attendance for key in ATTENDANCE_RECORD_FIELDS):
        with open(ATTENDANCE_FILE_PATH, 'a', newline='') as attendance_file:
            writer = csv.writer(attendance_file)
            if not ends_with_newline("datos/asistencia.csv"):
                attendance_file.write('\n') 
            writer.writerow([attendance[ATTENDANCE_RECORD_FIELDS[0]], attendance[ATTENDANCE_RECORD_FIELDS[1]],
                              attendance[ATTENDANCE_RECORD_FIELDS[2]], attendance[ATTENDANCE_RECORD_FIELDS[3]],
                                attendance[ATTENDANCE_RECORD_FIELDS[4]]])
        return jsonify({'message': 'Asistencia registrada exitosamente!.'}), 201
    else:
        return jsonify({'error': 'Datos incompletos o mal formados en la solicitud.'}), 400


@app.route('/total-asistencias', methods=['GET'])
def total_attendance():
    id = request.args.get('cedula_estudiante')
    course = request.args.get('nombre_curso')
    if not id or not course:
        return jsonify({'error': 'Parámetros faltantes en la solicitud!'}), 400
    total_attendance = 0
    with open(ATTENDANCE_FILE_PATH, 'r') as attendance_file:
        for row in csv.DictReader(attendance_file):
            if row['cedula'] == id and row['materia'] == course:
                total_attendance += 1
    return (jsonify({'total_asistencias': total_attendance}), 200) if total_attendance>0 else (jsonify({'error': 'El estudiante o la materia requerida no existen'}), 404)


if __name__ == '__main__':
    app.run()