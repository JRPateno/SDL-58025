from tkinter import *
import tkinter.font
import random

lives = 0
points = 0
current_screen = "Main"  # Set initial screen to Main
average_range = None
difficult_range = None
correct_answer = None


def start_game():
    global current_screen
    current_screen = "ChooseLevel"

    canvas.place_forget()
    b_instruction.place_forget()
    b_start.place_forget()
    b_quit.place_forget()
    label_tayms.place_forget()

    # Show level selection
    label_difficulty.place(x=115, y=50)
    b_easy.place(x=70, y=100)
    b_average.place(x=70, y=200)
    b_difficult.place(x=70, y=315)
    b_back.place(x=20, y=20)

def instruction():
    global current_screen
    current_screen = "HowToPlay"

    canvas.place_forget()
    b_instruction.place_forget()
    b_start.place_forget()
    b_quit.place_forget()
    b_instruction.place_forget()
    label_tayms.place_forget()

    label_instruction.place(x=40,y=50)
    b_ok.place(x=540,y=425)

def btn_ok():
    global current_screen

    # Show initial content
    canvas.place(x=0, y=0)
    b_instruction.place(x=205, y=225,width=231, height=60)
    b_start.place(x=205, y=300, width=231, height=60)
    b_quit.place(x=205, y=370, width=231, height=60)
    label_tayms.place(x=150,y=50,)

    label_instruction.place_forget()
    b_ok.place_forget()
    current_screen="Main"


def go_back():
    global current_screen

    # Show initial content
    canvas.place(x=0, y=0)
    b_instruction.place(x=205, y=225,width=231, height=60)
    b_start.place(x=205, y=300, width=231, height=60)
    b_quit.place(x=205, y=370, width=231, height=60)
    label_tayms.place(x=150, y=50, )

    label_difficulty.place_forget()
    b_easy.place_forget()
    b_average.place_forget()
    b_difficult.place_forget()
    b_back.place_forget()
    current_screen = "Main"  # Set current level back to Main


def quit_game():
    global current_screen
    current_screen = "ChooseLevel"  # Set current level back to ChooseLevel
    canvas_game.place_forget()
    b_quit_game.place_forget()
    label_lives.place_forget()
    label_points.place_forget()
    entry_answer.place_forget()
    label_result.place_forget()
    b_check.place_forget()
    label_gotthis.place_forget()
    start_game()  # Display level selection screen when quitting game
    print("Game quit")


def choose_level(level):
    global current_screen, average_range, difficult_range
    current_screen = level  # Set current screen to the chosen level
    if level == "Easy":
        start_game_window(range_val=3)
    elif level == "Average":
        average_range = (0, 7)
        start_game_window(range_val=average_range)
    elif level == "Difficult":
        difficult_range = (0, 10)
        start_game_window(range_val=difficult_range)


def draw_colorful_text(canvas, x, y, text, colors, font_name, size):
    font = tkinter.font.Font(family=font_name, size=size, weight="bold")
    x_offset = 0
    for i, letter in enumerate(text):
        canvas.create_text(x + x_offset, y, text=letter, fill=colors[i % len(colors)], font=font)
        x_offset += font.measure(letter)


def generate_random_problem(range_val):
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


def start_game_window(range_val):
    global lives, points

    # Show game content
    canvas_game.place(x=0, y=0)
    b_quit_game.place(x=20, y=20)  # Corrected placement of Quit button
    label_lives.place(x=520, y=20)
    label_points.place(x=520, y=50)
    entry_answer.place(x=225, y= 275, width=140, height= 30)
    label_result.place(x=275, y=325)
    b_check.place(x=385, y=270, height=40)
    label_gotthis.place(x=0, y=315)
    label_difficulty.place_forget()

    lives = 10
    update_lives_label()
    points =0
    update_points_label()

    generate_and_display_problem(range_val)
    entry_answer.bind("<Return>", lambda event: check_answer())

def generate_and_display_problem(range_val):
    problem_text = generate_random_problem(range_val)
    canvas_game.delete("all")
    canvas_game.create_text(320, 200, text=problem_text, fill="#ffffff", font=("Comic Sans MS", 48))
    entry_answer.delete(0, END)
    label_result.config(text="")


def check_answer():
    global lives, points, correct_answer, current_screen, average_range, difficult_range
    # Disable the Check button to prevent spammerz :P
    b_check.config(state=DISABLED)
    user_answer = entry_answer.get()
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            label_result.config(text="Correct!")
            addition = 1 if current_screen == "Easy" else 2 if current_screen == "Average" else 5
            points = points + addition
            update_points_label()
            window.after(1000, generate_and_display_problem,
                         average_range if current_screen == "Average" else difficult_range if current_screen == "Difficult" else 3)
        else:
            label_result.config(text="Incorrect!\nTry again.")
            deduction = 0.5 if current_screen == "Easy" else 1 if current_screen == "Average" else 2
            lives = max(lives - deduction, 0)
            update_lives_label()
            print(f"Lives deducted: {deduction}")
            if lives == 0:
                game_over()
    else:
        label_result.config(text="Invalid input!\nTry again.")  # Print message for invalid input
    # Re-enable the Check button after a delay
    window.after(1000, lambda: b_check.config(state=NORMAL))

def update_lives_label():
    label_lives.config(text=f"Lives: {lives}")

