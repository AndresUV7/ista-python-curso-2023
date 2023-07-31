import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_student_list_ascending_order_from_database():
    response = (supabase.table("estudiante")
                .select("*")
                .order('primer_apellido')
                .order('segundo_apellido')
                .order('primer_nombre')
                .order('segundo_nombre')
                .execute())
    return response.data

student_list_ascending_order_from_database = get_student_list_ascending_order_from_database()

def get_student_total_attendance_by_course_from_database(cedula, materia):
    response = (supabase.table("asistencia")
                .select('*', count= "exact")
                .eq("cedula", cedula)
                .eq("materia", materia)
                .execute())
    return response.count

def create_student_attendance_record_in_database(attendance_record):
    response = (supabase.table("asistencia")
                .insert(attendance_record)
                .execute())
    return response
