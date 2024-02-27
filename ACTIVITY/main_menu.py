from tkinter import *
from class_grade import Grades
from cipher import Cipher
from folder.tayms2 import Tayms
from inventory import InventoryApp


class ViewMenu:
    def __init__(self, window):
        self.menu_frame = Frame(window)
        self.menu_frame.pack(fill=BOTH, expand=True)

        self.button_frame = Frame(self.menu_frame, padx=20, pady=10, relief=GROOVE, borderwidth=4)
        self.button_frame.place(anchor=CENTER, rely=0.5, relx=0.5)

        self.soft1_button = Button(self.button_frame, text='SOFTWARE 1', height=2, width=20, font='Lato 10 bold', command=lambda: self.toSoftware(1))
        self.soft1_button.grid(column=0, row=0, pady=10)

        self.soft2_button = Button(self.button_frame, text='SOFTWARE 2', height=2, width=20, font='Lato 10 bold', command=lambda: self.toSoftware(2))
        self.soft2_button.grid(column=0, row=1, pady=10)

        self.soft3_button = Button(self.button_frame, text='SOFTWARE 3', height=2, width=20, font='Lato 10 bold', command=lambda: self.toSoftware(3))
        self.soft3_button.grid(column=0, row=2, pady=10)

        self.soft4_button = Button(self.button_frame, text='SOFTWARE 4', height=2, width=20, font='Lato 10 bold', command=lambda: self.toSoftware(4))
        self.soft4_button.grid(column=0, row=3, pady=10)

        self.soft5_button = Button(self.button_frame, text='SOFTWARE 5', height=2, width=20, font='Lato 10 bold')
        self.soft5_button.grid(column=0, row=4, pady=10)

        self.quit_button = Button(self.button_frame, text='EXIT', height=2, width=20, font='Lato 10 bold', command=lambda: self.quitMenu())
        self.quit_button.grid(column=0, row=5, pady=10)

    def quitMenu(self):
        window.destroy()

    def toMenu(self):
        ViewMenu(window)

    def toSoftware(self, software):
        self.menu_frame.destroy()

        match software:
            case 1:
                window.title("Tayms X")
                Tayms(window, self.toMenu)

            case 2:
                window.title("Class Grage Averages")
                Grades(window, self.toMenu)

            case 3:
                window.title("Cipher")
                window.geometry("1300x480")
                Cipher(window, self.toMenu)

            case 4:
                window.title("Inventory")
                InventoryApp(window, self.toMenu)

window = Tk()

ViewMenu(window)
window.title("Main Menu")
window.state('normal')
window.geometry("640x480")
window.resizable(False, False)

window.mainloop()
