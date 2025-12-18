from app import criar_app
from app import registrar_blueprints

app = criar_app()

if __name__== "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)