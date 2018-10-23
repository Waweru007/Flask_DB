import peewee
from flask import Flask, render_template,request, redirect, url_for

from db import Student

app = Flask(__name__)


@app.route('/')
def home():
    students=Student.select()
    return render_template("users_table.html", students=students)

@app.route('/add')
def adding_students():
     return  render_template("form.html")

@app.route('/save', methods=["POST"])
def save():
     email_adress= request.form["email_adress"]
     dob=request.form["dob"]
     course=request.form["course"]
     names=request.form["names"]
     gender=request.form["gender"]
     country=request.form["country"]
     try:
        Student.create(email_adress=email_adress, dob=dob, course=course, names= names, gender=gender, country=country)
     except  peewee.IntegrityError:
         return "Record alreasdy exists"
     return  render_template("form.html")

@app.route('/delete/<int:id>')
def deleting_students(id):
    s = Student.get(Student.id==id)
    s.delete_instance()
    return  redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5001)