def update_points_label():
    label_points.config(text=f"Points: {points}")
    label_tpoints.config(text=f"Points: {points}")


def game_over():
    global current_screen,points
    current_screen = "GameOver"  # Set current level to GameOver
    # Hide game content
    canvas_game.place_forget()
    b_quit_game.place_forget()
    label_lives.place_forget()
    label_points.place_forget()
    entry_answer.place_forget()
    label_result.place_forget()
    b_check.place_forget()
    label_gotthis.place_forget()
    # Show game over screen
    canvas_game_over.place(x=0, y=0)
    b_main_menu.place(x=225, y=300)
    label_game_over.place(x= 75, y=100)
    label_tpoints.place(x=225, y=230)
    label_tpoints.config(text="Total Points: " + str(points))


def close():
    window.destroy()


def back_to_main_menu():
    global current_screen, lives, points
    lives = 0  # Reset points
    points = 0
    canvas_game_over.place_forget()
    b_main_menu.place_forget()
    label_difficulty.place_forget()
    b_easy.place_forget()
    b_average.place_forget()
    b_difficult.place_forget()
    b_back.place_forget()
    label_game_over.place_forget()
    label_tpoints.place_forget()
    # Show initial content
    canvas.place(x=0, y=0)
    b_start.place(x=205, y=300, width=231, height=60)
    b_instruction.place(x=205, y=225, width=231, height=60)
    b_quit.place(x=205, y=370, width=231, height=60)
    label_tayms.place(x=150, y=50, )
    current_screen = "Main"


window = Tk()
window.geometry("640x480")
window.configure(bg="#000000")
window.title("TAYMS X")

# Initial content
canvas = Canvas(
    window,
    bg="#000000",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file="img0.png")
b_start = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=start_game,
    relief="flat",
    bg="#000000",
    activebackground="#000000")
b_start.place(
    x=205, y=300,
    width=231,
    height=60)

img1 = PhotoImage(file="img1.png")
b_quit = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=close,
    relief="flat",
    bg="#000000",
    activebackground="#000000")
b_quit.place(
    x=205, y=370,
    width=231,
    height=60)

# Level selection buttons (Initially hidden)
img2= PhotoImage(file="easy.png")
b_easy = Button(
    window,
    image= img2,
    borderwidth=0,
    command=lambda: choose_level("Easy"),
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

img3= PhotoImage(file="ave.png")
b_average = Button(
    window,
    image= img3,
    borderwidth=0,
    command=lambda: choose_level("Average"),
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

img4= PhotoImage(file="diff.png")
b_difficult = Button(
    window,
    image= img4,
    borderwidth=0,
    command=lambda: choose_level("Difficult"),
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

img5=PhotoImage(file="back.png")

b_back = Button(
    window,
    image=img5,
    command=go_back,
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

# Game window
canvas_game = Canvas(
    window,
    bg="#000000",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge")

imgy=PhotoImage(file="quit.png")
b_quit_game = Button(
    window,
    image=imgy,
    command=quit_game,
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

label_lives = Label(
    window,
    text="Lives: 0",
    bg="#000000",
    fg="#ff5994",
    font=("Comic Sans MS", 15)
)

label_points = Label(
    window,
    text="Points: 0",
    bg="#000000",
    fg="#edff8f",
    font=("Comic Sans MS", 15)
)
entry_answer = Entry(
    window,
    bg="#ffffff",
    fg="#000000",
    font=("Comic Sans MS", 12)
)

label_result = Label(
    window,
    text="",
    bg="#000000",
    fg="#ffffff",
    font=("Comic Sans MS", 12)
)

imgx = PhotoImage(file="img6.png")
label_difficulty = Label(
    window,
    image= imgx,
    bg="#000000",

)

imgz = PhotoImage(file="check.png")
b_check = Button(
    window,
    image=imgz,
    command=check_answer,
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

# Game over window
canvas_game_over = Canvas(
    window,
    bg="#000000",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge")


imga = PhotoImage (file="mm.png")
b_main_menu = Button(
    window,
    image= imga,
    command=back_to_main_menu,
    relief="flat",
    bg="#000000",
    activebackground="#000000",
)

imgb=PhotoImage(file="gmov.png")
label_game_over = Label(
    window,
    image=imgb,
    bg="#000000",

)
label_tpoints = Label(
    window,
    fg="#ffffff",
    bg="#000000",
    font=("Comic Sans MS", 20)
)

img6 = PhotoImage(file="htpl.png")
b_instruction = Button(
    window,
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=instruction,
    relief="flat",
    bg="#000000",
    activebackground="#000000"

)
b_instruction.place(
    x=205, y=225,
    width=231,
    height=60)

img7 = PhotoImage(file="inst.png")
label_instruction = Label(
    window,
    image=img7,
    bg="#000000"
)
img8=PhotoImage(file="ok.png")
b_ok= Button(
    window,
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn_ok,
    relief="flat",
    bg="#000000",
    activebackground="#000000"
)
img9 = PhotoImage(file="gotthis.png")
label_gotthis = Label(
    window,
    image=img9,
    bg="#000000"
)
img10=PhotoImage(file="tayms.png")
label_tayms = Label(
    image=img10,
    bg="#000000"
)
label_tayms.place(
    x = 150,
    y=50
)

window.resizable(False, True)
window.mainloop()