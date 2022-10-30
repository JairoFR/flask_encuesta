from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = '4511vs5d1v56sv51a' # establece una clave secreta

lenguajes={
    '1': 'Python',
    '2': 'C#',
    '3': 'Javascript',
    '4': 'C++',
    '5': 'PHP'
}

ciudades={
    '1': 'New York',
    '2': 'Santiago',
    '3': 'California',
    '4': 'Sicilon Valley',
    '5': 'Sidney'
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])    
def procesado():
    
    session['name'] = request.form['nombre']
    session['location'] = ciudades[request.form['ubicacion']]
    session['favorite'] = lenguajes[request.form['favorito']]
    session['comentary'] = request.form['comentario']
    return redirect('/resultados')

@app.route('/resultados')
def resultados():
    return render_template("informacion.html")


if __name__ == "__main__":
    app.run(debug=True)

