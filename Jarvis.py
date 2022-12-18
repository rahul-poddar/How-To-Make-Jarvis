from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from JarvisUi import Ui_MainWindow
import sys
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        def TakeCommand():

            r = sr.Recognizer()

            with sr.Microphone() as source:

                print(": Listening....")

                r.pause_threshold = 1

                audio = r.listen(source)


            try:

                print(": Recognizing...")

                query = r.recognize_google(audio,language='en-in')

                print(f": Your Command : {query}\n")

            except:
                return ""

            return query.lower()

        def Pass(pass_inp):

               password = "rahul"

               passss  = str(password)

               if passss==str(pass_inp):

                      Speak("Access Granted .")

                      import Main
                      Main.TaskExe()

               else:
                      Speak("Access Not Granted .")

        if __name__ == "__main__" :

               Speak("This Particular File Is Password Protected .")

               Speak("Kindly Provide The Password To Access .")

               passssssss = TakeCommand()

               Pass(passssssss)

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.jarvis_ui = Ui_MainWindow()
        
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.jarvis_ui.movies = QtGui.QMovie("S:\\AI Jarvis\\G.U.I Material\\B.G\\Iron_Template_1.gif")

        self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)

        self.jarvis_ui.movies.start()



        self.jarvis_ui.movies_2 = QtGui.QMovie("S:\\AI Jarvis\\G.U.I Material\\VoiceReg\\jarvis_jj.gif")

        self.jarvis_ui.Gif_2.setMovie(self.jarvis_ui.movies_2)

        self.jarvis_ui.movies_2.start()


        self.jarvis_ui.movies_3 = QtGui.QMovie("S:\\AI Jarvis\\G.U.I Material\\ExtraGui\\initial.gif")

        self.jarvis_ui.Gif_3.setMovie(self.jarvis_ui.movies_3)

        self.jarvis_ui.movies_3.start()


        self.jarvis_ui.movies_4 = QtGui.QMovie("S:\\AI Jarvis\\G.U.I Material\\ExtraGui\\Code_Template.gif")

        self.jarvis_ui.Gif_4.setMovie(self.jarvis_ui.movies_4)

        self.jarvis_ui.movies_4.start()



        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):
        
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time 

        self.jarvis_ui.textBrowser.setText(labbel)

Gui_App = QApplication(sys.argv)

Gui_Jarvis = Gui_Start()

Gui_Jarvis.show()

exit(Gui_App.exec_())
