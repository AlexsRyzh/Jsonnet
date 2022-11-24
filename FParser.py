from sly import Parser
from Flexer import FLexer


class FParser(Parser):
    tokens = FLexer.tokens


    parametr = {}
    timeparam = {}


    @_('"(" START terms ")"')
    def start(self,p):
        print(1)
        par = p.terms
        return par






    @_('empty')
    def terms(self,p):
        return {}

    @_('term terms')
    def terms(self,p):
        return p.term | p.terms






    @_('"(" str terms ")"')
    def term(self,p):
        return {
            p.str: p.terms
        }



    @_('"(" LIST ID list_items ")"')
    def term(self,p):
        return {
            p.ID: p.list_items
        }


    @_('empty')
    def list_items(self,p):
        return []

    @_('item list_items')
    def list_items(self,p):
        return [p.item] + p.list_items


    @_(' term ')
    def item(self,p):
        return p.term

    @_('"(" ITEM elem ")"')
    def item(self, p):
        return p.elem








    @_('"(" LET ID terms ")"')
    def term(self, p):
        if (p.ID in self.parametr):
            raise Exception(f"Повторное объяление переменной {p.ID} в строке {p.lineno}")
        self.parametr[p.ID] = {
            "value": p.terms,
            'time': 0
        }
        return {}

    @_('"(" str ID ")"')
    def term(self,p):
        print(p.ID)
        print(self.parametr.keys())
        if (p.ID in self.parametr):
            print(1)
            return {
                p.str: self.parametr[p.ID]['value']
            }
        else:
            raise Exception(f"Переменной {p.ID} не существует. Cтрока {p.lineno}")

    @_('"(" ID terms ")"')
    def term(self,p):
        if (p.ID in self.parametr):
            self.parametr[p.ID] = {
                "value": p.terms,
                'time': 0
            }
            return
        else:
            raise Exception(f"Переменной {p.ID} не существует. Cтрока {p.lineno}")




    @_('str')
    def elem(self, p):
        return p.str

    @_('INTEGER')
    def elem(self, p):
        return p.INTEGER


    @_('str')
    def terms(self,p):
        return p.str

    @_('INTEGER')
    def terms(self,p):
        return p.INTEGER







    @_('STRING')
    def str(self,p):
        return p.STRING[1:-1]

    @_('')
    def empty(self, expr):
        return {}




    @_('"(" FOR ID FROM INTEGER TO INTEGER terms ")"')
    def term(self,p):
        if not(p.ID in self.parametr):
            self.parametr[p.ID] = {
                'value': p.INTEGER0,
                'time': 1
            }
        list = []
        print(self.parametr.keys())
        for i in range(p.INTEGER0, p.INTEGER1):
            self.parametr[p.ID] = {
                'value': i,
                'time': 1
            }
            list.append(p.terms)


        print(self.parametr[p.ID]['value'])

        print(list)
        return
