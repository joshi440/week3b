from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register():
    return render_template("registration.html")

@app.route('/register', methods=['POST'])
def registration():
    student_name = request.form['student_name']
    return render_template(
        "registrationsuccess.html",
        student_name=student_name
    )

if __name__ == '__main__':
    app.run(debug=True)