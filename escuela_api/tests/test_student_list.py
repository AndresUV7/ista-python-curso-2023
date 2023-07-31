import json
import pytest
from escuela_api.app import app

EXPECTED_STUDENT_LIST = [
  {
    "cedula": "1100405040",
    "primer_apellido": "Castro",
    "primer_nombre": "Andrea",
    "segundo_apellido": "Costa",
    "segundo_nombre": "María"
  },
  {
    "cedula": "1120303040",
    "primer_apellido": "Correa",
    "primer_nombre": "Rafael",
    "segundo_apellido": "Lasso",
    "segundo_nombre": "Guillermo"
  },
  {
    "cedula": "1150203440",
    "primer_apellido": "Ortega",
    "primer_nombre": "Karen",
    "segundo_apellido": "Montaño",
    "segundo_nombre": "Paulina"
  },
  {
    "cedula": "1100203040",
    "primer_apellido": "Ramírez",
    "primer_nombre": "David",
    "segundo_apellido": "Arévalo",
    "segundo_nombre": "Alejando"
  },
  {
    "cedula": "0105813877",
    "primer_apellido": "Ullauri",
    "primer_nombre": "Andrés",
    "segundo_apellido": "Vallejo",
    "segundo_nombre": "Sebastián"
  }
]

def compare_dictionary_arrays(array1, array2):
    return set(tuple(sorted(dictionary.items())) 
               for dictionary in array1) == set(tuple(sorted(dictionary.items()))
                                                 for dictionary in array2)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_student_list_ascending_order(client):

    student_list_response = client.get('/lista-estudiantes')

    assert student_list_response.status_code == 200

    student_list_data = json.loads(student_list_response.data)

    assert isinstance(student_list_data, list)

    assert compare_dictionary_arrays(EXPECTED_STUDENT_LIST, student_list_data)

if __name__ == '__main__':
    pytest.main()
