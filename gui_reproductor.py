from reproductor import *
from tkinter import *

musica=Reproductor("wefere.mp3")
resp=""

def play_musica():
    resp=musica.play()

def pause_musica():
    resp=musica.pause()
    
master=Tk()
master.geometry("200x200")
master.title("Reproductor de windows")


etiqueta=Label(master,text="DJ")
etiqueta.pack(pady=5)

btn_play=Button(master, text="Play", command= play_musica)
btn_play.pack(pady=10)

btn_play=Button(master, text="Pause", command= pause_musica)
btn_play.pack(pady=10)


mainloop()