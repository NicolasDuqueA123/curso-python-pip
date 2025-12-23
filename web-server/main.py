import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse # para retornar un HTML

app = FastAPI()

# @app.get se conoce como un decorador

@app.get('/')
def get_list():
    return [1,2,3]

# ejercicio 1 se mostraba en la web
# @app.get('/contact')
# def get_list():
#     return {"name": "Platzi"}

# Ejercicio 2, se renderiza una respuesta HTML y se ve HTML en el navegador
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()