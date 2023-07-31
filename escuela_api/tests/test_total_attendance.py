import pytest
from escuela_api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_total_attendance_valid(client):
    total_attendance_response = client.get('/total-asistencias?cedula_estudiante=0105813877&nombre_curso=python')
    assert total_attendance_response.status_code == 200

    total_attendance_data = total_attendance_response.get_json()
    assert 'total_asistencias' in total_attendance_data
    assert total_attendance_data['total_asistencias'] == 5

def test_total_attendance_missing_parameters(client):
    total_attendance_response = client.get('/total-asistencias')
    assert total_attendance_response.status_code == 400

    total_attendance_data = total_attendance_response.get_json()
    assert 'error' in total_attendance_data
    assert total_attendance_data['error'] == 'Parámetros faltantes en la solicitud!'

def test_total_attendance_no_matching_data(client):
    total_attendance_response = client.get('/total-asistencias?cedula_estudiante=0105813877&nombre_curso=Javascript')
    assert total_attendance_response.status_code == 404

if __name__ == '__main__':
    pytest.main()
