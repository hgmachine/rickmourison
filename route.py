from app.controllers.application import Application
from bottle import Bottle, route, run, request, redirect, template, static_file

import mimetypes

# Adicione o tipo MIME para arquivos MP4
mimetypes.add_type('video/mp4', '.mp4')

app = Bottle()
ctl = Application()

# Configuração para Português
app.config['default_locale'] = 'pt_BR'  # Defina o local para Português (Brasil)
app.config['charset'] = 'utf-8'  # Defina o conjunto de caracteres para lidar com decodificações em UTF-8

#-----------------------------------------------------------------------------
# Rotas:


# Arquivos estáticos:
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


# Rotas:
# sempre que acessar home o logout é automaticamente realizado
@app.route('/')
def index():
    return ctl.render('index')


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
