from flask import Flask, render_template
import requests

app = Flask(__name__)

def obtener_preguntas():
    url = "https://backend-final1.onrender.com/api-auth/api/preguntas/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        preguntas = response.json()
        return [pregunta['texto_pregunta'] for pregunta in preguntas]
    except requests.exceptions.RequestException as e:
        print("Error al cargar las preguntas:", e)
        return None

@app.route('/')
def index():
    preguntas = obtener_preguntas()
    return render_template('preguntas.html', preguntas=preguntas)

if __name__ == '__main__':
    app.run(debug=True)
