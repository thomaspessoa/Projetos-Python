import qrcode

                #ABRIR DIRETO NA PAGINA 

class OpenPesquisa():
    def __init__(self):
        self.opendado = ''

    def qrPesquisa(self):
        self.opendado = "www.google.com"
        img = qrcode.make(self.opendado)
        img.show()

class OpenYoutube():
    def __init__(self):
        self.openYou = ''

    def qrYoutube(self):
        self.openYou = "https://www.youtube.com/"
        img = qrcode.make(self.openYou)
        img.show()

class OpenSpotify():
    def __init__(self):
        self.openSpotify = ''

    def qrSpotify(self):
        self.openSpotify = 'https://open.spotify.com/'
        img = qrcode.make(self.openSpotify)      
        img.show()

class Email():
    def __init__(self):
        self.dadoEmail = ''

    def openEmail(self):
        self.dadoEmail = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1665021456&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3de2b59a1f-313a-065d-8102-9e7883fdd880&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015'
        img = qrcode.make(self.dadoEmail)
        img.show()