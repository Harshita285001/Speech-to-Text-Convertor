# Importing required Modules
from tkinter import *
from tkinter.messagebox import showinfo
import speech_recognition as sr



def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')

    st = Label(speechtotextwindow, text='Speech-to-Text', font=("Times", 20, "bold"), bg='IndianRed')
    st.place(x=160, y=30)

    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=110, y=150)
    
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=230, y=100)

title = Label(mainwindow, text="Speech to Text Conversion", font=("Times", 30, "bold"))
title.place(x=62, y=50)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='brown', command=SpeechToText)
speechtotextbutton.place(x=125, y=150)

