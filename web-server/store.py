import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # ruta
    print(r.status_code) # estado de la web
    print(r.text) # respuesta de las categorias
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])