from flask import Flask, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student to database"""

    return render_template("student_add_form.html")

@app.route("/student-add-confirmation", methods=['POST'])
def student_add_confirmation():
    """Student add confirmation page"""
    
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(fname, lname, github)


    return render_template("student_add_confirmation.html",
                            first_name = fname,
                            last_name = lname,
                            github = github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
