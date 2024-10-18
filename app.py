from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal con el menú de opciones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de inscripción en curso
@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        # Aquí puedes procesar los datos o enviarlos a una base de datos
        return f'''<h1>Inscripción recibida: </h1 >{nombre} {apellidos} en el {curso} <br> <a href="/">Volver a inicio</a>'''
    return render_template('curso.html')

# Ruta para el formulario de registro de usuarios
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        return f"<h1>Usuario registrado: </h1>{nombre} {apellidos}, Email: {email} <br> <a href='/'>Volver a inicio</a>"
    return render_template('usuario.html')

# Ruta para el formulario de registro de productos
@app.route('/producto', methods=['GET', 'POST'])
def producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"<h1>Producto registrado: </h1>{producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}<br> <a href='/'>Volver a inicio</a>"
    return render_template('producto.html')

# Ruta para el formulario de registro de libros
@app.route('/libro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return f"<h1>Libro registrado: </h1>{titulo}, Autor: {autor}, Medio: {medio} <br> <a href='/'>Volver a inicio</a>"
    return render_template('libro.html')

if __name__ == '__main__':
    app.run(debug=True)
