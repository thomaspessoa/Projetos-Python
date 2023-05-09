import re

#Criando a Classe
class ExtratorURL():

    #Construtor
    def __init__(self,url):
        self.url = self.sanetizaURL(url)
        self.valida_URL()

    def sanetizaURL(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
        
    
    # Validação caso a URL esteja vazia
    def valida_URL(self):
        if not self.url:
            raise ValueError("A URL está vazia") # Informando o Error caso esteja vazia a URL
        
        padrao_URL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        validor = padrao_URL.match(self.url)
        if not validor:
            raise ValueError("URL não é valida !!")
        
    #Separação da base e o Parametro
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao] 
        return url_base

    # Parametros 
    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    # Valor Parametros
    def get_valor_parametros(self,parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)
    
#Executer      
extrator_URL = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_URL.get_valor_parametros("moedaDestino")
print("O Tamanho da URL é: ",len(extrator_URL))
print(valor_quantidade)
    

