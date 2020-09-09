"""
Created on Wednesday April 22 16:53:34 2020

@author: nkalyan🤠
        Implementing student repository database and getting result through web. 
"""


from flask import Flask, render_template
import sqlite3
from typing import Dict, List, Any

app: Flask = Flask(__name__)
"""Take the name from here"""
db_file: str = "/Users/nikhilkalyan/810_startup.db"


@app.route("/completed_cours")            # decorator the used to route the web address
def completed_course() -> str:
    """Method that checks exceptions and execute query to connect database table"""
    try:
        """Check for exceptions"""
        db: sqlite3.Connection = sqlite3.connect(db_file)
        query: str = "SELECT s.Name, s.CWID, g.Courses, g.Grade, i.Name AS 'Instructor' " \
                     "FROM Grades g JOIN students s ON g.StudentCWID = s.CWID " \
                     "JOIN Instructor i ON g.InstructorCWID = i.CWID ORDER BY s.Name"
    except sqlite3.OperationalError as v:
        print(v)
    else:
        """If no exception found the this operation performs"""
        data: List[Dict[str, Any]] = \
            [{"name": name, "cwid": cwid, "course": course, "grade": grade, "instructor": instructor}
             for name, cwid, course, grade, instructor in db.execute(query)]
        db.close()
        """The render template is going to render all items from template"""
        return render_template("student_courses.html",
                               title="Stevens Repository",
                               table_title="Student, Course, Grade and Instructor",
                               students=data)


if __name__ == '__main__':
    app.run(debug=True)
