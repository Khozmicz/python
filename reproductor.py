from pygame import mixer
class Reproductor:
    archivo=None

    def __init__ (self,archivo):
        self.archivo=archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música ha sido pausada"
    
    def unpause(self):
        mixer.music.unpause()
        return "Continuando reproducción"
    
    def stop(self):
        mixer.music.stop()
        return "La música se detuvo"
    
    def volume(self,v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a {}".format(v)

if __name__== "__main__":
    file="wefere.mp3"
    musica=Reproductor(file)
   
    while True:
        print("1-Play ▶️ | 2-Pause ⏸️ | 3-Stop ⏹️ | 4-Continuar | 5-Volumen 🔈 | 6-Salir ❌")
        accion=int(input("Opción: "))
        if accion==1:
            resp=musica.play()
        elif accion==2:
            resp=musica.pause()
        elif accion==3:
            resp=musica.stop()
        elif accion==4:
            resp=musica.unpause()
        elif accion==5:
            nuevo_volumen=float(input("Introduzca el nuevo volumen (0-100): "))
            nuevo_volumen=nuevo_volumen/100
            resp=musica.volume(nuevo_volumen)
        elif accion==6:
            print("Saliendo del reproductor")
            break
        else:
            resp="Opción no existente"
    
        print(resp)