from flask import Flask, render_template, request, redirect
from models import Patient, ClinicQueue

app = Flask(__name__)

clinic = ClinicQueue()


@app.route('/')
def home():
    patients = clinic.get_all_patients()
    return render_template('index.html', patients=patients, total=clinic.total_served)


@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        patient = Patient(name)
        clinic.add_patient(patient)
        return redirect('/')
    return render_template('add.html')


@app.route('/serve')
def serve():
    clinic.serve_patient()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/')
def home():
    return render_template('index.html', patients=clinic.patients)


@app.route('/delete/<int:index>')
def delete_patient(index):
    if 0 <= index < len(clinic.patients):
        clinic.patients.pop(index)
    return redirect('/')