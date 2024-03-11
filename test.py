import tkinter as tk
from gpiozero import LED, Button

class Valve:
    def __init__(self):
        self.state = "closed"

    def open(self):
        self.state = "open"

    def close(self):
        self.state = "closed"

class Seg:
    def __init__(self, affichage):
        self._numbers = {
            "L": [0, 0, 1, 1, 1, 0, 0],
            "0": [1, 1, 1, 1, 1, 1, 0],
            "1": [0, 1, 1, 0, 0, 0, 0],
            "2": [1, 1, 0, 1, 1, 0, 1],
            "H": [0, 1, 1, 1, 1, 1, 1],
        }
        self._affichage = self._numbers[affichage]
        self._leds = [LED(17), LED(27), LED(22), LED(5), LED(6), LED(13), LED(19), LED(26)]

    def show(self):
        for i in range(7):
            if self._affichage[i] == 1:
                self._leds[i].on()
            else:
                self._leds[i].off()

class Cuve:
    def __init__(self):
        self.valve_fill = Valve()
        self.valve_purge = Valve()

    def vidange(self):
        self.valve_fill.close()
        self.valve_purge.open()

class Capteurs:
    def __init__(self, segment, cuve):
        self.SEGMENT = segment
        self.CUVE = cuve
        self.cn0 = Button(5)
        self.cn1 = Button(6)
        self.cn2 = Button(13)
        self.cn3 = Button(19)
        self.cn0.when_pressed = self.on_press_capt0
        self.cn1.when_pressed = self.on_press_capt1
        self.cn2.when_pressed = self.on_press_capt2
        self.cn3.when_pressed = self.on_press_capt3
        self.statut_cn0 = False
        self.statut_cn1 = False
        self.statut_cn2 = False
        self.statut_cn3 = False

    def on_press_capt0(self):
        if self.cn0.is_pressed:
            self.statut_cn0 = True
            self.SEGMENT.show()
            if self.statut_cn0 and self.statut_cn1 and self.statut_cn2 and self.statut_cn3:
                self.CUVE.vidange()

    def on_press_capt1(self):
        if self.cn1.is_pressed:
            self.statut_cn1 = True
            self.SEGMENT.show()
            if self.statut_cn0 and self.statut_cn1 and self.statut_cn2 and self.statut_cn3:
                self.CUVE.vidange()

    def on_press_capt2(self):
        if self.cn2.is_pressed:
            self.statut_cn2 = True
            self.SEGMENT.show()
            if self.statut_cn0 and self.statut_cn1 and self.statut_cn2 and self.statut_cn3:
                self.CUVE.vidange()

    def on_press_capt3(self):
        if self.cn3.is_pressed:
            self.statut_cn3 = True
            self.SEGMENT.show()
            if self.statut_cn0 and self.statut_cn1 and self.statut_cn2 and self.statut_cn3:
                self.CUVE.vidange()

def main():
    root = tk.Tk()
    root.title("Système de Contrôle de Niveau")

    segment = Seg("L")
    cuve = Cuve()
    capteurs = Capteurs(segment, cuve)

    button_frame = tk.Frame(root)
    button_frame.pack()

    button_L = tk.Button(button_frame, text="Niveau L", command=lambda: update_display("L"), bg="red")
    button_0 = tk.Button(button_frame, text="Niveau 0", command=lambda: update_display("0"), bg="red")
    button_1 = tk.Button(button_frame, text="Niveau 1", command=lambda: update_display("1"), bg="red")
    button_2 = tk.Button(button_frame, text="Niveau 2", command=lambda: update_display("2"), bg="red")
    button_H = tk.Button(button_frame, text="Niveau H", command=lambda: update_display("H"), bg="red")
    button_quit = tk.Button(button_frame, text="Quitter", command=root.quit)

    button_L.pack(side="left")
    button_0.pack(side="left")
    button_1.pack(side="left")
    button_2.pack(side="left")
    button_H.pack(side="left")
    button_quit.pack(side="left")

    def update_display(niveau_liquide):
        if niveau_liquide in ["L", "0", "1", "2", "H"]:
            segment = Seg(niveau_liquide)
            segment.show()
            if niveau_liquide != "L":
                button = eval(f'button_{niveau_liquide}')
                button.config(bg="green")
        else:
            print("Niveau de liquide invalide")

    root.mainloop()

if __name__ == "__main__":
    main()
