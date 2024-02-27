import tkinter as tk
from tkinter import messagebox

class Search:
    def __init__(self, root, func):
        self.func = func
        self.window = root

        self.main_frame = tk.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.result_frame = tk.Frame(self.main_frame)
        self.result_frame.pack(side=tk.TOP, pady=20)

        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(side=tk.TOP)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(side=tk.TOP)

        self.search_lbl = tk.Label(self.result_frame)
        self.search_lbl.pack(side=tk.TOP)

        self.input1_lbl = tk.Label(self.search_frame, text="Enter your name:")
        self.input1_lbl.grid(row=0, column=0)

        self.input1 = tk.Entry(self.search_frame)
        self.input1.grid(row=0, column=1)

        self.search_btn = tk.Button(self.button_frame, text="Search", command=self.search, width=10)
        self.search_btn.grid(row=0, column=0, pady=15, padx=(0, 5))

        self.quit_btn = tk.Button(self.button_frame, text="Quit", command=self.exit, width=10)
        self.quit_btn.grid(row=0, column=1, pady=15, padx=(5, 0))


    def search(self):
        name = self.input1.get()
        phone_number = ""
        with open('phone_numbers.txt', 'r') as file:
            for line in file:
                entry = line.strip().split(',')
                if entry[0].lower() == name.lower():
                    phone_number = entry[1]
                    break
        if phone_number:
            self.search_lbl.config(text=f"{name} phone number is: {phone_number}")
        else:
            messagebox.showinfo("Error", f"{name} has no record.")

    def exit(self):
        self.main_frame.destroy()
        self.window.geometry("640x480")
        self.window.title("Main Menu")
        self.func()

# def Pass():
#     pass
#
# root = tk.Tk()
# Search(root, Pass)
# root.title("Phone Number Finder")
# root.geometry("300x200")
# root.configure(bg='blue')
#
#
# root.mainloop()
