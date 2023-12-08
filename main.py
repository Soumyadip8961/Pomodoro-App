from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
reset_timer = ''
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(reset_timer)
    timer_lable.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text=f"00:00")
    global reps
    reps=0
    tick_label.config(text="✔" * (reps // 2))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 2 != 0:
        timer_lable.config(text="Work", fg=GREEN)
        count_down(work_sec)
        tick_label.config(text="✔" * (reps // 2))



    elif reps % 8 == 0:
        timer_lable.config(text="Break", fg=RED)
        count_down(long_break_sec)
        tick_label.config(text="✔" * (reps // 2))


    elif reps%2 == 0:
        timer_lable.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        tick_label.config(text="✔" * (reps // 2))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minutes=count//60
    seconds=count%60
    if seconds <=9:
        seconds = f"0{seconds}" ##This line of code is an Example of "Dynamic Typing"
    if count>=0:
        global reset_timer
        reset_timer=window.after(1000, count_down, count-1 ) #Here, 'count_down' fucn is called after each seconds-
                                                             #and 'count' is decreased by 1
        canvas.itemconfig(timer,text=f"{minutes}:{seconds}")
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_lable=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer_lable.config(pady=10)
timer_lable.grid(column=1, row=0)


start_button=Button(text="Start", bg="white", borderwidth=0, command=start)
start_button.grid(column=0, row=2, pady=10)

reset_button=Button(text="Reset", bg="white", borderwidth=0, command=reset)
reset_button.grid(column=2, row=2, pady=10)

tick_label=Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
tick_label.grid(column=1, row=3)

window.mainloop()