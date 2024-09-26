from bottle import template
import time

class Application:

    def __init__(self):
        self.pages = {
        'index': self.index
        }


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.index)
        if not parameter:
            print(f'Acessando content({parameter})')
            return content()
        else:
            print(f'Tentando... content(self,{parameter})')
            return content(parameter)


    def index(self):
        print('Entrando na index.')
        return template('app/views/html/index', version=str(int(time.time())))
