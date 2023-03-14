import speech_recognition as sr # Reconhecimento de fala 
import pyttsx3 # Biblioteca para conversao de texto
import datetime
import wikipedia
import pywhatkit # Biblioteca para envio de mensagens 

class Assistente():

    def __init__(self):
        self.audio = sr.Recognizer()  # Vai reconhecer o audio 
        self.reproducao = pyttsx3.init()
        self.reproducao.say('Olá sou a Sofia, como posso Ajudar ?? ')
        self.reproducao.runAndWait()

    def executar_Comando(self):
        try:
            
            with sr.Microphone() as source:
                print('Ouvindo... ')
                voz = self.audio.listen(source) # Vai receber o Audio 

                #Comando de voz 
                self.comando = self.audio.recognize_google(voz,language='pt-BR')
                self.comando = self.comando.lower()

                #Vai reconhecer pelo nome dado, vai reconhcer no comando
                if 'sofia' in self.comando:
                    self.comando = self.comando.replace('sofia' , '')
                    self.reproducao.say(self.comando)
                    self.reproducao.runAndWait()

        except:
            print('Problema no seu Microfone !! ')  
        return self.comando

    def comando_voz_usuario (self):
        self.comando = self.executar_Comando()
        if 'horas' in self.comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            print(hora)
            self.reproducao.say('Agora é exatamente ' + hora)
            self.reproducao.runAndWait()
        
        #Comando quando quiser buscar por alguma coisa 
        elif 'procurar por ' in self.comando:
            self.procurar = self.comando.replace('procurar por', '')
            wikipedia.set_lang('pt')
            self.resultado = wikipedia.summary(self.procurar,1) # 2 referente a duas linhas que vai reproduzir do sumario
            print(self.resultado) 
            self.reproducao.say(self.resultado)
            self.reproducao.runAndWait()

        elif 'toque' in self.comando:
            musica = self.comando.replace('toque', '')
            self.resultado = pywhatkit.playonyt(musica)
            self.reproducao.say('Reproduzindo  ')
            self.reproducao.runAndWait()          