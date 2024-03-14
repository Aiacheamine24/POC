import tkinter as tk
import gpiozero as gz
from time import sleep

class Seg7():
    def showNumber(self, numberToShow):
        if numberToShow in self._numbers.keys():
            self._numberToShow = self._numbers[numberToShow]
        else:
            self._numberToShow = self._numbers["E"]
            
        for i in range(7):
            self._pins[i].value = self._numberToShow[i]

    def __init__(self):
        self._numbers = {
            # L F E D
            "L": [0, 0, 0, 1, 1, 1, 0],
            1: [0, 1, 1, 0, 0, 0, 0],
            2: [1, 1, 0, 0, 1, 0, 1],
            "H": [0, 1, 1, 0, 1, 1, 1],
            "E": [1, 1, 0, 0, 1, 1, 1],
        }
        
        self._pins = [gz.LED(17), gz.LED(2), gz.LED(3), gz.LED(4), gz.LED(5), gz.LED(6), gz.LED(7)]

class Valve():
    def __init__(self):
        self._valve_green = gz.LED(8)
        self._valve_red = gz.LED(9)
    
    def remplissage(self):
        self._valve_green.on()
        self._valve_red.off()
    
    def purge(self):
        self._valve_green.off()
        self._valve_red.on()

class Cuve():
    def __init__(self):
        self._seg7 = Seg7()
        self._valve = Valve()
        self._cap00 = gz.Button(10)
        self._cap01 = gz.Button(11)
        self._cap02 = gz.Button(12)
        self._cap03 = gz.Button(13)

        # Configuration des fonctions de rappel pour les boutons
        self._cap00.when_pressed = self.cap00
        self._cap01.when_pressed = self.cap01
        self._cap02.when_pressed = self.cap02
        self._cap03.when_pressed = self.cap03

    def cap00(self):
        self._seg7.showNumber("L")
        self._valve.remplissage()
        print("cap00 pressed so remplissage")
    
    def cap01(self):
        self._seg7.showNumber(1)
        self._valve.purge()
        print("cap01 pressed so remplissage")

    def cap02(self):
        self._seg7.showNumber(2)
        self._valve.remplissage()
        print("cap02 pressed so remplissage")

    def cap03(self):
        self._seg7.showNumber("H")
        self._valve.purge()
        print("cap03 pressed so remplissage")

def main():
    # Instanciation de la cuve et des capteurs
    cuve = Cuve()
    # Création de la fenêtre
    window = tk.Tk()
    window.title("Cuve")
    window.geometry("800x600")
    # Affichage de la fenêtre
    window.mainloop()

if __name__ == "__main__":
    main()
