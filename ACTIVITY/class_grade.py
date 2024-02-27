from tkinter import *
from tkinter.ttk import Notebook, Progressbar, Separator, Style
from random import randint
from faker import Faker

# {"configure": {"background": 'white',"foreground": "white", "relief": "flat"}}


class Grades:
    def __init__(self, window, func):
        def adjust_scrollregion(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.window = window
        self.func = func
        self.window.bind_all("<Button-1>", lambda event: event.widget.focus())

        self.listq1 = []
        self.listq2 = []
        self.listq3 = []
        self.listq4 = []
        self.listq5 = []

        # self.style = Style()

        # self.style.theme_create('no margin', settings={'.': {"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}, "borderwidth": 0}}})

        # self.style.theme_use('no margin')

        self.menu_frame = Frame(window)
        self.menu_frame.pack(fill=BOTH, expand=True)

        #   NOTEBOOK SETUP
        self.notebook = Notebook(self.menu_frame,)

        self.addtab = Frame(self.notebook)
        self.gradetab = Frame(self.notebook)

        self.notebook.add(self.addtab, text='Insert')
        self.notebook.add(self.gradetab, text='Grades')

        self.notebook.pack(expand=True, fill=BOTH)

        #   FRAME SETUP
        self.addtab_frame = Frame(self.addtab)
        self.addtab_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.gradetab_frame = Frame(self.gradetab)
        self.gradetab_frame.pack(fill=BOTH, expand=True)

        #   STUDENT SETUP
        self.student_frame = Frame(self.addtab_frame)
        self.student_frame.pack(side=TOP)

        self.studentFN_frame = Frame(self.student_frame)
        self.studentFN_frame.pack(side=LEFT, padx=5)

        self.studentLN_frame = Frame(self.student_frame)
        self.studentLN_frame.pack(side=LEFT, padx=5)

        self.studentFN_label = Label(self.studentFN_frame, text='FIRST NAME:', font='Lato 12')
        self.studentFN_label.pack(side=LEFT, padx=(0,10))

        self.studentFN_entry = Entry(self.studentFN_frame, font='Lato 12')
        self.studentFN_entry.pack(side=LEFT)

        self.studentLN_label = Label(self.studentLN_frame, text='LAST NAME:', font='Lato 12')
        self.studentLN_label.pack(side=LEFT, padx=(0,10))

        self.studentLN_entry = Entry(self.studentLN_frame, font='Lato 12')
        self.studentLN_entry.pack(side=LEFT)

        #   GRADE SETUP
        self.grade_frame = Frame(self.addtab_frame)
        self.grade_frame.pack(side=TOP, pady=20)

        self.quiz1_label = Label(self.grade_frame, text='QUIZ 1:', font='Lato 12')
        self.quiz1_label.grid(row=0, column=0, pady=5, padx=(0,10))

        self.quiz1_entry = Entry(self.grade_frame, font='Lato 12')
        self.quiz1_entry.grid(row=0, column=1, pady=5, ipady=1)

        self.quiz2_label = Label(self.grade_frame, text='QUIZ 2:', font='Lato 12')
        self.quiz2_label.grid(row=1, column=0, pady=5, padx=(0,10))

        self.quiz2_entry = Entry(self.grade_frame, font='Lato 12')
        self.quiz2_entry.grid(row=1, column=1, pady=5, ipady=1)

        self.quiz3_label = Label(self.grade_frame, text='QUIZ 3:', font='Lato 12')
        self.quiz3_label.grid(row=2, column=0, pady=5, padx=(0,10))

        self.quiz3_entry = Entry(self.grade_frame, font='Lato 12')
        self.quiz3_entry.grid(row=2, column=1, pady=5, ipady=1)

        self.quiz4_label = Label(self.grade_frame, text='QUIZ 4:', font='Lato 12')
        self.quiz4_label.grid(row=3, column=0, pady=5, padx=(0,10))

        self.quiz4_entry = Entry(self.grade_frame, font='Lato 12')
        self.quiz4_entry.grid(row=3, column=1, pady=5, ipady=1)

        self.quiz5_label = Label(self.grade_frame, text='QUIZ 5:', font='Lato 12')
        self.quiz5_label.grid(row=4, column=0, pady=5, padx=(0,10))

        self.quiz5_entry = Entry(self.grade_frame, font='Lato 12')
        self.quiz5_entry.grid(row=4, column=1, pady=5, ipady=1)

        #   BUTTON SETUP
        self.button_frame = Frame(self.addtab_frame)
        self.button_frame.pack(side=TOP)

        self.add_button = Button(self.button_frame, text='ADD GRADES', font='Lato 12 ', width=15, command=lambda: self.add_grade(), borderwidth=4)
        self.add_button.grid(row=0, column=0, pady=5)

        self.random_button = Button(self.button_frame, text='RANDOMIZE', font='Lato 12', width=15, command=lambda: self.random(), borderwidth=4)
        self.random_button.grid(row=1, column=0, pady=5)

        self.clear_button = Button(self.button_frame, text='CLEAR', font='Lato 12', width=15, command=lambda: self.clear(), borderwidth=4)
        self.clear_button.grid(row=2, column=0, pady=5)

        self.exit_button = Button(self.button_frame, text='QUIT', font='Lato 12', width=15, command=lambda: self.exit(), borderwidth=4)
        self.exit_button.grid(row=3, column=0, pady=5)

        #   GRADE TAB
        self.stats_frame = Frame(self.gradetab_frame, relief=GROOVE, borderwidth=4)
        self.stats_frame.pack(side=LEFT, fill=Y, ipadx=10)

        self.classstat_label = Label(self.stats_frame, text=f'\nOverall Class Average: {0}\n', font='Lato 12')
        self.classstat_label.grid(row=0, column=0, sticky=W)

        self.stats1_label = Label(self.stats_frame, text=f'Quiz 1 Average: {0}', font='Lato 12')
        self.stats1_label.grid(row=1, column=0, sticky=W)

        self.stats2_label = Label(self.stats_frame, text=f'Quiz 2 Average: {0}', font='Lato 12')
        self.stats2_label.grid(row=2, column=0, sticky=W)

        self.stats3_label = Label(self.stats_frame, text=f'Quiz 3 Average: {0}', font='Lato 12')
        self.stats3_label.grid(row=3, column=0, sticky=W)

        self.stats4_label = Label(self.stats_frame, text=f'Quiz 4 Average: {0}', font='Lato 12')
        self.stats4_label.grid(row=4, column=0, sticky=W)

        self.stats5_label = Label(self.stats_frame, text=f'Quiz 5 Average: {0}', font='Lato 12')
        self.stats5_label.grid(row=5, column=0, sticky=W)

        self.tab_frame = Frame(self.gradetab_frame)
        self.tab_frame.pack(expand=TRUE, fill=BOTH)

        self.canvas= Canvas(self.tab_frame, highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.scroll= Scrollbar(self.tab_frame, bd=0, command=self.canvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.canvas.bind('<Configure>', lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.scroll_frame_settings = Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.scroll_frame_settings, anchor='n')

        self.scroll_frame_settings.bind("<Configure>", adjust_scrollregion)

        self.frame = Frame(self.scroll_frame_settings)
        self.frame.pack(padx=40)

    def random(self):
        fake = Faker()
        num = []
        for i in range(0,5):
            text = str(randint(5, 100))
            num.append(text)

        self.clear()

        self.studentFN_entry.insert(0, fake.first_name())

        self.studentLN_entry.insert(0, fake.last_name())

        self.quiz1_entry.insert(0,num[0])

        self.quiz2_entry.insert(0, num[1])

        self.quiz3_entry.insert(0, num[2])

        self.quiz4_entry.insert(0, num[3])

        self.quiz5_entry.insert(0, num[4])

    def clear(self):
        self.studentFN_entry.delete(0, END)
        self.studentLN_entry.delete(0, END)
        self.quiz1_entry.delete(0, END)
        self.quiz2_entry.delete(0, END)
        self.quiz3_entry.delete(0, END)
        self.quiz4_entry.delete(0, END)
        self.quiz5_entry.delete(0, END)

    def updatestat(self):
        av1 = round(sum(self.listq1) /len(self.listq1), 2)
        av2 = round(sum(self.listq2) / len(self.listq2), 2)
        av3 = round(sum(self.listq3) / len(self.listq3), 2)
        av4 = round(sum(self.listq4) / len(self.listq4), 2)
        av5 = round(sum(self.listq5) / len(self.listq5), 2)
        classav = round((av1+av2+av3+av4+av5) / 5)

        self.classstat_label.configure(text=f'\nOverall Class Average: {classav}\n')
        self.stats1_label.configure(text=f'Quiz 1 Average: {av1}')
        self.stats2_label.configure(text=f'Quiz 2 Average: {av2}')
        self.stats3_label.configure(text=f'Quiz 3 Average: {av3}')
        self.stats4_label.configure(text=f'Quiz 4 Average: {av4}')
        self.stats5_label.configure(text=f'Quiz 5 Average: {av5}')

    def add_grade(self):
        quiz1 = int(self.quiz1_entry.get())
        quiz2 = int(self.quiz2_entry.get())
        quiz3 = int(self.quiz3_entry.get())
        quiz4 = int(self.quiz4_entry.get())
        quiz5 = int(self.quiz5_entry.get())

        self.listq1.append(quiz1)
        self.listq2.append(quiz2)
        self.listq3.append(quiz3)
        self.listq4.append(quiz4)
        self.listq5.append(quiz5)

        average = (quiz1+quiz2+quiz3+quiz4+quiz5)/5

        self.label = Label(self.frame,
                           text=f'\n      Name: {self.studentFN_entry.get()} {self.studentLN_entry.get()}\n      Quiz Average: {average}\n\n      Quiz 1: {quiz1}\n      Quiz 2: {quiz2}\n      Quiz 3: {quiz3}\n      Quiz 4: {quiz4}\n      Quiz 5: {quiz5}\n',
                           font='lato 15',
                           justify=LEFT,
                           width=30,
                           anchor=W,
                           takefocus=0,
                           relief=RAISED,
                           borderwidth=4)

        self.label.pack(side=TOP, pady=10)

        self.updatestat()

    def exit(self):
        self.menu_frame.destroy()
        self.window.title("Main Menu")
        self.func()


# window = Tk()
#
# def Pass():
#     pass
#
# Grades(window, Pass)
# window.title("Cipher Encoder")
# window.state('normal')
# window.geometry("640x480")
# window.resizable(False, False)
# window.mainloop()
