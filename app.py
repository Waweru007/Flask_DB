from flask import Flask, render_template

from db import Student

app = Flask(__name__)


@app.route('/')
def home():
    students=Student.select()
    return render_template("users_table.html", students=students)


if __name__ == '__main__':
    app.run(port=5001)
