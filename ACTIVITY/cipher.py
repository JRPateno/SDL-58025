from tkinter import *

class Cipher:
    def __init__(self, window, func):
        self.window = window
        self.func = func
        self.keyshift = 1

        self.window.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        self.main_frame = Frame(window, bg='blue')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.everything_frame = Frame(self.main_frame, bg='yellow')
        self.everything_frame.pack(side=TOP)

        self.text_frame = Frame(self.everything_frame)
        self.text_frame.pack(side=TOP)

        self.textInput_frame = Frame(self.text_frame, bg='white', relief=GROOVE, borderwidth=5)
        self.textInput_frame.grid(row=0, column=0)

        self.shift_frame = Frame(self.text_frame, bg='white', relief=GROOVE, borderwidth=5)
        self.shift_frame.grid(row=0, column=1, padx=20)

        self.textResult_frame = Frame(self.text_frame, bg='white', relief=GROOVE, borderwidth=5)
        self.textResult_frame.grid(row=0, column=2)

        self.button_shift_frame = Frame(self.shift_frame,  bg='white')
        self.button_shift_frame.pack(side=TOP, pady=(30,15), padx=30)

        self.menuButton_shift_frame = Frame(self.shift_frame, bg='green')
        self.menuButton_shift_frame.pack(side=TOP, pady=(15,30), padx=30)




        #AHSDASD
        self.inputbar = Text(self.textInput_frame, font='Lato 12', width=50, relief=FLAT)
        self.inputbar.pack(side=LEFT, padx=10, pady=10)
        self.inputbar.bind('<KeyRelease>', lambda event: self.code())

        self.resultbar = Text(self.textResult_frame, font='Lato 12', width=50, relief=FLAT)
        self.resultbar.pack(side=LEFT, padx=10, pady=10)

        #
        self.minus_button = Button(self.button_shift_frame, text='-', command=lambda: self.shift(1), width=2, height=3)
        self.minus_button.pack(side=LEFT)

        self.label = Label(self.button_shift_frame, font='Lato 10 bold', text=f'Shift: {self.keyshift}', width=10, height=3, relief=RAISED, borderwidth=2)
        self.label.pack(side=LEFT, padx=10, ipadx=2, ipady=1)

        self.plus_button = Button(self.button_shift_frame, text='+', command=lambda: self.shift(2), width=2, height=3)
        self.plus_button.pack(side=LEFT)

        self.toMenu = Button(self.menuButton_shift_frame, text='QUIT', font='Lato 10 bold', command=lambda: self.exit(), width=10, height=1)
        self.toMenu.pack(side=TOP)


    def code(self):
        text = self.inputbar.get(0.0, END)

        newlist = []

        for i in range(len(text)):
            char = text[i]

            if char.isalpha():
                if char.isupper():
                    codes = chr((ord(char) + self.keyshift -65) % 26 + 65)
                    newlist.append(codes)

                elif char.islower():
                    codes = chr((ord(char) + self.keyshift - 97) % 26 + 97)
                    newlist.append(codes)

            else:
                newlist.append(char)

        string = ''.join(newlist)

        self.resultbar.configure(state="normal")
        self.resultbar.delete(1.0, "end-1c")
        self.resultbar.insert(1.0, string)
        self.resultbar.configure(state="disabled")

    def shift(self, operation):
        match operation:
            case 1:
                self.keyshift -= 1
            case 2:
                self.keyshift += 1

        self.label.configure(text=f'Shift: {self.keyshift}')
        self.code()

    def exit(self):
        self.main_frame.destroy()
        self.window.geometry("640x480")
        self.window.title("Main Menu")
        self.func()

# window = Tk()
#
# def Pass():
#     pass
#
# Cipher(window, Pass())
# window.title("Cipher Encoder")
# window.state('zoomed')
# window.mainloop()
