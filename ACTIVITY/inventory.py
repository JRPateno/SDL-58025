from tkinter import *

class InventoryApp:
    def __init__(self, window, func):
        self.window = window
        self.func = func

        self.inventory = {'Motherboards': 12,
                          'Hard Disk': 20,
                          'Diskette': 30,
                          'Compact Disk': 40,
                          'Memory Cards': 50
                          }

        self.main_frame = Frame(self.window, relief=GROOVE, borderwidth=4)
        self.main_frame.place(anchor=CENTER, rely=0.5, relx=0.5)

        self.inventory_frame = Frame(self.main_frame)
        self.inventory_frame.pack(side=TOP)

        self.inventory_label = Label(self.inventory_frame, text="Inventory:\n", font='Lato 12 bold',width=20)
        self.inventory_label.grid(row=0, column=0)

        self.output_label = Label(self.inventory_frame, justify=LEFT, font='Lato 12')
        self.output_label.grid(row=1, column=0, columnspan=4)

        #   QUANTITY
        self.quantity_frame = Frame(self.main_frame)
        self.quantity_frame.pack(side=TOP, pady=12)

        self.item_number_label = Label(self.quantity_frame, text="Item Number:", font='Lato 12',)
        self.item_number_label.grid(row=0, column=0, pady=5)
        self.item_number_entry = Entry(self.quantity_frame, font='Lato 12')
        self.item_number_entry.grid(row=0, column=1, pady=5)

        self.quantity_label = Label(self.quantity_frame, text="Quantity:", font='Lato 12',)
        self.quantity_label.grid(row=1, column=0, pady=5)
        self.quantity_entry = Entry(self.quantity_frame, font='Lato 12')
        self.quantity_entry.grid(row=1, column=1, pady=5)

        # BUTTON
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=TOP)

        self.add_btn = Button(self.button_frame, text="Add", font='Lato 12', command=self.add_item, width=8)
        self.add_btn.grid(row=0, column=0, padx=(0,3), pady=5)

        self.remove_btn = Button(self.button_frame, text="Remove", font='Lato 12', command=self.remove_item, width=8)
        self.remove_btn.grid(row=0, column=1, padx=(3,0), pady=5)

        self.quit_btn = Button(self.button_frame, text="Quit", font='Lato 12', command=self.exit, width=18)
        self.quit_btn.grid(row=1, column=0, columnspan=2, pady=5)

        self.display_inventory()

    def display_inventory(self):
        inventory_display = ""
        for item, quantity in self.inventory.items():
            inventory_display += f"{item}: {quantity}\n\n"
        self.output_label.config(text=inventory_display)

    def add_item(self):
        item_number = int(self.item_number_entry.get())
        if 1 <= item_number <= len(self.inventory):
            selected_item = list(self.inventory.keys())[item_number - 1]
            quantity = int(self.quantity_entry.get())
            self.inventory[selected_item] += quantity
            self.display_inventory()
        else:
            pass

    def remove_item(self):
        item_number = int(self.item_number_entry.get())
        if 1 <= item_number <= len(self.inventory):
            selected_item = list(self.inventory.keys())[item_number - 1]
            quantity = int(self.quantity_entry.get())
            if quantity <= self.inventory[selected_item]:
                self.inventory[selected_item] -= quantity
                self.display_inventory()
            else:
                self.inventory[selected_item] = 0
                self.display_inventory()
                # self.output_label.config(text="Quantity to remove exceeds the available quantity.")
        else:
            pass
            # self.output_label.config(text="Invalid item number.")

    def exit(self):
        self.main_frame.destroy()
        self.window.title("Main Menu")
        self.func()

# window = Tk()
# window.state('normal')
# window.geometry("640x480")
# window.resizable(False, False)
# window.title('Inventory')
#
# def Pass():
#      pass
#
# InventoryApp(window, Pass())
# window.mainloop()
