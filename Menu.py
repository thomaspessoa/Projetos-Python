
from ast import Return
from QrcodePesquisa import *
from QrcodeOpen import *
import PySimpleGUI as sg
from Assistente_Virtual import * 
from Browser import * 


class Menu():

    def __init__(self):
        pass

    def menuAcesso(self,parametro):


        if parametro =='1':
            openpes = OpenPesquisa()
            openpes.qrPesquisa()

        elif parametro == '2':
            openYou = OpenYoutube()
            openYou.qrYoutube()

        elif parametro == '3':
            openSpoti = OpenSpotify()
            openSpoti.qrSpotify()

        elif parametro == '4':
            eemail = Email()
            eemail.openEmail()

# __________________________________________________________________________


class MenuPesquisa(PesPesquisa):

    def __init__(self):
        pass

    def menuPesquisa(self, parametro, pesquisas):

        self.opcaoPesquisa = 0

            # pesquisa google
        if parametro == "1":
            pesquisa = PesPesquisa()
            pesquisa.inserirPesquisa(pesquisas)

            # pesquisa youtube
        elif parametro == "2":
            print('')
            youtube = PesYoutube()
            youtube.inserirYoutube(pesquisas)

            # pesquisa imagem
        elif parametro == "3":
            print('')
            imagem = PesImagem()
            imagem.inserirImagem(pesquisas)

            # pesquisa Spotify
        elif parametro == "4":
            print('')
            spotify = PesSpotify()
            spotify.inserirImagem(pesquisas)

            # Saida
        else:
            print('Voce Saiu ! ')
            print("Até Logo ")

# __________________________________________________________________________

if __name__ == "__main__":
    abc = MenuPesquisa()
    dfg = Menu()    
    sg.theme("DarkPurple4")
    layout = [
        [sg.Text('MENU DE ACESSO ',font='Courier 12', text_color="yellow")],
        [sg.Text('')],
        [sg.Text(' 1 --->>> Menu Para Pesquisar ',font='Courier 12', text_color="yellow")],
        [sg.Text(' 2 --->>> Abrir direto do navegador por QRCODE',font='Courier 12', text_color="yellow")],
        [sg.Text(' 3 --->>> Assistente Virtual ',font='Courier 12', text_color="yellow")],
        [sg.Text(' 4 --->>> Abrir Browser Nock',font='Courier 12', text_color="yellow")],
        [sg.Text('Informe Sua Opção ', size=(18, 0),font='Courier 12', text_color="yellow"),
         sg.Input(size=(10, 0))],
        [sg.Button(' Enviar Dado ',font='Courier 12',button_color='#B8BC00'), sg.Button(' Sair ',font='Courier 12',button_color="Red")]
    ]

    layoutpes = [
    [sg.Text('MENU DE PESQUISA ')],
    [sg.Text('')],
    [sg.Text(' 1 --->>> Pesquisar pelo Google ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 2 --->>> Pesquisa pelo  Youtube ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 3 --->>> Pesquisa por Imagem ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 4 --->>> Pesquisa pelo   Spotify ',font='Courier 12', text_color="yellow")],
    [sg.Text('Informe Sua Opção ',size=(18,0),font='Courier 12', text_color="yellow"),sg.Input(size=(10,0))],
    [sg.Text('Sua Pesquisa aqui:  ',size=(18,0),font='Courier 12', text_color="yellow"),sg.Input(size=(24,0))],
    [sg.Button(' Enviar Dado ',font='Courier 12',button_color='#B8BC00'), sg.Button(' Voltar ',font='Courier 12',button_color='Red')]
    ]

    layoutopen = [
    [sg.Text('MENU NAVEGADOR ')],
    [sg.Text('')],
    [sg.Text(' 1 --->>> Abrir Google por  QRCODE ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 2 --->>> Abrir Youtube Por QRCODE ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 3 --->>> Abrir Spotify Por QRCODE ',font='Courier 12', text_color="yellow")],
    [sg.Text(' 4 --->>> Abrir Email por QRCODE ',font='Courier 12', text_color="yellow")],
    [sg.Text('Informe Sua Opção ',size=(18,0),font='Courier 12', text_color="yellow"),sg.Input(size=(10,0))],
    [sg.Button(' Enviar Dado ',font='Courier 12',button_color='#B8BC00'), sg.Button(' Voltar ',font='Courier 12',button_color='Red')]
    ]

    # Janela
    janela = sg.Window('Dados do Usuario ',layout, element_justification="c")

    event, values = janela.read()
    while True:
        event, values = janela.read()

        try:
            nome = values[0]

        except TypeError:
            # sg.popup("Tente Novamente ")
            break

        if event == ' Enviar Dado ':
            # sg.popup(values[0])

            if values[0] == "1":

                janelapes = sg.Window('Janla Pesquisa ',layoutpes,element_justification="c")
                while True: 
                    event, values = janelapes.read() 

                    try:
                        nome = values[0]
                        print(values[0])

                    except TypeError: 
                        # sg.popup("Tente Novamente ")
                        break 
                  
                    if event == ' Voltar ': 
                        janelapes.close() 

                    elif values[0] == '1':
                        abc.menuPesquisa(values[0], values[1])

                    elif values[0] == '2':
                        abc.menuPesquisa(values[0], values[1])
                    
                    elif values[0] == '3':
                        abc.menuPesquisa(values[0], values[1])

                    elif values[0] == '4':
                        abc.menuPesquisa(values[0], values[1])


            elif values[0] == "2":
                # dfg.menuAcesso()
                janelaopen = sg.Window('Janela Open ',layoutopen,element_justification="c")

                while True: 
                    event, values = janelaopen.read() 

                    try:
                        nome = values[0]
                        print(values[0])

                    except TypeError: 
                        # sg.popup("Tente Novamente ")
                        break 

                    if event == ' Voltar ': 
                        janelaopen.close()   

                    elif values[0] == '1': 
                        dfg.menuAcesso(values[0])

                    elif values[0] == '2': 
                        dfg.menuAcesso(values[0])

                    elif values[0] == '3': 
                        dfg.menuAcesso(values[0])

                    elif values[0] == '4': 
                        dfg.menuAcesso(values[0])


                #Assistente Virtual 
            elif values[0] == "3":
                abc = Assistente()
                abc.comando_voz_usuario()
                '''
                Palavras Chaves para a Assistente 

                horas 
                pesquise por 
                toque
                '''

            elif values[0] == "4":
                app = QApplication(sys.argv)

                        #Dando nome ao Browser
                QApplication.setApplicationName('Nock')

                        #Executando o Browser 
                windows = Navegador()

                app.exec()
        elif event == ' Sair ':
            janela.close()