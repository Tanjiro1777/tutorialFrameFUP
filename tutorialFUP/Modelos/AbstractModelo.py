from abc import ABCMeta

class AbstractModelo(metaclass=ABCMeta):
    def init (self,data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
