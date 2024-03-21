import tkinter as tk
from gpiozero import LED, Button
from time import sleep

class Seg7():
    def showNumber(self, numberToShow):
        if numberToShow in self._numbers.keys():
            self._numberToShow = self._numbers[numberToShow]
        else:
            self._numberToShow = self._numbers["E"]
            
        for i in range(8):
            self._pins[i].value = self._numberToShow[i]

    def __init__(self):
        self._numbers = {
            # L F E D
            "L": [0, 0, 0, 1, 1, 1, 0, 0],
            1: [0, 1, 1, 0, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1, 0],
            "H": [0, 1, 1, 0, 1, 1, 1, 0],
            "E": [1, 1, 0, 0, 1, 1, 1, 0],
        }
        
        self._pins = [LED(14), LED(15), LED(18), LED(2), LED(3), LED(17), LED(27), LED(22)]

class Valve():
    def __init__(self):
        self._valve_green = LED(5)
        self._valve_red = LED(6)
    
    def remplissage(self):
        self._valve_green.on()
        self._valve_red.off()
    
    def purge(self):
        self._valve_green.off()
        self._valve_red.on()

class Cuve():
    def __init__(self, master):
        self._seg7 = Seg7()
        self._valve = Valve()
        
        # Création des boutons tkinter
        self._button_L = Button(master, text="L", pull_up=True, command=self.cap00)
        self._button_1 = Button(master, text="1", pull_up=True, command=self.cap01)
        self._button_2 = Button(master, text="2", pull_up=True, command=self.cap02)
        self._button_H = Button(master, text="H", pull_up=True, command=self.cap03)

        # Placement des boutons tkinter
        self._button_L.grid(row=0, column=0)
        self._button_1.grid(row=0, column=1)
        self._button_2.grid(row=0, column=2)
        self._button_H.grid(row=0, column=3)

    def cap00(self):
        self._seg7.showNumber("L")
        self._valve.remplissage()
        print("Button L pressed so remplissage")
    
    def cap01(self):
        self._seg7.showNumber(1)
        self._valve.remplissage()
        print("Button 1 pressed so remplissage")

    def cap02(self):
        self._seg7.showNumber(2)
        self._valve.remplissage()
        print("Button 2 pressed so remplissage")

    def cap03(self):
        self._seg7.showNumber("H")
        self._valve.purge()
        print("Button H pressed so Purge")

def main():
    # Création de la fenêtre Tkinter
    window = tk.Tk()
    window.title("Cuve")
    window.geometry("800x600")
    
    # Instanciation de la cuve dans la fenêtre
    cuve = Cuve(window)
    
    # Affichage de la fenêtre Tkinter
    window.mainloop()

if __name__ == "__main__":
    main()
