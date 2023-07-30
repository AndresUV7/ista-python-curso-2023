import pytest
from escuela_api.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_attendance_record(client):
    valid_attendance = {
        'cedula': '0105813877',
        'materia': 'javascript',
        'fecha_año': 2023,
        'fecha_mes': 7,
        'fecha_dia': 30
    }

    attendance_record_response = client.post('/registro-asistencia', json=valid_attendance)

    assert attendance_record_response.status_code == 201

    attendance_record_data = attendance_record_response.get_json()
    assert attendance_record_data['message'] == 'Asistencia registrada exitosamente!.'

def test_invalid_attendance_record(client):
    invalid_attendance = {
        'cedula': '0105813877',
        'materia': 'javascript',
        'fecha_año': 2023,
        'fecha_mes': 7,
    }

    attendance_record_response = client.post('/registro-asistencia', json=invalid_attendance)

    assert attendance_record_response.status_code == 400

    attendance_record_data = attendance_record_response.get_json()
    assert attendance_record_data['error'] == 'Datos incompletos o mal formados en la solicitud.'

def test_empty_request(client):
    attendance_record_response = client.post('/registro-asistencia', json={})

    assert attendance_record_response.status_code == 400

    data = attendance_record_response.get_json()
    assert data['error'] == 'Datos incompletos o mal formados en la solicitud.'

if __name__ == '__main__':
    pytest.main()
