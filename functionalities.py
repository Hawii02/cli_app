from seeds import mysession
from models import Teacher

def list_teachers():
    myteachers = mysession.query(Teacher).all()
    for teacher in myteachers:
        print(teacher.name)
def add_teacher():
    teacher_name = input("Enter Teachers name:")
    tr_id_no = input
    teacher = Teacher(name= teacher_name, id_no = tr_id_no)