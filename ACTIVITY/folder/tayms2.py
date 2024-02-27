from tkinter import *
import tkinter.font
import random

class Tayms:
    def __init__(self, window, func):
        self.window = window
        self.func = func

        self.lives = 0
        self.points = 0
        self.current_screen = "Main"  # Set initial screen to Main
        self.average_range = None
        self.difficult_range = None
        self.correct_answer = None

        self.main_frame = Frame(window, bg="#000000")
        self.main_frame.pack(fill=BOTH, expand=True, side=RIGHT)

        self.canvas = Canvas(
            self.main_frame,
            bg="#000000",
            height=480,
            width=640,
            bd=0,
            highlightthickness=0,
            relief="ridge")

        self.canvas.place(x=0, y=0)

        self.img0 = PhotoImage(file="s1/img0.png")

        self.b_start = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.start_game,
            relief="flat",
            bg="#000000",
            activebackground="#000000")
        self.b_start.place(
            x=205, y=300,
            width=231,
            height=60)

        self.img1 = PhotoImage(file="s1/img1.png")
        self.b_quit = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.close,
            relief="flat",
            bg="#000000",
            activebackground="#000000")
        self.b_quit.place(
            x=205, y=370,
            width=231,
            height=60)

        # Level selection buttons (Initially hidden)
        self.img2 = PhotoImage(file="s1/easy.png")
        self.b_easy = Button(
            self.main_frame,
            image=self.img2,
            borderwidth=0,
            command=lambda: self.choose_level("Easy"),
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        self.img3 = PhotoImage(file="s1/ave.png")
        self.b_average = Button(
            self.main_frame,
            image=self.img3,
            borderwidth=0,
            command=lambda: self.choose_level("Average"),
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        self.img4 = PhotoImage(file="s1/diff.png")

        self.b_difficult = Button(
            self.main_frame,
            image=self.img4,
            borderwidth=0,
            command=lambda: self.choose_level("Difficult"),
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        self.img5 = PhotoImage(file="s1/back.png")

        self. b_back = Button(
            self.main_frame,
            image=self.img5,
            command=self.go_back,
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        # Game window
        self.canvas_game = Canvas(
            self.main_frame,
            bg="#000000",
            height=480,
            width=640,
            bd=0,
            highlightthickness=0,
            relief="ridge")

        self.imgy = PhotoImage(file="s1/quit.png")
        self.b_quit_game = Button(
            self.main_frame,
            image=self.imgy,
            command=self.quit_game,
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        self. label_lives = Label(
            self.main_frame,
            text="Lives: 0",
            bg="#000000",
            fg="#ff5994",
            font=("Comic Sans MS", 15)
        )

        self.label_points = Label(
            self.main_frame,
            text="Points: 0",
            bg="#000000",
            fg="#edff8f",
            font=("Comic Sans MS", 15)
        )
        self.entry_answer = Entry(
            self.main_frame,
            bg="#ffffff",
            fg="#000000",
            font=("Comic Sans MS", 12)
        )

        self.label_result = Label(
            self.main_frame,
            text="",
            bg="#000000",
            fg="#ffffff",
            font=("Comic Sans MS", 12)
        )

        self.imgx = PhotoImage(file="s1/img6.png")

        self.label_difficulty = Label(
            self.main_frame,
            image=self.imgx,
            bg="#000000",

        )

        self.imgz = PhotoImage(file="s1/check.png")

        self.b_check = Button(
            self.main_frame,
            image=self.imgz,
            command=self.check_answer,
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        # Game over window
        self.canvas_game_over = Canvas(
            self.main_frame,
            bg="#000000",
            height=480,
            width=640,
            bd=0,
            highlightthickness=0,
            relief="ridge")

        self.imga = PhotoImage(file="s1/mm.png")

        self.b_main_menu = Button(
            self.main_frame,
            image=self.imga,
            command=self.back_to_main_menu,
            relief="flat",
            bg="#000000",
            activebackground="#000000",
        )

        self.imgb = PhotoImage(file="s1/gmov.png")

        self.label_game_over = Label(
            self.main_frame,
            image=self.imgb,
            bg="#000000",

        )

        self.label_tpoints = Label(
            self.main_frame,
            fg="#ffffff",
            bg="#000000",
            font=("Comic Sans MS", 20)
        )

        self.img6 = PhotoImage(file="s1/htpl.png")

        self.b_instruction = Button(
            self.main_frame,
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.instruction,
            relief="flat",
            bg="#000000",
            activebackground="#000000"

        )

        self.b_instruction.place(
            x=205, y=225,
            width=231,
            height=60)

        self.img7 = PhotoImage(file="s1/inst.png")

        self.label_instruction = Label(
            self.main_frame,
            image=self.img7,
            bg="#000000"
        )

        self.img8 = PhotoImage(file="s1/ok.png")

        self.b_ok = Button(
            self.main_frame,
            image=self.img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_ok,
            relief="flat",
            bg="#000000",
            activebackground="#000000"
        )
        self.img9 = PhotoImage(file="s1/gotthis.png")
        self.label_gotthis = Label(
            self.main_frame,
            image=self.img9,
            bg="#000000"
        )
        self.img10 = PhotoImage(file="s1/tayms.png")
        self.label_tayms = Label(
            image=self.img10,
            bg="#000000"
        )
        self.label_tayms.place(
            x=150,
            y=50
        )

    def start_game(self):
        global current_screen
        current_screen = "ChooseLevel"

        self.canvas.place_forget()
        self.b_instruction.place_forget()
        self.b_start.place_forget()
        self.b_quit.place_forget()
        self.label_tayms.place_forget()

        # Show level selection
        self.label_difficulty.place(x=115, y=50)
        self.b_easy.place(x=70, y=100)
        self.b_average.place(x=70, y=200)
        self.b_difficult.place(x=70, y=315)
        self.b_back.place(x=20, y=20)

    def instruction(self):
        global current_screen
        current_screen = "HowToPlay"

        self.canvas.place_forget()
        self.b_instruction.place_forget()
        self.b_start.place_forget()
        self.b_quit.place_forget()
        self.b_instruction.place_forget()
        self.label_tayms.place_forget()

        self.label_instruction.place(x=40, y=50)
        self.b_ok.place(x=540, y=425)

    def btn_ok(self):
        global current_screen

        # Show initial content
        self.canvas.place(x=0, y=0)
        self.b_instruction.place(x=205, y=225, width=231, height=60)
        self.b_start.place(x=205, y=300, width=231, height=60)
        self.b_quit.place(x=205, y=370, width=231, height=60)
        self.label_tayms.place(x=150, y=50, )

        self.label_instruction.place_forget()
        self.b_ok.place_forget()
        current_screen = "Main"

    def go_back(self):
        global current_screen

        # Show initial content
        self.canvas.place(x=0, y=0)
        self.b_instruction.place(x=205, y=225, width=231, height=60)
        self.b_start.place(x=205, y=300, width=231, height=60)
        self.b_quit.place(x=205, y=370, width=231, height=60)
        self.label_tayms.place(x=150, y=50, )

        self.label_difficulty.place_forget()
        self.b_easy.place_forget()
        self.b_average.place_forget()
        self.b_difficult.place_forget()
        self.b_back.place_forget()
        current_screen = "Main"  # Set current level back to Main

    def quit_game(self):
        global current_screen
        current_screen = "ChooseLevel"  # Set current level back to ChooseLevel
        self.canvas_game.place_forget()
        self.b_quit_game.place_forget()
        self.label_lives.place_forget()
        self.label_points.place_forget()
        self.entry_answer.place_forget()
        self.label_result.place_forget()
        self.b_check.place_forget()
        self.label_gotthis.place_forget()
        self.start_game()  # Display level selection screen when quitting game
        print("Game quit")

    def choose_level(self, level):
        global current_screen, average_range, difficult_range
        current_screen = level  # Set current screen to the chosen level
        if level == "Easy":
            self.start_game_window(range_val=3)
        elif level == "Average":
            average_range = (0, 7)
            self.start_game_window(range_val=average_range)
        elif level == "Difficult":
            difficult_range = (0, 10)
            self.start_game_window(range_val=difficult_range)

    def draw_colorful_text(self, canvas, x, y, text, colors, font_name, size):
        font = tkinter.font.Font(family=font_name, size=size, weight="bold")
        x_offset = 0
        for i, letter in enumerate(text):
            canvas.create_text(x + x_offset, y, text=letter, fill=colors[i % len(colors)], font=font)
            x_offset += font.measure(letter)

    def generate_random_problem(self, range_val):
        global correct_answer
        if isinstance(range_val, tuple):
            a = random.randint(range_val[0], range_val[1])
            b = random.randint(range_val[0], range_val[1])
        else:
            a = random.randint(0, range_val)
            b = random.randint(0, range_val)
        problem_text = f"{a} x {b}"
        correct_answer = a * b
        return problem_text

    def start_game_window(self, range_val):
        global lives, points

        # Show game content
        self.canvas_game.place(x=0, y=0)
        self.b_quit_game.place(x=20, y=20)  # Corrected placement of Quit button
        self.label_lives.place(x=520, y=20)
        self.label_points.place(x=520, y=50)
        self.entry_answer.place(x=225, y=275, width=140, height=30)
        self.label_result.place(x=275, y=325)
        self.b_check.place(x=385, y=270, height=40)
        self.label_gotthis.place(x=0, y=315)
        self.label_difficulty.place_forget()

        lives = 10
        self.update_lives_label()
        points = 0
        self.update_points_label()

        self.generate_and_display_problem(range_val)
        self.entry_answer.bind("<Return>", lambda event: self.check_answer())

    def generate_and_display_problem(self, range_val):
        problem_text = self.generate_random_problem(range_val)
        self.canvas_game.delete("all")
        self.canvas_game.create_text(320, 200, text=problem_text, fill="#ffffff", font=("Comic Sans MS", 48))
        self.entry_answer.delete(0, END)
        self.label_result.config(text="")

    def check_answer(self):
        global lives, points, correct_answer, current_screen, average_range, difficult_range
        # Disable the Check button to prevent spammerz :P
        self.b_check.config(state=DISABLED)
        user_answer = self.entry_answer.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                self.label_result.config(text="Correct!")
                addition = 1 if current_screen == "Easy" else 2 if current_screen == "Average" else 5
                points = points + addition
                self.update_points_label()
                self.window.after(1000, self.generate_and_display_problem,
                             average_range if current_screen == "Average" else difficult_range if current_screen == "Difficult" else 3)
            else:
                self.label_result.config(text="Incorrect!\nTry again.")
                deduction = 0.5 if current_screen == "Easy" else 1 if current_screen == "Average" else 2
                lives = max(lives - deduction, 0)
                self.update_lives_label()
                print(f"Lives deducted: {deduction}")
                if lives == 0:
                    self.game_over()
        else:
            self.label_result.config(text="Invalid input!\nTry again.")  # Print message for invalid input
        # Re-enable the Check button after a delay
        self.window.after(1000, lambda: self.b_check.config(state=NORMAL))

    def update_lives_label(self):
        self.label_lives.config(text=f"Lives: {lives}")

    def update_points_label(self):
        self.label_points.config(text=f"Points: {points}")
        self.label_tpoints.config(text=f"Points: {points}")

    def game_over(self):
        global current_screen, points
        current_screen = "GameOver"  # Set current level to GameOver
        # Hide game content
        self.canvas_game.place_forget()
        self.b_quit_game.place_forget()
        self.label_lives.place_forget()
        self.label_points.place_forget()
        self.entry_answer.place_forget()
        self.label_result.place_forget()
        self.b_check.place_forget()
        self.label_gotthis.place_forget()
        # Show game over screen
        self.canvas_game_over.place(x=0, y=0)
        self.b_main_menu.place(x=225, y=300)
        self.label_game_over.place(x=75, y=100)
        self.label_tpoints.place(x=225, y=230)
        self.label_tpoints.config(text="Total Points: " + str(points))

    def close(self):
        self.canvas.destroy()
        self.b_instruction.destroy()
        self.b_start.destroy()
        self.b_quit.destroy()
        self.label_tayms.destroy()
        self.main_frame.destroy()

        self.window.title("Main Menu")
        self.func()

    def back_to_main_menu(self):
        global current_screen, lives, points
        lives = 0  # Reset points
        points = 0
        self.canvas_game_over.place_forget()
        self.b_main_menu.place_forget()
        self.label_difficulty.place_forget()
        self.b_easy.place_forget()
        self.b_average.place_forget()
        self.b_difficult.place_forget()
        self.b_back.place_forget()
        self.label_game_over.place_forget()
        self.label_tpoints.place_forget()
        # Show initial content
        self.canvas.place(x=0, y=0)
        self.b_start.place(x=205, y=300, width=231, height=60)
        self.b_instruction.place(x=205, y=225, width=231, height=60)
        self.b_quit.place(x=205, y=370, width=231, height=60)
        self.label_tayms.place(x=150, y=50, )
        current_screen = "Main"


# def Pass():
#      pass
#
# window = Tk()
# Tayms(window, Pass())
#
# window.geometry("640x480")
# window.configure(bg="#000000")
# window.title("TAYMS X")
#
# window.resizable(False, True)
# window.mainloop()
