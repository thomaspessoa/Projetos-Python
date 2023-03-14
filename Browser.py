from this import d
from PyQt5.QtWidgets import * 
import sys
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtCore import * 

#QMainWindow tem seu proprio Layout, na qual podemos adicionar barra de ferramentas 
class Navegador(QMainWindow):
    
    def go_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def go_you(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/'))
    
    def go_email(self):
        self.browser.setUrl(QUrl('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1667262756&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d1f48fab5-a0d6-1541-513e-7b413e0fd313&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015'))

    def go_linkedin(self):
        self.browser.setUrl(QUrl('https://www.linkedin.com/in/thomas-soares-pessoa-ab02bb209/'))

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,url):
        self.url_bar.setText(url.toString())

    def __init__(self):
        
        #Importando tudo da classe Mae que seria QMainWindow
        super(Navegador,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser) #Centralizando o Google 
        self.showMaximized()

        #Barra de Navegação 
        navbar = QToolBar()
        self.addToolBar(navbar)

        #Botoes de Voltar e Avançar 
        voltar_btn = QAction('<-', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)

        #Botao de Refresh
        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        #Botao Home
        home_btn = QAction('Inicio', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        #Botao Youtube 
        you_btn = QAction('Youtube',self)
        you_btn.triggered.connect(self.go_you) 
        navbar.addAction(you_btn)
        
        #Botao Email
        email_btn = QAction('Email',self)
        email_btn.triggered.connect(self.go_email)
        navbar.addAction(email_btn)

        #Botao Linkedin 
        linkedin_btn = QAction('Linkedin',self)
        linkedin_btn.triggered.connect(self.go_linkedin)
        navbar.addAction(linkedin_btn)

        #Botao Seguir
        seguir_btn = QAction('->',self)
        seguir_btn.triggered.connect(self.browser.forward)
        navbar.addAction(seguir_btn)


        #Barra de Endereço
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)  # ter a barra de Url 
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url) # Para Atualizar a URL da pagina onde estou acessando







#triggered Procedimento de Armazenamento
# QAction podem ser adicionadas a menus e barras de ferramentas e as manterão sincronizadas automaticamente