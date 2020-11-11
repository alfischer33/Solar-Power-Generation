from flask import Flask, render_template, url_for, request, redirect
from model import predict

app = Flask(__name__)

#define app route on initial run
@app.route('/', methods=['POST', 'GET'])
def index():
    
    try:
        ambient
    except NameError:
        ambient = 25
        module = 30
        irradiation = 0.25
        prediction = 3363
    
        prediction = int(predict(float(ambient), float(module), float(irradiation)))

    return render_template('index.html', ambient=ambient, module=module, irradiation=irradiation, prediction=prediction)

#define app route for adjusted sliders or manually entered parameters
@app.route('/<int:ambient>/<int:module>/<float:irradiation>', methods=['POST', 'GET'])
def index2(ambient, module, irradiation):

    prediction = int(predict(float(ambient), float(module), float(irradiation)))

    if request.method == "POST":
        if request.form['ambient'] != '':
            ambient = request.form['ambient']
        if request.form['module'] != '':
            module = request.form['module']
        if request.form['irradiation'] != '':
            irradiation = request.form['irradiation']
        prediction = int(predict(float(ambient), float(module), float(irradiation)))

    return render_template('index.html', ambient=ambient, module=module, irradiation=irradiation, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)