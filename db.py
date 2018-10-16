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


Student.create_table(fail_silently=True)