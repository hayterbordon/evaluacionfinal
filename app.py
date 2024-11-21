from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ''
    total_sin_descuento = 0
    total_con_descuento = 0
    descuento_en_precio = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_en_precio = int(total_sin_descuento * descuento)
        total_con_descuento = total_sin_descuento - descuento_en_precio

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        total_con_descuento=total_con_descuento,
        descuento_en_precio=descuento_en_precio
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    mensaje = ''

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre in usuarios and usuarios[nombre] == contraseña:
            if nombre == "juan":
                mensaje = f"Bienvenido administrador {nombre}"
            elif nombre == "pepe":
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
