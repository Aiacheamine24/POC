import tkinter as tk
from gpiozero import LED

class Seg:
    def __init__(self):
        self.segments = {
            "L": [1, 1, 1, 1, 1, 1, 0],
            "1": [0, 0, 1, 1, 0, 0, 0],
            "2": [1, 1, 0, 1, 1, 0, 1],
            "H": [0, 1, 1, 0, 1, 1, 1],
        }
        self.led_pins = [21, 20, 16, 12, 7, 8, 25]  # GPIO pins for LED segments
        self.leds = [LED(pin) for pin in self.led_pins]

    def show(self, number):
        if number in self.segments:
            for i, value in enumerate(self.segments[number]):
                self.leds[i].value = value
            print("Affichage segment:", self.segments[number])
        else:
            print("Nombre invalide")

class Cuve:
    def vidange(self):
        print("Vidange de la cuve")

class Capteurs:
    def __init__(self, segment, cuve):
        self.segment = segment
        self.cuve = cuve

    def update_cuve(self, niveau):
        self.segment.show(niveau)
        if niveau == "L":
            self.cuve.vidange()

def main():
    root = tk.Tk()
    root.title("Système de Contrôle de Niveau")

    segment = Seg()
    cuve = Cuve()
    capteurs = Capteurs(segment, cuve)

    button_frame = tk.Frame(root)
    button_frame.pack()

    niveaux = ["L", "1", "2", "H"]

    buttons = []
    for niveau in niveaux:
        button = tk.Button(button_frame, text=f"Niveau {niveau}", command=lambda n=niveau: capteurs.update_cuve(n), bg="red")
        button.pack(side="left")
        buttons.append(button)

    btn_quit = tk.Button(button_frame, text="Quitter", command=root.quit)
    btn_quit.pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
