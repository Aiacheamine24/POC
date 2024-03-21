import tkinter as tk
from tkinter import ttk, Label, Entry, Button, StringVar
from time import sleep
from gpiozero import LED


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My App")
        self.geometry("400x200")

        self.seg7 = Seg7()
        self.seg7.showNumber(0)


        # Set 2 Columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # First Column setup 2 Sub-Columns and 2 Rows
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Inside First Column set 4 Buttons in each Sub-Column
        self.z01Status = False
        self.z01 = Button(self, text="Zone 01", command=self.pressZone01)
        self.z01.grid(row=0, column=0, sticky="nsew")

        self.z02Status = False
        self.z02 = Button(self, text="Zone 02", command=self.pressZone02)
        self.z02.grid(row=1, column=0, sticky="nsew")

        self.z03Status = False
        self.z03 = Button(self, text="Zone 03", command=self.pressZone03)
        self.z03.grid(row=0, column=1, sticky="nsew")

        self.z04Status = False
        self.z04 = Button(self, text="Zone 04", command=self.pressZone04)
        self.z04.grid(row=1, column=1, sticky="nsew")

        # Add here 2 labels and 2 entries
        self.label1 = Label(self, text="Status")
        self.label1.grid(row=2, column=0, sticky="nsew")

        self.statusOfSystem = "off"

        self.statusSystem = Label(self, text=self.statusOfSystem)
        self.statusSystem.grid(row=2, column=1, sticky="nsew")

        # Second Column setup 3 Rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Inside Second Column set 3 Buttons
        self.activate = Button(self, text="Activate", command=self.pressActivate)
        self.activate.grid(row=0, column=2, sticky="nsew")

        self.deactivate = Button(self, text="Deactivate", command=self.pressDeactivate)
        self.deactivate.grid(row=1, column=2, sticky="nsew")

        self.reset = Button(self, text="Reset", command=self.pressReset)
        self.reset.grid(row=2, column=2, sticky="nsew")

    def pressActivate(self):
        # Change the status of the system
        self.statusOfSystem = "on"
        # show the new status
        self.statusSystem.config(text=self.statusOfSystem)
        # change the color of the button
        self.activate.config(bg="green")
        self.deactivate.config(bg="red")
        self.reset.config(bg="yellow")

        # Set the status of the zones to "off"
        self.z01.config(bg="red")
        self.z02.config(bg="red")
        self.z03.config(bg="red")
        self.z04.config(bg="red")

        self.z01Status = False
        self.z02Status = False
        self.z03Status = False
        self.z04Status = False
        
    def pressDeactivate(self):
        # Change the status of the system
        self.statusOfSystem = "off"
        # show the new status
        self.statusSystem.config(text=self.statusOfSystem)
        # change the color of the button
        self.activate.config(bg="red")
        self.deactivate.config(bg="green")
        self.reset.config(bg="yellow")

        # Set the status of the zones to "off"
        self.z01.config(bg="red")
        self.z02.config(bg="red")
        self.z03.config(bg="red")
        self.z04.config(bg="red")

        self.z01Status = False
        self.z02Status = False
        self.z03Status = False
        self.z04Status = False

    def pressReset(self):
        # Change the status of the system
        self.statusOfSystem = "off"
        # show the new status
        self.statusSystem.config(text=self.statusOfSystem)
        # change the color of the button
        self.activate.config(bg="white")
        self.deactivate.config(bg="white")
        self.reset.config(bg="white")

        # Set the status of the zones to "off"
        self.z01.config(bg="white")
        self.z02.config(bg="white")
        self.z03.config(bg="white")
        self.z04.config(bg="white")

        self.z01Status = False
        self.z02Status = False
        self.z03Status = False
        self.z04Status = False

    def pressZone01(self):
        # Set the status of the zone to "on"
        if self.statusOfSystem == "on":
            self.z01Status = not self.z01Status
            self.z01.config(bg="green" if self.z01Status else "red")
            self.seg7.showNumber(1)
    def pressZone02(self):
        if self.statusOfSystem == "on":
            self.z02Status = not self.z02Status
            self.z02.config(bg="green" if self.z02Status else "red")
            self.seg7.showNumber(2)

    def pressZone03(self):
        if self.statusOfSystem == "on":
            self.z03Status = not self.z03Status
            self.z03.config(bg="green" if self.z03Status else "red")
            self.seg7.showNumber(3)

    def pressZone04(self):
        if self.statusOfSystem == "on":
            self.z04Status = not self.z04Status
            self.z04.config(bg="green" if self.z04Status else "red")
            self.seg7.showNumber(4)
    
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
            0: [1, 1, 1, 1, 1, 1, 0, 0],
            1: [0, 1, 1, 0, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1, 0],
            3: [1, 1, 1, 1, 0, 0, 1, 0],
            4: [0, 1, 1, 0, 0, 1, 1, 0],
            "E": [1, 0, 0, 1, 1, 1, 1, 0],
        }
        
        self._pins = [LED(14), LED(15), LED(18), LED(2), LED(3), LED(17), LED(27), LED(22)]


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

