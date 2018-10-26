from peewee import *

db=MySQLDatabase("school", host="localhost", user="root", password="")

class Student(Model):
    id=PrimaryKeyField()
    email_adress=CharField()
    dob=DateField()
    course=CharField()
    names=CharField()
    gender=CharField()
    country=CharField()
    class Meta:
        database=db
        db_table="students"

class Result(Model):
    id=PrimaryKeyField()
    student=ForeignKeyField(Student,related_name='student')
    name=CharField()
    maths=IntegerField()
    english=IntegerField()
    chemistry=IntegerField()
    date_done=DateField()
    class Meta:
        database=db
        db_table="results"


Student.create_table(fail_silently=True)

# r1= Result.get(Result.id==1)
# print(r1.name)
# print(r1.student.names)
# print(r1.student.course)
