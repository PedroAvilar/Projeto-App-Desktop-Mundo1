from banco_de_dados import Sistemas

class Sistema:

    def setCodigoSistema (self, codigo_sistema):
        self.codigo_sistema = codigo_sistema
    
    def getCodigoSistema (self):
        return self.codigo_sistema
    
    def setNomeSistema (self, nome_sistema):
        self.nome_sistema = nome_sistema
    
    def getNomeSistema (self):
        return self.nome_sistema
    