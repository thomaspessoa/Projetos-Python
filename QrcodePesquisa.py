
import qrcode

                 # Pesquisa Pela Pagina 
                 
class PesPesquisa():
    dado = ''

    def inserirPesquisa(self,pesquisa):
        self.dado = str(pesquisa)
        img = qrcode.make("www.google.com/search?q=" + self.dado)
        img.show()


class PesYoutube():
    dadoYoutube = ''

    def inserirYoutube(self,pesquisa):
        self.dadoYoutube = str(pesquisa)
        img = qrcode.make("https://www.youtube.com/search?q=" + self.dadoYoutube)
        img.show()


class PesImagem():
    dadoImagem = ''

    def inserirImagem(self,pesquisa):
        self.dadoImagem = str(pesquisa)
        img = qrcode.make('https://www.google.com.br/search?q='+ self.dadoImagem +'&uact=5&sclient=img&tbm=isch&sa=X')
        img.show()


class PesSpotify():
    dadoSpotify = ''

    def inserirImagem(self,pesquisa):
        self.dadoSpotify = str(pesquisa)
        img = qrcode.make('https://open.spotify.com/search/ ' + self.dadoSpotify)
        img.show()

    